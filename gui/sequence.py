self.move_frames = 0.01
        self.move_count = 0

self.from_pos = pygame.Vector2(pos)
        self.to_pos = None
        self.speed = pygame.Vector2([0, 0])


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


def rush(self, sequence, img, x_speed, right=False, mode=None):
    """Animates the rush animation for a character.
       1. Character moves backwards.
       2. Character rushes to the nearest enemy character.
       3. Character returns to original position.
       Note that mode can be either a target sprite or an og_x."""
    self.status(False)
    self.image = self.images[img]

    # Backing Up
    if sequence == 3:
        if right:
            self.command_move(x_speed, 0, int((self.x - self.image.get_width()) / 2), self.y)
        else:
            self.command_move(x_speed, 0, self.x + int((self.image.get_width()) / 2), self.y)
    # Charging towards the target sprite (but not intersecting it)
    elif sequence == 2:
        if right:
            self.command_move(x_speed, 0, mode.x - self.image.get_width(), self.y)
        else:
            self.command_move(x_speed, 0, mode.x + mode.image.get_width(), self.y)

    # Returning to original position
    else:
        self.command_move(x_speed, 0, mode, self.y)