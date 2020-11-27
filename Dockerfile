FROM python:latest
RUN mkdir app
RUN mkdir /app/myapp
WORKDIR /app/
ADD app/ app/
RUN pip install -r /app/requirements.txt
# COPY . /app/myapp
# RUN pip install /app/myapp
# CMD flask run wookim_api:app

