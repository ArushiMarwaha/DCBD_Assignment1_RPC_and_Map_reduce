\# DCBD Assignment 1 — RPC and MapReduce



\## Overview

This project implements a distributed-style computation using RPC concepts to analyze publication metadata. The objective is to extract and verify the most frequent words using a MapReduce-like approach.



\---



\## Implementation Details



\- \*\*Language:\*\* Python  

\- \*\*Approach:\*\*

&#x20; - Map step: Extract words from metadata  

&#x20; - Reduce step: Aggregate word frequencies  

&#x20; - Output: Top 10 most frequent words along with verification results  



\---



\## How to Run



\### Run Locally

```bash

python dcbd\_assignment\_MDS202512.py

```



\### Run Using Docker

```bash

docker build -t rpcmap\_assignment .

docker run rpcmap\_assignment

```



\---



\## Sample Output



```text

Top 10 words: \['Advanced', 'Analytical', 'Comprehensive', 'Automated', 'Distributed', 'Dynamic', 'Fundamental', 'Heuristic', 'Experimental', 'Global']



Verification Result:

{'correct': True, 'message': 'Congratulations! You found all top 10 first words.', 'score': 10, 'total': 10}

```



\---



\## Docker Configuration



\- \*\*Base Image:\*\* python:3.10-slim  

\- \*\*Dependencies:\*\* requests  

\- \*\*Execution:\*\* Runs the main script automatically  



\---



\## Repository Structure



\- `dcbd\_assignment\_MDS202512.py` — main implementation  

\- `Dockerfile` — container configuration  

\- `output.png` — Codespace execution screenshot  



\---



\## Result



The program successfully computes the top 10 most frequent words and verifies correctness with a full score (10/10). The solution is reproducible using Docker.



\---



\## Author



Arushi Marwaha  

Roll Number: MDS202512

