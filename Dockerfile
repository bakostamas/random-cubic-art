FROM python:3.7-slim

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

EXPOSE 5055
CMD python app.py
