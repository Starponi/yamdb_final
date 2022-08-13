FROM python:3.7-slim

WORKDIR /app

COPY ./api_yamdb .

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]