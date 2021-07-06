from actions.media import VolumeUpAction, VolumeDownAction, SetVolumeAction
from components import Button, RotaryEncoder
from actions import Action, WaitAction
from interfaces import SerialInterface
from actions import OpenLinkAction
from OpenStreamDeck import OpenStreamDeck
import jsonpickle
import os, sys

class SayHello(Action):
    def execute(self) -> None:
        print("hello")


oled_button_1 = Button(1)
oled_button_1.set_actions('push', [OpenLinkAction("http://google.de"), WaitAction(1), SayHello()])

volume_mixer = RotaryEncoder(1)
volume_mixer.set_actions('rotate_left', [VolumeDownAction()])
volume_mixer.set_actions('rotate_right', [VolumeUpAction()])

components = [oled_button_1, volume_mixer]

def main():
    try:
        interface = SerialInterface('COM4')
        osd = OpenStreamDeck(interface, components)
        print("OSD started.")
        osd.start()
        print("OSD stoped.")
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


if __name__ == "__main__":
    main()
