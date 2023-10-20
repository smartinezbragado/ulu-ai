# Base image
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

# Use bash shell with pipefail option
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Set the working directory
WORKDIR /

# Update and upgrade the system packages (Worker Template)
COPY setup.sh /
RUN chmod o+x /setup.sh 
RUN /setup.sh && rm /setup.sh

# Install Python dependencies (Worker Template)
RUN apt-get install python3-pip -y

COPY requirements.txt /
COPY requirements_2.txt /

RUN --mount=type=cache,target=/root/.cache/pip

RUN pip install --upgrade -r /requirements.txt --no-cache-dir 
RUN rm /requirements.txt

RUN pip install --upgrade -r /requirements_2.txt --no-cache-dir 
RUN rm /requirements_2.txt
RUN pip install --upgrade runpod --no-cache-dir 

COPY src/ /src
COPY handler.py /
COPY inference.py /
COPY utils.py /

CMD python3 -u handler.py
