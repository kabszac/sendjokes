web: gunicorn sendjoke.wsgi --log-file -
celeryworker2: celery -A sendjoke.celery worker & celery -A sendjoke beat -l INFO & wait -n
