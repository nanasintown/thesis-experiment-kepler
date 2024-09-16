FROM python:3.8

COPY . /app
WORKDIR /app

RUN apt-get update
RUN pip3 install --no-cache-dir -r /app/requirements.txt

CMD ["python3", "workload.py"]
