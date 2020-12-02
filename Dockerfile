FROM python:latest
RUN mkdir myapp/
ADD app/ myapp/
WORKDIR /myapp/
RUN pip install -r requirements.txt
EXPOSE 8000
# CMD ["python", "app.py"]

