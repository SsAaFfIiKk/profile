FROM python:3.8

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

WORKDIR /app
COPY . .
# COPY 'video_fragments/*/*' /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python3 server.py