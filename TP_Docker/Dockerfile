FROM ubuntu:latest

WORKDIR usr/src/app

COPY . .

RUN apt-get update && apt-get install -y \
vim \
python3 \
python3-pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD python3 app/app.py

