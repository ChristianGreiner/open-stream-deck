
from typing import Tuple

class Page:
    def __init__(self, root: Page, size: Tuple[int, int], items: list) -> None:
        self.pages = []
        self.size = (3, 2)
        self.items = [[0 for x in range(self.size[0])] for y in range(self.size[1])] 

    def add_subpage(self, page: Page):
        page.root = self
        self.pages.append(page)




