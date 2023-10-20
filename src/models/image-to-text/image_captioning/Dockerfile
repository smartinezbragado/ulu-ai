FROM python:3.11.1-buster

WORKDIR /

ADD requirements.txt .

RUN pip install --upgrade -r /requirements.txt --no-cache-dir 

ENV HF_HOME="/runpod-volume"

COPY . .

CMD [ "python", "-u", "/handler.py" ]