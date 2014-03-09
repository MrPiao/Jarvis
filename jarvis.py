import os, requests, logging
from flask import Flask, request, json

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['POST'])
def jarvis():
	try:
		app.logger.debug(request.form)
		if request.form["name"] != "Jarvis":
			returnString = request.form["text"]
			sendMessage(returnString)
	except e:
		app.logger.debug(e)

def sendMessage(message):
	try:
		url = "https://api.groupme.com/v3/bots/post"
		r = requests.post(url, {"text" : message, "bot_id" : "0ef377109c8295124ee4af8978"})
	except e:
		app.logger.debug(e)