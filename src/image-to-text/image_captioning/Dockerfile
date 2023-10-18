FROM python:3.11.1-buster

WORKDIR /

ADD requirements.txt .

RUN pip install -r requirements.txt

ENV HF_HOME="/runpod-volume"

COPY . .

CMD [ "python", "-u", "/handler.py" ]