from GroupMeInterface import GroupMeInterface

class Jarvis:
    def __init__(self):
        self.talkingTo = None

    def ParseAndRespond(self, incoming):
        incoming = incoming.lower()
        body = incoming["text"]
        speaker = incoming["name"]

        if body == "jarvis":
            self.Acknowledge(speaker)

        if speaker == self.talkingTo:
            if body == "thanks" or body == "thx":
                self.EndConversation()

    def Acknowledge(self, name):
        self.talkingTo = name
        GroupMeInterface.SendMessage("How can I help you, " + self.talkingTo + "?")

    def EndConversation(self):
        self.talkingTo = None
        GroupMeInterface.SendMessage("You're welcome")

    def Speak(self, text):
        GroupMeInterface.SendMessage(text)