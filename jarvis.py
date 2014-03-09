import os
from flask import flask

app = Flask(__name__)

@app.route('/')
def jarvis():
	return "I'm Jarvis."