from .command import Command
from ..elements import Idle


class MoveCommand(Command):
    """Command used to move an Idle displayable element."""

    def __init__(self, element: Idle, speed: tuple[int, int], start: tuple[int, int],
                 destination: tuple[int, int], func):
        super().__init__(func)
        self.element = element
        self.to_pos = destination
        self.velocity = self.calculate_velocity(start, speed)

    def __repr__(self):
        return f"MoveCommand to {self.to_pos}"

    def calculate_velocity(self, pos: tuple[int, int], speed: tuple[int, int]) -> tuple[int, int]:
        """With pos -> to_pos, turns the speed into the appropriate velocity."""
        x = -speed[0] if pos[0] > self.to_pos[0] else speed[0]
        y = -speed[1] if pos[1] > self.to_pos[1] else speed[1]
        return x, y

    def reached_destination(self):
        """Zeroes out the appropriate velocity axis if the element reached the destination on that axis."""
        pos = self.element.get_position()
        if (self.velocity[0] < 0 and pos[0] <= self.to_pos[0]) or \
           (self.velocity[0] > 0 and pos[0] >= self.to_pos[0]):
            self.velocity = (0, self.velocity[1])
        if (self.velocity[1] < 0 and pos[1] <= self.to_pos[1]) or \
           (self.velocity[1] > 0 and pos[1] >= self.to_pos[1]):
            self.velocity = (self.velocity[0], 0)

    def move(self):
        """Moves the entity incrementally towards the destination."""
        self.element.add_position(self.velocity)
        self.reached_destination()
        if self.velocity == (0, 0):
            self.element.set_position(self.to_pos)
            self.stop()

    def update(self, dt: float):
        """Executing the command each update."""
        if self.done:
            return
        self.dt_runner.dt_update(dt, self.move)
