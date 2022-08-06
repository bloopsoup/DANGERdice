from collections import deque
from .command import Command


class CommandQueue:
    """Manager for executing bundles of commands sequentially."""

    def __init__(self):
        self.queue = deque(maxlen=128)

    def add(self, commands: list[Command]):
        """Append a set of commands to the queue."""
        assert len(commands), "commands cannot be empty"
        self.queue.append(commands)

    def clear(self):
        """Clears the command queue."""
        self.queue.clear()

    def finished_commands(self) -> bool:
        """Checks if the current set of commands are done."""
        return all([command.is_done() for command in self.queue[0]])

    def update(self, dt: float):
        """Processes the current set of commands and moves to the next set if all the commands are finished."""
        if not len(self.queue):
            return
        for command in self.queue[0]:
            if not command.is_done():
                command.update(dt)
        if self.finished_commands():
            self.queue.popleft()
