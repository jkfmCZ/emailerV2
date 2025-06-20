# Dockerfile

FROM python:3.10-slim-bullseye


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 8069


CMD ["python", "manage.py", "runserver", "0.0.0.0:8069"]
