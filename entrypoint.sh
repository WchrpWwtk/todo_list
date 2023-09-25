#!/bin/sh

# wait for the database to become available
echo "Waiting for the database..."

python manage.py makemigrations
python manage.py migrate