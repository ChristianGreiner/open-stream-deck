"""A list of all devices"""
from abc import ABC, abstractmethod
from typing import List, Tuple
from actions import Action

class EventNotSupportedError(Exception):
    """Exception for not supporting the event"""


class Component(ABC):
    def __init__(self, slug: str, device_nr: str) -> None:
        super().__init__()
        self.device_nr = 0
        self.slug = None
        self.id = f"{slug}_{device_nr}"
        self.actions = {}

    def add_action(self, event: str, action: Action):
        self.actions[event].append(action)

    def set_actions(self, event: str, actions: List[Action]):
        self.actions[event].extend(actions)

    def trigger(self, event: str):
        for action in self.actions[event]:
            action.execute()

class Button(Component):
    def __init__(self, device_nr: str) -> None:
        super().__init__('BTN', device_nr)
        self.actions = {
            'push': [],
            'hold': []
        }

class RotaryEncoder(Component):
    def __init__(self, device_nr: str) -> None:
        super().__init__('ROTENC', device_nr)
        self.actions = {
            'rotate_left': [],
            'rotate_right': [],
        }

class Potentiometer(Component):
    def __init__(self, device_nr: str, min_value: int = 0, max_value: int = 1600) -> None:
        super().__init__('POT', device_nr)
        self.min_value = min_value
        self.max_value = max_value
        self.actions = {
            'changed': {},
        }