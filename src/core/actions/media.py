from actions import Action
from pynput.keyboard import Key, Controller
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from const import VOLUME_SCALE

class VolumeUpAction(Action):
    def __init__(self) -> None:
        super().__init__()
        self.keyboard = Controller()

    def execute(self) -> None:
        self.keyboard.press(Key.media_volume_up)


class VolumeDownAction(Action):
    def __init__(self) -> None:
        super().__init__()
        self.keyboard = Controller()

    def execute(self) -> None:
        self.keyboard.press(Key.media_volume_down)


class SetVolumeAction(Action):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def execute(self) -> None:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        currentVolumeDb = volume.GetMasterVolumeLevel()
        print(currentVolumeDb)
        volume.SetMasterVolumeLevel(scale.get(VOLUME_SCALE + "%"), None)
