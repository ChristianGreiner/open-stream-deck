import logging
from actions.media import VolumeUpAction, VolumeDownAction, SetVolumeAction
from components import Button
from actions import WaitAction
from interfaces import SerialInterface
from actions import OpenLinkAction
from OpenStreamDeck import OpenStreamDeck
import jsonpickle



btn = Button(1)
#btn.set_actions('push', [OpenLinkAction("http://google.de"), WaitAction(1), OpenLinkAction("http://google.de")])
print(btn.actions)
btn.push()
print(btn.id)


def main():
    #interface = SerialInterface('COM1')

    #osd = OpenStreamDeck(interface)

    #logging.info("OSD started.")
    """
    data = {
        "button1": [
            OpenLinkAction("https://google.de")
        ]
    }

    js = jsonpickle.encode(data)
    print(js)
    obj = jsonpickle.decode(js)
    obj["button1"][0].execute() 
    """
    #osd.start()
    


if __name__ == "__main__":
    main()
