FROM python:3.11.1-buster

WORKDIR /

ADD requirements.txt .

RUN pip install -r requirements.txt
RUN pip install bitsandbytes accelerate

COPY . .

CMD [ "python", "-u", "/handler.py" ]