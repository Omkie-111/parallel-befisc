FROM python:3.10.12-slim-buster

RUN mkdir -p /befisc
COPY . /befisc/
WORKDIR /befisc/

RUN apt-get update && \
    apt-get install -y python3-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python3", "main/run.py"]
