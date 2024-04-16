FROM python:3.11.5-alpine

#RUN apk update && apk add python3-dev gcc libc-dev

COPY . .

# RUN \
#  apk add --no-cache postgresql-libs && \
#  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
#  pip install -r requirements.txt --no-cache-dir && \
#  apk --purge del .build-deps

RUN pip install --upgrade pip

RUN pip install -r requirements.txt 
# --no-cache-dir
# WORKDIR /backend/cyourself
WORKDIR /docker/backend
# CMD ["python", "backend/cyourself/manage.py", "runserver", "0:8000"]
# CMD ["gunicorn", "cyourself.wsgi:application", "--bind", "0.0.0.0:8000"]
# RUN gunicorn backend.cyourself.cyourself.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
# 
RUN chmod +x serverentrypoint.sh
RUN chmod +x worker-entrypoint.sh
