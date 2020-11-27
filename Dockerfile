FROM python:latest
RUN mkdir myapp/
ADD app/ myapp/
WORKDIR /myapp/
RUN pip install -r requirements.txt
# COPY . /app/myapp
# RUN pip install /app/myapp
EXPOSE 5000
CMD ["python", "app.py"]

