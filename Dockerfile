FROM python:3.7
COPY requirements.txt /tmp
RUN pip install -r requirements.txt
COPY . /tml/myapp
RUN pip install /tmp/myapp
# CMD flask run wookim_api:app