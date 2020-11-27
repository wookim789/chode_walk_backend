FROM python:latest
RUN mkdir myapp
ADD app/ myapp/app
WORKDIR /myapp/
RUN pip install -r myapp/app/requirements.txt
# COPY . /app/myapp
# RUN pip install /app/myapp
# CMD flask run wookim_api:app

