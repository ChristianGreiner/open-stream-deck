"""Interfaces"""
import serial
from abc import ABC, abstractmethod

class Interface(ABC):
    """Abstract class for interfaces"""
    @abstractmethod
    def read(self):
        """Reads the incoming data"""

class SerialInterface(Interface):
    """Implementation of a serial interface"""

    def __init__(self, port: str) -> None:
        self.serialPort = serial.Serial(
            port=port, baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
        )

    def read(self):
        if self.serialPort.in_waiting > 0:
            serialString = self.serialPort.readline()
            text = serialString.decode("Ascii").strip()
            return text