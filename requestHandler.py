from Jarvis import Jarvis
import os, requests, logging
from flask import Flask, request, json

app = Flask(__name__)
jarvis = Jarvis()
app.debug = True

@app.route('/', methods=['POST'])
def requestHandler():
    try:
        incoming = request.get_json(force=True)
        app.logger.debug(incoming)
        if incoming["name"] != "Jarvis":
            jarvis.ParseAndRespond(incoming)
    except:
        pass

    return ""