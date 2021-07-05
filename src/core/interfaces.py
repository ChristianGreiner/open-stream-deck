"""Interfaces"""
from abc import ABC, abstractmethod
import serial
from api import SerialAPI

class Interface(ABC):
    """Abstract class for interfaces"""

    @abstractmethod
    def read(self):
        """Reads the incoming data"""

class SerialInterface(Interface):
    """Implementation of a serial interface"""

    def __init__(self, port: str) -> None:
        self.api = SerialAPI()
        self.serialPort = serial.Serial(
            port=port, baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
        )
        self.buffer = bytearray()

    def _readline(self):
        i = self.buffer.find(b"\n")
        if i >= 0:
            r = self.buffer[:i+1]
            self.buffer = self.buffer[i+1:]
            return r
        while True:
            i = max(1, min(2048, self.serialPort.in_waiting))
            data = self.serialPort.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buffer + data[:i+1]
                self.buffer[0:] = data[i+1:]
                return r
            else:
                self.buffer.extend(data)

    def read(self):
        if self.serialPort.in_waiting > 0:
            serialString = self._readline()
            text = serialString.decode("Ascii").strip()
            value = self.api.read(text)
            return text