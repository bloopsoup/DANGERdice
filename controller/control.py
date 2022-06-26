import pygame


class Control:
    """Controls the game. Sets up settings and your starting state. Your controller will
       manage one state at a time where it will switch out states when prompted. This allows us to keep
       using one main game loop, greatly simplifying things. Courtesy of @metulburr's tutorial."""

    def __init__(self, start: str, states: dict, surface: pygame.Surface):
        self.states = states
        self.surface = surface

        self.DONE = False

        self.fps = 60
        self.clock = pygame.time.Clock()

        self.state_name = start
        self.state = self.states[self.state_name]
        self.state.startup()

    def to_state(self):
        """The game will move to another state."""
        # Leaving current state
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state.cleanup()

        # Moving onto the next
        self.state = self.states[self.state_name]
        self.state.startup()
        self.state.previous = previous

    def update(self, dt: float):
        """Moves to another state when prompted. Then, update your screen."""
        if self.state.quit:
            self.DONE = True
        elif self.state.done:
            self.to_state()
        self.state.update(self.surface, dt)

    def event_loop(self):
        """Processes events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.DONE = True
            self.state.handle_event(event)

    def main_loop(self):
        """Where the game takes place."""
        while not self.DONE:
            dt = self.clock.tick(self.fps) / 1000
            if dt >= 0.05:
                continue
            self.event_loop()
            self.update(dt)
            pygame.display.update()
