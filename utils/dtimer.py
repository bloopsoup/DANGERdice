import pygame


class DTimer:
    """Timer that relies on dt. Constructed with an event to signal when its timer reaches
       0. Must be activated manually and should be updated under a general update loop."""

    def __init__(self, event):
        self.event = event
        self.seconds = 0
        self.dt_time = 0
        self.loop = False
        self.active = False

    def activate(self, seconds: float, loop: bool = False):
        """Activates the timer by setting a time to decrement. Loop determines
           whether the timer stays active and resets its timer constantly."""
        self.seconds = seconds
        self.dt_time = seconds
        self.loop = loop
        self.active = True

    def deactivate(self):
        """Shut off looping."""
        self.loop = False

    def update(self, dt: float):
        """If timer is active, will decrement its dt_time by dt. It will also check
           whether enough time has passed in order to signal an event."""
        if not self.active:
            return

        self.dt_time -= dt
        if self.dt_time < 0:
            pygame.event.post(pygame.event.Event(self.event, {}))
            if self.loop:
                self.dt_time = self.seconds
            else:
                self.seconds = 0
                self.dt_time = 0
                self.active = False
