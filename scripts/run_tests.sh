export ENV=test
export FLASK_APP=app/autoapp.py
export FLASK_ENV=test
export FLASK_DEBUG=True
export HOST=127.0.0.1
export PORT=5000
export PYTHONPATH=$(pwd)/app
pytest app/tests/
