import redditUtils as ru
import PySimpleGUI as sg
from PIL import Image
import threading
import os
import base64
from io import BytesIO

class Memelord():
    def __init__(self):
        self.windowOpened = False

    def openWindow(self) -> bool:
        if self.windowOpened:
            return False

        self.submissions = ru.getSubmissions()
        self.subidx = 0
        img = ru.getSubmissionImage(self.submissions[self.subidx])
        sh = sg.Window.get_screen_size()[1] - 200
        height = float(img.size[1])
        ratio = sh/height
        img = img.resize((int(img.size[0]*ratio),sh),Image.ANTIALIAS)
        buffered = BytesIO()
        img.save(buffered,format="PNG")
        img_str = base64.b64encode(buffered.getvalue())
        self.image = sg.Image(data=img_str)
        self.title = sg.Text(self.submissions[self.subidx].title,size=(50,2),font='Default 40',justification="center")
        self.layout =   [[sg.Col([  [self.title],
                                    [self.image]],
                                    element_justification='center'),
                        ]]
        self.window = sg.Window("Memelord",self.layout).Finalize()
        self.window.maximize()
        self.windowOpened = True
        return True

    def showSubmission(self, subidx: int):
        img = ru.getSubmissionImage(self.submissions[subidx])
        sh = self.window.size[1] - 200
        height = float(img.size[1])
        ratio = sh/height
        img = img.resize((int(img.size[0]*ratio),sh),Image.ANTIALIAS)
        buffered = BytesIO()
        img.save(buffered,format="PNG")
        img_str = base64.b64encode(buffered.getvalue())
        self.image.update(data=img_str)
        self.title.update(self.submissions[subidx].title)

    def next(self) -> bool:
        if not self.windowOpened:
            self.openWindow()
            return True

        self.window.Finalize()
        if self.subidx + 1 != len(self.submissions):
            self.subidx = self.subidx + 1
            self.showSubmission(self.subidx)
            return True
        else:
            return False

    def previous(self) -> bool:
        if not self.windowOpened:
            self.openWindow()
            return True

        self.window.Finalize()
        if self.subidx - 1 >= 0:
            self.subidx = self.subidx - 1
            self.showSubmission(self.subidx)
            return True
        else:
            return False

    def closeWindow(self):
        self.window.close

m = Memelord()
m.openWindow()

i = input("[N]ext, [P]revious or [Q]uit?")
while i.lower() != "q":
    if i.lower() == "n":
        m.next()
    elif i.lower() == "p":
        m.previous()
    i = input("[N]ext, [P]revious or [Q]uit?")

m.closeWindow()