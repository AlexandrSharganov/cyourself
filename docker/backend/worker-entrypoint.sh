#!/bin/sh

until cd /backend/cyourself
do
    echo "Waiting for server volume..."
done

celery -A cyourself worker --loglevel DEBUG --concurrency 1 -E