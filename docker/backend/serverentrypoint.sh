#!/bin/sh

cd /backend/cyourself

python manage.py migrate
python manage.py createfixtures
python manage.py collectstatic --noinput

gunicorn cyourself.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4