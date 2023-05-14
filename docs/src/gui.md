<img src="../assets/icon.ico" height="100" align="right" />

# GUI

> [**Go Back**](../../README.md)

<br>

The `gui` folder implements all the UI and displayable elements that are seen in the game. These elements are made up 
of components implemented in `/core`.

# Elements

Anything you see in the game is an element. They are managed by the `Canvas`.

## `Displayable`

The base class for any displayable element. It is made up of a list of `AbstractImage`s that represent the element visually, 
a position, and `theme` which is used to customize the attributes of a particular element like color.

It contains abstract methods for handling input, updating its internal state, and drawing itself. All elements inherit from 
this class.

Here's an example of a background element.

```python
class StaticBG(Displayable):
    def __init__(self, images: list[AbstractImage], pos: tuple[int, int]):
        super().__init__(images, pos, {})

    def draw(self):
        self.images[0].blit(self.get_position())
```

## `Interactive`

The base class for any element you can interact with. It is a child class of `Displayable`. The only additional parameter it 
needs is `on_event`, a callback function that is triggered by user input.

Here's an example of a button element.

```python
class Button(Interactive):
    def __init__(self, images: list[AbstractImage], pos: tuple[int, int], 
                       theme: dict, on_event):
        super().__init__(images, pos, theme, on_event)
        self.clicked, self.hovered = False, False

    def current_picture_index(self) -> int:
        if self.clicked: return 2
        elif self.hovered: return 1
        else: return 0

    def handle_event(self, event: Event):
        if not event.is_mouse_event(): return
        if self.is_mouse_over_element(event):
            self.hovered = True
            if event.get_type() == EventType.MOUSE_DOWN and self.on_event:
                SOUND_PLAYER.play_sfx(self.theme["sfx"])
                self.clicked = True
                self.on_event()
            else: self.clicked = False
        else: self.hovered = False

    def draw(self):
        self.images[self.current_picture_index()].blit(self.get_position())
        self.draw_border()
```

# Canvas

The `Canvas` is a list of GUI elements. It display elements in a FIFO order, meaning the elements that are first will be displayed 
in the bottom layer.

The list itself consists of tuples of `(Displayable, str)` where `Displayable` is the element itself and `str` is the group the element 
is a part of. This provides ease in deleting lots of elements at once (such as clearing a screen).

Every game loop, the canvas has to pass inputs, update state, and draw each element.

# Commands

Commands are actions that execute over a period of time via updates. These actions typically involve modifying GUI components, 
but can also be used to call other types of functions after a certain period of time.

## `Command`
Actions that execute over a period of time. They have a callback function (called when the command is done) and a flag 
called `done`.

There are two primary types of commands.

- `MoveCommand`: A command that controls an `Idle` element, moving it at a certain speed from `start` to `dest`. 
Primarily used for setting up animations and cutscenes.
- `TimerCommand`: A command that runs `func` after a certain number of `frames` has passed. 
Typically used for setting up delays or timing for animations.

## `CommandQueue`

Processes batches of queued up commands in FIFO fashion. When adding to the queue, you add batches of commands to run at the same 
time rather than one command at a time.

Typically, a queue looks like this.
```python
[[TimerCommand, MoveCommand], [TimerCommand], ...]
```

The queue will process a batch of commands until all commands in that batch indicate their `done` flag is `True`. At this point it 
will run the next batch of commands.

The `AnimationHandler` can be seen as presets for batches of commands to feed into the queue. This is used to store frequently seen animations.

# Utils

A collection of objects used in constructing elements.

- `DeltaTimerRunner`: Runs functions periodically after enough time has passed on every update.
- `DialogueData`: Keeps track of a sequence of texts and images. Displays text one character at time per update to simulate a typing effect. 
Used to implement the `DialogueBox` which is just a graphical representation.
- `IndexCycler`: Essentially a 2D list of numbers. Loops through a particular row of numbers when enough time has passed. If it reaches the end of a
row, it loops through another row chosen randomly. Used to implement idle animations, as each row represents a particular animation to play.
