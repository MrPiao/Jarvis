import os, requests, logging
from flask import Flask, request, json

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['POST'])
def jarvis():
	incoming = request.get_json(force=True)
	app.logger.debug(incoming)
	if incoming["name"] != "Jarvis":
		returnString = incoming["text"]
		sendMessage(returnString)

def sendMessage(message):
	url = "https://api.groupme.com/v3/bots/post"
	r = requests.post(url, {"text" : message, "bot_id" : "0ef377109c8295124ee4af8978"})