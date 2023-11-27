#!/bin/sh

until cd /var/django/backend
do
    echo "Waiting for server volume..."
done

celery -A backend worker --loglevel=info --concurrency 1 -E
