# Base image
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

# Use bash shell with pipefail option
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Set the working directory
WORKDIR /

# Update and upgrade the system packages (Worker Template)
COPY builder/setup.sh /setup.sh
RUN chmod o+x /setup.sh 
RUN /setup.sh && rm /setup.sh


# Install Python dependencies (Worker Template)
RUN apt-get install python3-pip -y

COPY builder/requirements.txt /requirements.txt
COPY builder/requirements_2.txt /requirements_2.txt

RUN --mount=type=cache,target=/root/.cache/pip

RUN pip install --upgrade -r /requirements_2.txt --no-cache-dir 
RUN rm /requirements_2.txt

RUN pip install --upgrade -r /requirements.txt --no-cache-dir 
RUN rm /requirements.txt

COPY src/ /src
COPY handler.py /
COPY inference.py /

CMD python3 -u handler.py

# Need to install jupyter lab to make it work
# ENTRYPOINT ["jupyter", "lab","--ip=0.0.0.0","--allow-root"]
