FROM python:3.11-slim

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

EXPOSE 5055
CMD gunicorn -w 4 --bind 0.0.0.0:5055 'app:app'
