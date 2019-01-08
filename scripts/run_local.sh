export ENV=production
export FLASK_APP=app/autoapp.py
export FLASK_ENV=production
export HOST=0.0.0.0
export PORT=5000
gunicorn app.autoapp:APP -b ${HOST}:${PORT} --chdir app