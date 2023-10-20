FROM python:3.11.1-buster

WORKDIR /

ADD requirements.txt .

RUN pip install --upgrade -r /requirements.txt --no-cache-dir 

COPY handler.py /
COPY utils.py /

CMD [ "python", "-u", "/handler.py" ]