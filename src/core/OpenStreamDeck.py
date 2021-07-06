"""OpenStreamDeck"""

from threading import Thread
from interfaces import Interface
import time

class OpenStreamDeck():
    
    def __init__(self, interface: Interface, components: list) -> None:
        self.interface = interface
        self.run_thread = Thread(target=self._run, args=(), daemon=True)
        self.components = {}
        for component in components:
            self.components[component.id] = component

    def _init_components(self, components: list):
        for component in components:
            self.components[component.id] = component

    def start(self):
        self.run_thread.do_run = True
        self.run_thread.start()

        while True:
            time.sleep(0.1)

    def _run(self):
        while getattr(self.run_thread, "do_run", True):
            data = self.interface.read()
            try:
                if data:
                    if data == 'exit':
                        self.run_thread.do_run = False
                        exit()
                    
                    command = data.split(' ')
                    if command[0] in self.components:
                        self.components[command[0]].trigger(event=command[1])
                    
                    print(data)
                time.sleep(0.1)
            except IndexError:
                print("Invalid command...")
