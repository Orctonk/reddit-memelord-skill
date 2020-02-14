from mycroft import MycroftSkill, intent_file_handler


class RedditMemelord(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('memelord.reddit.intent')
    def handle_memelord_reddit(self, message):
        self.speak_dialog('memelord.reddit')


def create_skill():
    return RedditMemelord()

