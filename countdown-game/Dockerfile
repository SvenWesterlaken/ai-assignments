FROM python:3

RUN cd ~

RUN apt-get update -yq \
    && apt-get install curl gnupg -yq \
    && curl -sL https://deb.nodesource.com/setup_10.x | bash \
    && apt-get install nodejs -yq

RUN npm i -g nodemon

RUN mkdir -p /usr/src/app

RUN cd /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["nodemon", "-L", "main.py", "||", "exit", "1"]
