FROM python:3.11.1-buster

WORKDIR /

ADD requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip

RUN pip install --upgrade -r /requirements.txt --no-cache-dir 
RUN pip install runpod --no-cache-dir 

COPY . .
RUN rm /requirements.txt


CMD [ "python", "-u", "/handler.py" ]