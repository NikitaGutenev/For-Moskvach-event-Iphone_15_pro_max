FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt install build-essential python3-dev libgmp3-dev -y && \
    apt install git -y && \
    apt install nano -y && \
    pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


CMD [ "python", "./main.py" ]