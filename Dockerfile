FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt update
RUN apt install -y postgresql-client
COPY . /code/
CMD ["bash", "-c", "python manage.py makemigrations && python manage.py makemigrations airport_app && python manage.py makemigrations airline_app && python manage.py migrate && PGPASSWORD=YtUlP7zzTz0Q5w0aqx4yZa5vHxmgZfiB psql -h dpg-cq5nn9o8fa8c7389rff0-a.frankfurt-postgres.render.com -U user db_2yi9 -a -f database_init.sql && python manage.py makemigrations airline_app && python manage.py runserver 0.0.0.0:8000"]
