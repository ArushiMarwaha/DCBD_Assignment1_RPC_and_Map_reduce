FROM python:3.10-slim

WORKDIR /app
COPY dcbd_assignment_MDS202512.py .

RUN pip install --no-cache-dir requests

CMD ["python", "dcbd_assignment_MDS202512.py"]