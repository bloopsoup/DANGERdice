import pygame
from utils.index_cycler import IndexCycler


class BaseEntity:
    """A base entity for gameplay use. Can move via animation or move to a location directly
       via commands. If not moving, performs an idling animation."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        self.images = images
        self.image = self.images[0]

        self.pos = pygame.Vector2(pos)
        self.from_pos = pygame.Vector2(pos)
        self.to_pos = None
        self.speed = pygame.Vector2([0, 0])

        # A reference rectangle of the entity
        self.reference = self.images[0].get_rect()
        self.reference.move_ip(self.pos)

        # Animations
        self.idle = True
        self.idle_handler = IndexCycler([], 0)  # Dummy for this base class
        self.move_frames = 0.01
        self.move_count = 0

    def set_idle(self, on: bool):
        """Indicates whether the entity is idle or not."""
        self.idle = on

    def command_move(self, speed: tuple[float, float], destination: tuple[float, float]):
        """Move the entity with a specified velocity to some destination."""
        self.stop_move()
        self.to_pos = pygame.Vector2(destination)
        self.speed = pygame.Vector2(speed)
        self.set_idle(False)

    def stop_move(self):
        """Used to stop the entity and interrupt ongoing move commands."""
        self.from_pos = pygame.Vector2(self.pos)
        self.to_pos = None
        self.speed = pygame.Vector2([0, 0])
        self.set_idle(True)
        self.move_count = 0

    def direct_move(self, destination: tuple[float, float]):
        """Directly moves the entity to the destination."""
        self.pos = pygame.Vector2(destination)
        self.from_pos = pygame.Vector2(destination)

    def move_x(self):
        """Helper for MOVE, handling the x-axis."""
        if self.speed.x <= 0:
            return

        if self.from_pos.x < self.to_pos.x:
            if self.pos.x < self.to_pos.x:
                self.pos.x += self.speed.x
            else:
                self.speed.x = 0
        elif self.from_pos.x > self.to_pos.x:
            if self.pos.x > self.to_pos.x:
                self.pos.x -= self.speed.x
            else:
                self.speed.x = 0

    def move_y(self):
        """Helper for MOVE, handling the y-axis."""
        if self.speed.y <= 0:
            return

        if self.from_pos.y < self.to_pos.y:
            if self.pos.y < self.to_pos.y:
                self.pos.y += self.speed.y
            else:
                self.speed.y = 0
        elif self.from_pos.y > self.to_pos.y:
            if self.pos.y > self.to_pos.y:
                self.pos.y -= self.speed.y
            else:
                self.speed.y = 0

    def move(self, dt: float):
        """Moves the entity incrementally to the destination and then disables movement when done."""
        if self.speed.x == 0 and self.speed.y == 0:
            return

        # Wait for dt
        self.move_count += dt
        if self.move_count < self.move_frames:
            return
        self.move_count = 0

        # Movement
        self.move_x()
        self.move_y()

        # Cancel residue movement when done
        if self.speed.x == 0 and self.speed.y == 0:
            self.pos = pygame.Vector2(self.to_pos)
            self.stop_move()

    def idle_animate(self, dt: float):
        """Change the current image quickly to simulate an idle animation."""
        if not self.idle:
            return
        result = self.idle_handler.update(dt)
        if result != -1:
            self.image = self.images[result]

    def update(self, dt: float):
        """Updating the entity."""
        self.move(dt)
        self.reference.move_ip(self.pos)
        self.idle_animate(dt)

    def draw(self, surface: pygame.Surface):
        """Drawing the entity."""
        surface.blit(self.image, (self.pos.x, self.pos.y))
