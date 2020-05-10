release: cd backend && python manage.py migrate 
web: cd backend && gunicorn backend.wsgi --workers=3 --threads=2 --log-file -
worker: cd backend && celery worker -A backend -l info

