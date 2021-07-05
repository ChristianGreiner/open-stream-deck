"""Serial API"""
from abc import ABC, abstractmethod

class API(ABC):
    """Abstract class for an api"""
    
    @abstractmethod
    def parse(self):
        """Reads the incoming data"""


class SerialAPI(API):
    """Implementation of a serial interface api"""

    def read(self, data):
        # parse button
        # Example BTN 1
        if data.startswith('BTN'):
            btn_nr = data.split(' ')[1]
            if btn_nr.isnumeric():
                return True


