#!/bin/sh

set -a
source .env
set +a

if [ "$POSTGRES_ENGINE" = "django.db.backends.postgresql_psycopg2" ]; then
  echo "**Ожидание PostgreSQL...**"
  while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 0.1
  done
  echo "**PostgreSQL запущен**"
fi

echo "**Создаю миграции...**"
python manage.py makemigrations

echo "**Применяю миграции...**"
python manage.py migrate

echo "**Собираю статические файлы...**"
python manage.py collectstatic --no-input

exec "$@"
