FROM python:3.10

RUN apt-get update \
    && apt-get install -y --no-install-recommends

COPY requirements.txt /home
WORKDIR /home
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["tail", "-f", "/dev/null"]
