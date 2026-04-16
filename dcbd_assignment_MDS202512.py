import requests
import time
from multiprocessing import Pool, cpu_count, freeze_support
from collections import Counter

BASE_URL = "http://72.60.221.150:8080"
STUDENT_ID = "MDS202512"


# ---------------- LOGIN ----------------
def login(student_id):
    url = f"{BASE_URL}/login"
    response = requests.post(url, json={"student_id": student_id}, timeout=5)

    if response.status_code == 200:
        return response.json()["secret_key"]
    else:
        raise Exception("Login failed")


# ---------------- FETCH TITLE ----------------
def get_publication_title(args):
    secret_key, filename = args
    url = f"{BASE_URL}/lookup"

    while True:
        try:
            response = requests.post(
                url,
                json={
                    "secret_key": secret_key,
                    "filename": filename
                },
                timeout=5
            )

            if response.status_code == 200:
                return response.json()["title"]

            elif response.status_code == 429:
                time.sleep(0.2)

            else:
                return None

        except requests.exceptions.RequestException:
            time.sleep(0.2)


# ---------------- MAP FUNCTION ----------------
def mapper(titles_chunk):
    counter = Counter()

    for title in titles_chunk:
        if title:
            words = title.strip().split()

            if len(words) > 0:
                first_word = words[0].strip(".,:;!?\"'()[]")
                counter[first_word] += 1

    return counter


# ---------------- CHUNKING ----------------
def chunkify(lst, n):
    chunk_size = len(lst) // n
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


# ---------------- VERIFY ----------------
def verify_top_10(student_id, top_10_list):
    secret_key = login(student_id)

    url = f"{BASE_URL}/verify"

    response = requests.post(
        url,
        json={
            "secret_key": secret_key,
            "top_10": top_10_list
        },
        timeout=5
    )

    if response.status_code == 200:
        print("Verification Result:", response.json())
    else:
        print("Verification failed")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    freeze_support()

    filenames = [f"pub_{i}.txt" for i in range(1000)]

    secret_key = login(STUDENT_ID)

    args = [(secret_key, fname) for fname in filenames]

    num_workers = min(4, cpu_count())

    # STEP 1: fetch titles
    with Pool(num_workers) as pool:
        titles = pool.map(get_publication_title, args)

    # STEP 2: map-reduce
    chunks = chunkify(titles, num_workers)

    with Pool(num_workers) as pool:
        results = pool.map(mapper, chunks)

    # REDUCE
    final_counter = Counter()
    for c in results:
        final_counter.update(c)

    top_10 = [word for word, _ in final_counter.most_common(10)]

    print("Top 10 words:", top_10)

    verify_top_10(STUDENT_ID, top_10)