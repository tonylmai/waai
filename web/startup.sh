!/usr/bin/sh

export PYTHONPATH=$PWD
# unicorn main:app --reload
FLASK_APP=waai.py flask run

