<img src="../assets/icon.ico" height="100" align="right" />

# Core

> [**Go Back**](../../README.md)

<br>

The `core` folder implements low-level features that are crucial to running a game.

- Controlling the flow of the entire application.
- Handling user I/O where inputs are treated as events.
- Rendering images and text to the screen (with the help of libraries like `pygame`).
- Having useful data structures to easily manipulate images or positions.

From a higher level overview, the game runs as a state machine which runs on a variable delta-time.
States contain objects and other data that the player interacts with.

# Components

Interfaces for primitive game objects. We use libraries such as `pygame` or `pyglet` to implement them.
All UI and game objects such as player characters are made of these things. For example, a dialogue box
is made of a `AbstractImage` (for the box itself) and `AbstractLabel` (for the text).

**The purpose of this is to keep the game engine library-agnostic.**
**Any library can be used as long as it can implement the following components.**

## `AbstractImage`

An image that is displayed on the game screen. 

It is made up of the image (type depends on library), height, and width. Implementation is straight-forward 
as a library only needs to implement the `blit` and `blit_border` drawing methods.

Here's a `pygame` implementation. Notice how `pygame` uses `Surface` to represent images and we use its
corresponding `blit` method to draw it.

```python
import pygame
from .constants import surface
from ..components import AbstractImage

class Image(AbstractImage):
    def __init__(self, image: pygame.Surface):
        super().__init__(image)
        self.width, self.height = self.image.get_width(), self.image.get_height()

    def blit_border(self, pos: tuple[int, int], color: tuple[int, int, int], size: int):
        rect = self.image.get_rect()
        rect.update(pos, (self.width, self.height))
        pygame.draw.rect(surface, color, rect, size)

    def blit(self, pos: tuple[int, int]):
        surface.blit(self.image, pos)
```

## `AbstractLabel`

Text that is displayed on the game screen.

It is made up of the text (a string that will be displayed), font, and color. The library must implement
the `blit` drawing method, which typically involves rendering the text through a font and displaying it.

Here's a `pygame` implementation. Note that `loaded_fonts` is a mapping between `str` to a `pygame` font object.

```python
from .constants import loaded_fonts, surface
from ..components import AbstractLabel

class Label(AbstractLabel):
    def __init__(self, text: str, font: str, color: tuple[int, int, int]):
        assert font in loaded_fonts, f"{font} is not a valid font"
        super().__init__(text, font, color)
        self.rendered_text = loaded_fonts[font].render(text, True, color)
        self.width, self.height = self.rendered_text.get_width(), self.rendered_text.get_height()

    def blit(self, pos: tuple[int, int]):
        surface.blit(self.rendered_text, pos)

# EXAMPLE
label = Label("Hello World", "calibri", [100, 100, 100])
```

## `AbstractSoundPlayer`

A jukebox. It contains a collection of songs that can be played or muted when needed.
Most methods need to be implemented as each library has their own implementation in deal with sounds.

## `AbstractSpritesheet`

A giant `AbstractImage` that is a grid of smaller `AbstractImages`. Commonly used for
storing animations or related images for an element like a button.

The library must implement the `load_image` method, which loads a specific subimage from a spritesheet.

Here's a `pygame` implementation. Notice the `pygame` specific code in getting a region of the spritesheet
to output.

```python
import pygame
from .image import Image
from ..components import AbstractImage, AbstractSpritesheet

class Spritesheet(AbstractSpritesheet):
    def __init__(self, spritesheet: pygame.Surface, height: int, width: int, rows: int, cols: int):
        super().__init__(spritesheet, height, width, rows, cols)

    def load_image(self, row: int, col: int) -> AbstractImage:
        reference = pygame.Rect(col * self.width, row * self.height, self.width, self.height)
        image = pygame.Surface(reference.size).convert_alpha()
        image.fill((0, 0, 0, 0))
        image.blit(self.spritesheet, (0, 0), reference)
        return Image(image)
```

# Control

Components for a finite-state machine. Each state can be thought of as a different screen of the game such as a menu, battling,
inventory, etc. This is to simplify control flow of the entire game as we only need to maintain a **single** game loop.

## `Event`

A user input. Consumed by states to trigger some action such as clicking a button or inputting text.
It only supports key presses and basic mouse clicks.

Under the hood, it is just a bunch of enums. The `enums` folder contains definitions for event types, key presses, and mouse actions.

## `StateManager`

The finite-state machine itself, running one state at a time. It does three things in each pass for an active state.

- Passing events into it so that elements such as buttons can be triggered in that state.
- Updating the information in order to execute actions that happen over time (such as movment and timers). This is 
also where the manager monitors the flags of the state which tells the manager to transition or quit.
- Drawing the elements in the state.

A state transition is a two phase process.

- The manager resets the flag and calls the `cleanup` hook of the current state.
- It changes its current state to the next state and calls the `startup` hook of that new state.

You will notice that the `StateManager` has no loops, so what runs it? A higher level object called `App` which you will read on later.

Example usage of `StateManager`.

```python
manager = StateManager("start", {"start": Start(), "end": End()})
while True:
    manager.pass_event(None)
    manager.update(0)
    manager.draw()
```

## `State`

A state which manages a bunch of game objects. It's responsible for passing events, giving information, and drawing objects that it
contains. Usually, a `State` keeps track of data (which are its attributes) that get passed into the objects themselves for display.
Objects can then modify the data.

States also contain two hooks: `startup` and `cleanup`.
- `startup` is called before a state actually runs. This is where you can setup objects and load data.
- `cleanup` is called before a state becomes inactive. This is where you can reset attributes and clean up elements.

Normally you would inherit from this class.

```python
class Test(State):
    def __init__(self):
        super().__init__()
        self.state_info = 1

    def startup(self):
        print(self.state_info)

    def cleanup(self):
        self.state_info = 1

    def handle_event(self, event: Event):
        print(event)

    def update(self, dt: float):
        self.state_info += 1

    def draw(self):
        # Use a label to display text!
        pass
```

# `lib` Folders

These contain the actual implementations of the components and the driver code that starts the whole application.
When creating the game, you only need to import the `__init__.py` file of `/core`. 

Besides the component implementations, there are a few other noteworthy aspects.

## `App`

A higher-level wrapper over the `StateManager`. This is where you directly use the libraries like `pygame` to handle initialization,
inputs, and the main game loop. 

`App`s are then ran by driver code contained in `run.py`. These scripts simply initialize the `App`, do some other library related
setup, and then call the main loop.

A `pygame` implementation of `App`. We see that the app keeps track of a state manager and runs it in `main_loop`. In the `event_loop`, we
see the translation from `pygame` events to this engine's events.

```python
class App:
    def __init__(self, state_manager: StateManager):
        self.state_manager = state_manager
        self.fps, self.clock = 60, pygame.time.Clock()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key in translate_keys:
                self.state_manager.pass_event(Event(EventType.KEY_DOWN, key=translate_keys[event.key]))

    def main_loop(self):
        """Where the game takes place."""
        while not self.state_manager.is_done():
            dt = self.clock.tick(self.fps) / 1000
            if dt >= 0.05:
                continue
            self.event_loop()
            self.state_manager.update(dt)
            self.state_manager.draw()
            pygame.display.update()

# EXAMPLE
manager = StateManager("start", {"start": Start(), "end": End()})
app = App(manager)
app.main_loop()
```

## `Constants`

Contains library-specific constants.

- Assets which are loaded using the library. Paths to the assets are found in `/path`.
- Translations from the library's events to the game engine's `Event`.
- Additional setup that couldn't be done in `run.py`.
