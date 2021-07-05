"""OpenStreamDeck"""

from threading import Thread
from interfaces import Interface
import time

class OpenStreamDeck():
    
    def __init__(self, interface: Interface) -> None:
        self.interface = interface
        self.run_thread = Thread(target=self._run, args=())

    def start(self):
        self.run_thread.do_run = True
        self.run_thread.start()

    def _run(self):
        while getattr(self.run_thread, "do_run", True):
            data = self.interface.read()
            if data:
                print(data)
            time.sleep(0.1)