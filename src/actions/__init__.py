from abc import ABC, abstractmethod
import webbrowser
import time

class Action(ABC):
    """Abstract class for Actions"""

    @abstractmethod
    def execute() -> None:
        """Executes the Action"""


class WaitAction(Action):
    """Action that waits a given time"""

    def __init__(self, duration: str) -> None:
        super().__init__()
        self.duration = duration

    def execute(self) -> None:
        time.sleep(self.duration)


class OpenLinkAction(Action):
    """Action that open links in the webbrowser"""

    def __init__(self, link: str) -> None:
        super().__init__()
        self.link = link

    def execute(self) -> None:
        webbrowser.open(self.link)

