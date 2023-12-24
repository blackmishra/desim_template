#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
pip install djangorestframework
# pip install redis
pip install yagmail
pip install psycopg2
pip install dj-database-url
pip install python-dotenv
pip install authlib
python manage.py collectstatic --no-input
python manage.py migrate