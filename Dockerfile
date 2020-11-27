FROM python:lastest
RUN mkdir app
WORKDIR /app/
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app/myapp
RUN pip install /app/myapp
# CMD flask run wookim_api:app