import os, pprint
from flask import Flask, request, json
from http.client import *

app = Flask(__name__)

@app.route('/', methods=['POST'])
def jarvis():
	try:
		pp = pprint.PrettyPrinter(indent=4)
		returnString = pp.pformat(request.form)
		sendMessage(returnString)
	except e:
		print(e)

def sendMessage(message):
	try:
		conn = HTTPSConnection("")
		body = {
			"bot_id": "0ef377109c8295124ee4af8978",
			"text": message
		}
		conn.request("POST", "https://api.groupme.com/v3/bots/post", body)
	except e:
		print(e)