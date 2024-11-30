FROM python:3.11-alpine

WORKDIR /app

COPY requirements/prod.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT ["sh", "entrypoint.sh"]