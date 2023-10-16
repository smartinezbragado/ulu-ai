FROM python:3.11.1-buster

WORKDIR /

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-u", "/handler.py" ]