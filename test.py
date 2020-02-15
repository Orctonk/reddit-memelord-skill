from .memelord import Memelord

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