import pygame


# CANVAS ELEMENTS
class CanvasElement:
    """An element being placed into the canvas.
       file -- Image File -- The image to load.
       ID -- Integer -- The ID of the Canvas element for deletion."""

    def __init__(self, file, ID):
        self.image = pygame.Surface.convert_alpha(pygame.image.load(file))
        self.ID = ID

    def update(self, surface, dt):
        """Displays the element."""
        pass


class StaticElement(CanvasElement):
    """Literally just a static image."""

    def __init__(self, file, ID, x, y):
        super().__init__(file, ID)

        self.x = x
        self.y = y

    def update(self, surface, dt):
        surface.blit(self.image, (self.x, self.y))


class MovingBG(CanvasElement):
    """A moving background object. Loads an image (designed to be bigger than the surface) and moves the image
       in a cardinal direction with a speed. This was meant to be simpler to use than MovingElement.
       speed -- Integer -- The speed of the background.
       up -- Boolean -- Does it go vertically or horizontally?
       backwards -- Boolean -- Does it go backwards or not?
       (width, height) -- Integers -- Dimensions of the surface."""

    def __init__(self, file, ID, speed, up, backwards, width, height):
        super().__init__(file, ID)

        self.speed = speed
        self.up = up
        self.backwards = backwards

        self.width = width
        self.height = height

        self.count = 0
        self.frames = 0.01

        # Determine where to start the image
        self.x = 0
        self.y = 0
        if self.up:
            if self.backwards:
                self.y = self.height - self.image.get_height()
        else:
            if self.backwards:
                self.x = self.width - self.image.get_width()

    def move(self, dt):
        """Moves the background according to the chosen direction. If it strays too far, reset it back
        to its original position."""

        # Wait for dt
        self.count += dt
        if self.count < self.frames:
            return
        self.count = 0

        if self.up:
            if self.backwards:
                self.y += self.speed
                if self.y > 2 * self.height - self.image.get_height():
                    self.y = self.height - self.image.get_height()
            else:
                self.y -= self.speed
                if self.y < self.height - self.image.get_height():
                    self.y = 0
        else:
            if self.backwards:
                self.x += self.speed
                if self.x > 2 * self.width - self.image.get_width():
                    self.x = self.width - self.image.get_width()
            else:
                self.x -= self.speed
                if self.x < self.width - self.image.get_width():
                    self.x = 0

    def update(self, surface, dt):
        self.move(dt)
        surface.blit(self.image, (self.x, self.y))


# CANVAS
class Canvas:
    """Canvas is a container object for background elements, moving or not. The only thing it keeps track of is
       an image queue and moving image queue.
       Note that the FIRST added image will be the FARTHEST BACK.
       The LAST added image will be the FRONT of the canvas."""

    def __init__(self):
        self.image_queue = []

    def add_static_element(self, file, ID, x, y):
        """Add a static background element."""
        self.image_queue.append(StaticElement(file, ID, x, y))

    def add_moving_bg(self, file, ID, speed, up, backwards, width, height):
        """Add a moving background element."""
        self.image_queue.append(MovingBG(file, ID, speed, up, backwards, width, height))

    def check_id(self, ID):
        """Checks if an element exists with that ID."""
        return any([element.ID == ID for element in self.image_queue])

    def delete_element(self, ID):
        """Deletes an element from the canvas with ID. Only one element must have that ID."""
        for i in range(len(self.image_queue)):
            if self.image_queue[i].ID == ID:
                self.image_queue.pop(i)
                break

    def update(self, surface, dt):
        """Draw the full canvas."""
        for image in self.image_queue:
            image.update(surface, dt)
