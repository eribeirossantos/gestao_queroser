web: gunicorn core.wsgi:application --bind 0.0.0.0:$PORT --workers 2
release: python manage.py migrate && python init_db.py
