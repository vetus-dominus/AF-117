FROM python:3-alpine
RUN apk update && \
apk add python3-dev gcc libc-dev pkgconf mariadb-dev mariadb-connector-c-dev
RUN mkdir -p /var/django
ADD ./requirements.txt /var/django/
ADD ./backend /var/django/backend
ADD ./docker /var/django/docker
RUN chmod +x /var/django/docker/backend/server.sh
RUN chmod +x /var/django/docker/backend/worker.sh
WORKDIR /var/django
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt
