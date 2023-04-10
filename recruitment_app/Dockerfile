FROM python:3.8

#Docker compose
ENV PYTHONUNBUFFERED=1

WORKDIR /recruitment-pipeline

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#Move to docker compose
# COPY . .

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]