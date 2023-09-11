web: uvicorn hngx_two.wsgi --log-file -
release: python manage.py migrate --noinput
release: python manage.py collectstatic --noinput
