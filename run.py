#!.venv/bin/python
from app import app
app.run(host='0.0.0.0')  # Does __not__ run as a debug! For use with gunicorn

