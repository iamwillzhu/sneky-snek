FROM python:3.8-alpine

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8080
COPY . .
CMD ["python3", "server.py"]
