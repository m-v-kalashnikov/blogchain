#!/bin/sh

rm db.sqlite3
rm ./*/migrations/0*.py
python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input --clear
python manage.py createsuperuser --noinput
python manage.py create_auth_custom_fixtures
python manage.py create_blog_fixtures
python manage.py change_site_credentials
python manage.py runserver 0.0.0.0:8000