from mycroft import MycroftSkill, intent_file_handler
from .memelord import Memelord

class RedditMemelord(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.memelord = Memelord()

    @intent_file_handler('memelord.open.intent')
    def handle_memelord_open(self, message):
        if self.memelord.openWindow():
            self.speak_dialog('memelord.serve')
        else:
            self.speak_dialog('memelord.reopen')

    @intent_file_handler('memelord.close.intent')
    def handle_memelord_close(self, message):
        self.memelord.closeWindow()
        self.speak_dialog('memelord.close')

    @intent_file_handler('memelord.next.intent')
    def handle_memelord_next(self, message):
        if self.memelord.next():
            self.speak_dialog('memelord.serve')
        else:
            self.speak_dialog('memelord.last')
    
    @intent_file_handler('memelord.previous.intent')
    def handle_memelord_next(self, message):
        if self.memelord.next():
            self.speak_dialog('memelord.serve')
        else:
            self.speak_dialog('memelord.hottest')

def create_skill():
    return RedditMemelord()
