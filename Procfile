web: gunicorn djangodrftodo.wsgi
release: python manage.py migrate --noinput
release: python manage.py test
release: python manage.py collectstatic --noinput