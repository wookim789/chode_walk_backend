FROM python:3.7
COPY requirements.txt /tmp
RUN pip install -r requirements.txt
COPY . /tmp/myapp
RUN pip install /tmp/myapp
EXPOSE 5000
# CMD flask run wookim_api:app