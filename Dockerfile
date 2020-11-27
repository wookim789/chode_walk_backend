FROM ubuntu:latest
MAINTAINER wookim "wookim789@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
# COPY requirements.txt /tmp
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ['router.py']
# COPY . /tmp/myapp
# RUN pip install /tmp/myapp
# EXPOSE 5000
# CMD flask run wookim_api:app