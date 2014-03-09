import os
from flask import Flask, request, json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def jarvis():
	try:
		returnString = "Testing: " + request.form["text"]
		print(returnString)
	except e:
		print(e)