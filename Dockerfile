FROM python:3.13-alpine

WORKDIR /app

COPY .  .

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "80" ]

#! docker run -d -p 127.0.0.1:8000:8000 --name my-fastapi-container app_1