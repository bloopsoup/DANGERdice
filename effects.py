import pygame


# Base Effects
class BaseEffect:
    """Defines a base effect for visual use. It handles animation similar to Base but it is intended to be
       much simpler as these effects feature only one animation and is meant to be managed by an
       effect manager.
       files -- List of file names -- Pictures for the element.
       (x, y) -- Integers -- Starting location.
       ID -- Integer -- For identifying an effect when used with effect manager."""

    def __init__(self, files, ID, x, y):
        self.images = [pygame.image.load(file) for file in files]
        self.image = self.images[0]

        self.ID = ID

        self.x = x
        self.y = y

        # How quickly you want to go through frames
        self.frame = 0.07

        self.index = 0
        self.count = 0

        self.active = False

    def activate(self):
        """Turn on the animation and run."""
        self.active = True

    def run(self, dt):
        """Change the current image to simulate the animation. Runs once."""
        self.count += dt
        if self.count >= self.frame:
            self.count = 0
            self.index += 1
            if self.index > (len(self.images) - 1):
                self.index = 0
                self.active = False
                return
            self.image = self.images[self.index]

    def update(self, surface, dt):
        """Drawing the element."""
        # Draw the element if it's active
        if self.active:
            self.run(dt)
            surface.blit(self.image, (self.x, self.y))


# Effect Manager
class EffectManager:
    """Manages the effects."""

    def __init__(self):
        self.effect_queue = []

    def add_effect(self, file, ID, x, y):
        """Add a static background element."""
        self.effect_queue.append(BaseEffect(file, ID, x, y))

    def activate_effect(self, ID):
        """Activates an effect with the ID. Since effect queue is not changing, multiple effects
           can share the same ID."""
        for effect in self.effect_queue:
            if effect.ID == ID:
                effect.activate()

    def update(self, surface, dt):
        """Draw the full canvas."""
        for effect in self.effect_queue:
            effect.update(surface, dt)
