FROM python:latest
RUN mkdir myapp/app/
ADD app/ myapp/app/
WORKDIR /myapp/app/
RUN pip install -r myapp/app/requirements.txt
# COPY . /app/myapp
# RUN pip install /app/myapp
# CMD flask run wookim_api:app

