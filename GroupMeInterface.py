import requests

class GroupMeInterface:
    @staticmethod
    def SendMessage(message):
        url = "https://api.groupme.com/v3/bots/post"
        r = requests.post(url, {"text" : message, "bot_id" : "0ef377109c8295124ee4af8978"})