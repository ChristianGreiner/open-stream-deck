import time
import logging
from actions.media import VolumeUpAction, VolumeDownAction, SetVolumeAction
from interfaces import SerialInterface
from actions import OpenLinkAction

interface = SerialInterface('COM5')

def run():
    while True:
        data = interface.read()
        print(data)
        time.sleep(0.25)


def main():
    # setup loggin
    logging.info("OSD started.")
    print("Hello World!")
    link = OpenLinkAction("http://google.de")
    link.execute()
    run()


if __name__ == "__main__":
    main()
