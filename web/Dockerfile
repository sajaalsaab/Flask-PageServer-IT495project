# see https://hub.docker.com/search for more base images.
FROM python:3.9
LABEL maintainer="SajaSaab <411201865@qu.edu.sa>"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["app.py"]
