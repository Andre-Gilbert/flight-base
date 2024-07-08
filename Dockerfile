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
CMD ["bash", "-c", "python manage.py makemigrations && python manage.py makemigrations airport_app && python manage.py makemigrations airline_app && python manage.py migrate && python manage.py fill_db && python manage.py makemigrations airline_app && python manage.py runserver 0.0.0.0:8000"]
