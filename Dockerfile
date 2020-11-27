FROM python:latest
ADD app/ .
WORKDIR /app/
RUN pip install -r app/requirements.txt
# COPY . /app/myapp
# RUN pip install /app/myapp
# CMD flask run wookim_api:app

