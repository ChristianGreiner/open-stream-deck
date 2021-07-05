"""A list of all devices"""
from abc import ABC, abstractmethod
from typing import List

from actions import Action

class EventNotSupportedError(Exception):
    """Exception for not supporting the event"""


class Component(ABC):
    def __init__(self, slug: str, device_nr: str) -> None:
        super().__init__()
        self.device_nr = 0
        self.slug = None
        self.id = f"{slug}_{device_nr}"
        self.actions = {
            'push': [],
            'rotate': [],
        }

    def add_action(self, event: str, action: Action):
        self.actions[event].append(action)

    def set_actions(self, event: str, actions: List[Action]):
        self.actions[event].extend(actions)

    @abstractmethod
    def push(self):
        """When the component is pushed"""
        raise EventNotSupportedError()

    @abstractmethod
    def rotate(self):
        """When the component is rotated"""
        raise EventNotSupportedError()

class Button(Component):
    def __init__(self, device_nr: str) -> None:
        super().__init__('BTN', device_nr)

    def push(self):
        """Reads the incoming data"""
        for action in self.actions['push']:
            action.execute()
            
    def rotate(self):
        """When the component is rotated"""
        raise EventNotSupportedError()


class RotaryEncoder(Component):
    def __init__(self, device_nr: str) -> None:
        super().__init__('ROTENC', device_nr)

    def push(self):
        """Reads the incoming data"""
        raise NotImplementedError()

    def rotate(self):
        """When the component is rotated"""
        raise NotImplementedError()


class PressableRotaryEncoder(RotaryEncoder):
    def __init__(self, device_nr: str) -> None:
        super().__init__(device_nr)

    def push(self):
        """Reads the incoming data"""
        raise NotImplementedError()

    def rotate(self):
        """When the component is rotated"""
        raise NotImplementedError()