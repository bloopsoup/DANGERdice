from .command_queue import CommandQueue
from .timer_command import TimerCommand
from .move_command import MoveCommand
from ..elements import Idle


class AnimationHandler:
    """Handles animations between sets of Idle elements and adds it to a command_queue."""

    def __init__(self, a: Idle, a_start: tuple[float, float], b: Idle, b_start: tuple[float, float],
                 queue: CommandQueue):
        self.a, self.a_start = a, a_start
        self.b, self.b_start = b, b_start
        self.queue = queue

    def to_start(self, hook):
        """Adds a command to the queue where both elements go to their starting positions."""
        self.queue.add([MoveCommand(self.a, (10, 0), (self.a_start[0] - 300, self.a_start[1]), self.a_start, None),
                        MoveCommand(self.b, (10, 0), (self.b_start[0] + 300, self.b_start[1]), self.b_start, None)])
        self.queue.add([TimerCommand(0.1, hook)])

    def scavenge(self, a_run: bool, hook):
        """Adds a command where one element rises up while the other element runs to its position."""
        run, rise = self.a if a_run else self.b, self.b if a_run else self.a
        run_start, rise_start = self.a_start if a_run else self.b_start, self.b_start if a_run else self.a_start
        self.queue.add([MoveCommand(rise, (0, 10), rise_start, (rise_start[0], rise_start[1] - 600), None)])
        self.queue.add([MoveCommand(run, (6, 0), run_start, (rise_start[0], run_start[1]), None)])
        self.queue.add([TimerCommand(0.5, hook)])

    def rush(self, a_rush: bool, hooks: list):
        """Adds a rush animation to queue. If a_rush is True, A will be charging.
           Use hooks to have certain functions called during the sequence."""
        assert len(hooks) == 3, "there must be three hooks"

        src, dest = self.a if a_rush else self.b, self.b if a_rush else self.a
        src_start, dest_start = self.a_start if a_rush else self.b_start, self.b_start if a_rush else self.a_start
        side = 1 if a_rush else -1
        backup, contact = src_start[0] - (side * 60), dest_start[0] - (side * self.a.get_width())
        recoil = dest_start[0] + (side * 100)

        self.queue.add([MoveCommand(src, (3, 0), src_start, (backup, src_start[1]), hooks[0])])
        self.queue.add([MoveCommand(src, (15, 0), (backup, src_start[1]), (contact, src_start[1]), hooks[1])])
        self.queue.add([TimerCommand(0.025, None)])
        self.queue.add([MoveCommand(dest, (12, 0), dest_start, (recoil, dest_start[1]), None)])
        self.queue.add([TimerCommand(0.5, None)])
        self.queue.add([MoveCommand(src, (15, 0), (contact, src_start[1]), src_start, None),
                        MoveCommand(dest, (6, 0), (recoil, dest_start[1]), dest_start, None)])
        self.queue.add([TimerCommand(0.2, hooks[2])])
