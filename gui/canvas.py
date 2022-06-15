import pygame


class Canvas:
    """A container object for displayable elements."""

    def __init__(self):
        # A list of tuples (elements, group_ID)
        self.element_queue = []

    def add_element(self, element, group_ID: int):
        """Adds (elements, group_ID) to the queue."""
        self.element_queue.append((element, group_ID))

    def group_exists(self, group_ID: int) -> bool:
        """Checks if tuple(s) with group_ID exists."""
        return any([data[1] == group_ID for data in self.element_queue])

    def delete_group(self, group_ID: int):
        """Deletes all tuple(s) with group_ID."""
        self.element_queue = [data for data in self.element_queue if data[1] != group_ID]

    def handle_event(self, event):
        """Passes events into each element."""
        for data in self.element_queue:
            data[0].handle_event(event)

    def update(self, dt: float):
        """Updates each element."""
        for data in self.element_queue:
            data[0].update(dt)

    def draw(self, surface: pygame.Surface):
        """Displays each element onto surface (first is farthest back)."""
        for data in self.element_queue:
            data[0].draw(surface)
