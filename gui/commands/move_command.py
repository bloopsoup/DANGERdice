import pygame
from .command import Command
from ..elements import Idle


class MoveCommand(Command):
    """Command used to move an Idle displayable element."""

    def __init__(self, element: Idle, speed: tuple[float, float], start: tuple[float, float],
                 destination: tuple[float, float], func):
        super().__init__(func)
        self.element = element
        self.to_pos = pygame.Vector2(destination)
        self.velocity = self.calculate_velocity(pygame.Vector2(start), speed)

    def __repr__(self):
        return "MoveCommand to {0}".format(self.to_pos)

    def calculate_velocity(self, pos: pygame.Vector2, speed: tuple[float, float]) -> pygame.Vector2:
        """With pos -> to_pos, turns the speed into the appropriate velocity."""
        x = -speed[0] if pos.x > self.to_pos.x else speed[0]
        y = -speed[1] if pos.y > self.to_pos.y else speed[1]
        return pygame.Vector2((x, y))

    def reached_destination(self):
        """Zeroes out the appropriate velocity axis if the element reached the destination on that axis."""
        if (self.velocity.x < 0 and self.element.get_position().x <= self.to_pos.x) or \
           (self.velocity.x > 0 and self.element.get_position().x >= self.to_pos.x):
            self.velocity.update((0, self.velocity.y))
        if (self.velocity.y < 0 and self.element.get_position().y <= self.to_pos.y) or \
           (self.velocity.y > 0 and self.element.get_position().y >= self.to_pos.y):
            self.velocity.update((self.velocity.x, 0))

    def move(self):
        """Moves the entity incrementally towards the destination."""
        self.element.add_position(self.velocity)
        self.reached_destination()
        if self.velocity.x == 0 and self.velocity.y == 0:
            self.element.set_position(pygame.Vector2(self.to_pos))
            self.stop()

    def update(self, dt: float):
        """Executing the command each update."""
        if self.done:
            return
        self.dt_runner.dt_update(dt, self.move)
