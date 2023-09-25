#!/bin/bash
set -e

echo "${0}: running migrations."
python wait_for_db.py
python manage.py makemigrations --merge
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000