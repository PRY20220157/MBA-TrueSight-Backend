web: gunicorn todolistapi.wsgi
release: python manage.py makemigrations --nopinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput