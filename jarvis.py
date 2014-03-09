import os, pprint, requests
from flask import Flask, request, json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def jarvis():
	try:
		pp = pprint.PrettyPrinter(indent=4)
		returnString = pp.pformat(request.form)
	except e:
		print(e)

def sendMessage(message):
	try:
		url = "https://api.groupme.com/v3/bots/post"
		r = requests.post(url, {"text" : message, "bot_id" : "0ef377109c8295124ee4af8978"})
	except e:
		print(e)