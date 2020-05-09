release: cd backend && python manage.py migrate 
web: cd backend && gunicorn backend.wsgi --works=3 --threads=2 --log-file -
