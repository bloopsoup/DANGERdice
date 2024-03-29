from .elements import Displayable
from src.core import Event


class Canvas:
    """A container object for displayable elements."""

    def __init__(self):
        self.element_queue: list[tuple[Displayable, str]] = []

    def add_element(self, element: Displayable, group_ID: str):
        """Adds (element, group_ID) to the queue."""
        self.element_queue.append((element, group_ID))

    def insert_element(self, element: Displayable, group_ID: str, i: int):
        """Inserts (element, group_ID) to the queue at the ith spot."""
        self.element_queue.insert(i, (element, group_ID))

    def group_exists(self, group_ID: str) -> bool:
        """Checks if tuple(s) with group_ID exists."""
        return any([data[1] == group_ID for data in self.element_queue])

    def get_group(self, group_ID: str) -> list[Displayable]:
        """Returns a list of elements with group_ID."""
        return [data[0] for data in self.element_queue if data[1] == group_ID]

    def delete_group(self, group_ID: str):
        """Deletes all tuple(s) with group_ID."""
        self.element_queue = [data for data in self.element_queue if data[1] != group_ID]

    def delete_all(self):
        """Deletes all elements from the canvas."""
        self.element_queue.clear()

    def handle_event(self, event: Event):
        """Passes events into each element."""
        for data in self.element_queue:
            data[0].handle_event(event)

    def update(self, dt: float):
        """Updates each element."""
        for data in self.element_queue:
            data[0].update(dt)

    def draw(self):
        """Displays each element (first is farthest back)."""
        for data in self.element_queue:
            data[0].draw()
