class Rectangle:
    """A rectangle supporting basic collision detection."""

    def __init__(self, pos: tuple[float, float], width: int, height: int):
        self.pos = pos
        self.width, self.height = width, height

    def get_width(self) -> int:
        """Gets the width of the image."""
        return self.width

    def get_height(self) -> int:
        """Gets the height of the image."""
        return self.height

    def get_position(self) -> tuple[float, float]:
        """Gets the position of the rectangle."""
        return self.pos

    def set_position(self, pos: tuple[float, float]):
        """Sets the position of the rectangle."""
        self.pos = pos

    def add_position(self, pos: tuple[float, float]):
        """Adds to the position of the rectangle."""
        self.pos = (self.pos[0] + pos[0], self.pos[1] + pos[1])

    def collides_with_point(self, pos: tuple[float, float]) -> bool:
        """Checks if a point's position is within the rectangle."""
        return self.pos[0] <= pos[0] <= self.pos[0] + self.width and self.pos[1] <= pos[1] <= self.pos[1] + self.height
