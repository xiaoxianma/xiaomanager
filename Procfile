release: cd backend && python manage.py migrate && cd ../frontend && yarn build
web: cd backend && gunicorn backend.wsgi --log-file -
