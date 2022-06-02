from utils import *


# WIDGETS
class WidgetImage:
    """A widget for use with menus.
       Note that widgets use images instead of regular PyGame drawings in order to utilize graphics done in PhotoShop.
       All images must have the same dimensions.
       x, y    -- Integers -- Location of the widget.
       files   -- List of file locations  -- The file locations leading to images used to represent the widget.
       borders -- Boolean -- If true, draws a black, 4px border around the widget.
       onEvent -- Function -- The function the widget runs if interacted with. Defaults to NONE.
       ID -- Integer -- An ID given to the widget. Used for deletions."""

    def __init__(self, x, y, files, borders, onEvent, ID):
        self.x, self.y = x, y
        self.ID = ID

        if not isinstance(files[0], str):
            self.images = files
        else:
            self.images = [pygame.Surface.convert_alpha(pygame.image.load(file)) for file in files]

        # This is for having a reference rectangle of the widget
        self.reference = self.images[0].get_rect()
        self.reference.move_ip(self.x, self.y)

        self.validate_images()

        self.borders = borders
        self.onEvent = onEvent

    def validate_images(self):
        """Checks if the images are all the same size."""
        for image in self.images:
            assert image.get_size() == self.reference.size, "One of these images aren't the same size as the " \
                                                            "others! "

    def draw_border(self, surface):
        """Draws the black 4px border."""
        if self.borders:
            pygame.draw.rect(surface, (0, 0, 0), self.reference, 4)

    def handle_event(self, event):
        """Handles the widget events. Unique to each specified widget."""
        raise NotImplementedError

    def update(self, surface, dt):
        """The drawing function for a widget."""
        raise NotImplementedError


class Button(WidgetImage):
    """A button that runs functions on click."""

    def __init__(self, x, y, files, borders, onEvent, ID):
        assert len(files) == 3, "Need three!"
        super().__init__(x, y, files, borders, onEvent, ID)

        self.clicked = False
        self.hovered = False

    def handle_event(self, event):
        """Handles button events."""
        # Is your mouse over the button?
        if self.reference.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
            # Did you click it?
            if event.type == pygame.MOUSEBUTTONDOWN and self.onEvent is not None:
                handle_sound("click.mp3")
                self.clicked = True
                self.onEvent()
            else:
                self.clicked = False
        else:
            self.hovered = False

    def update(self, surface, dt):
        """Draws the button. If hovered over, changes the button to second image. If clicked, changes
           the button to third image."""
        # Draw the interactive image
        if self.clicked:
            surface.blit(self.images[2], (self.x, self.y))
        elif self.hovered:
            surface.blit(self.images[1], (self.x, self.y))
        else:
            surface.blit(self.images[0], (self.x, self.y))

        # Then draw the border
        self.draw_border(surface)


class ButtonArg(Button):
    """A button that runs functions on click providing one argument."""

    def __init__(self, x, y, files, borders, onEvent, ID, param):
        super().__init__(x, y, files, borders, onEvent, ID)
        self.param = param

    def handle_event(self, event):
        """Handles button events but runs a function with provided argument."""
        # Is your mouse over the button?
        if self.reference.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
            # Did you click it?
            if event.type == pygame.MOUSEBUTTONDOWN and self.onEvent is not None:
                self.clicked = True
                self.onEvent(self.param)
            else:
                self.clicked = False
        else:
            self.hovered = False


class InputText(WidgetImage):
    """Input some text. Text will be centered in the input box as you type."""

    def __init__(self, x, y, files, borders, onEvent, ID):
        assert len(files) == 2, "Need two!"
        super().__init__(x, y, files, borders, onEvent, ID)

        self.active = False

        # By default, we will use Times New Roman black. Scaled where 50 pt fits a 600x75 box as reference
        self.text = ""
        self.font_size = int((50 * self.reference.height) / 75)
        self.font = pygame.font.Font(rp("assets/VT323-Regular.ttf"), self.font_size)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))

    def submit_text(self):
        """Function for other widgets to call in order to submit the stored text."""
        self.onEvent(self.text)
        self.text = ''

    def handle_event(self, event):
        """Handles input events. Allows you type in text."""
        # Check for clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Did you click the box?
            if self.reference.collidepoint(pygame.mouse.get_pos()):
                self.active = not self.active
            else:
                self.active = False

        # What to do if you press keys?
        if event.type == pygame.KEYDOWN:
            # You have to be in the textbox first
            if self.active:
                # Do something when you press ENTER
                if event.key == pygame.K_RETURN:
                    self.onEvent(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    # To prevent the text from going out of the box
                    if self.text_surface.get_width() + self.font_size + 35 <= self.reference.width:
                        self.text += event.unicode

    def update(self, surface, dt):
        """Draws the input box. If clicked, it lights up indicating you can type in stuff."""
        # Draw the interactive box
        if self.active:
            surface.blit(self.images[1], (self.x, self.y))
        else:
            surface.blit(self.images[0], (self.x, self.y))

        # Then draw the border
        self.draw_border(surface)

        # Then the text
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        x_center = int((self.reference.width - self.text_surface.get_width())/2)
        y_center = int((self.reference.height - self.text_surface.get_height())/2)

        surface.blit(self.text_surface, (self.reference.x + x_center, self.reference.y + y_center))


class DialogueBox(WidgetImage):
    """Displays text like it's typed. Consists of the main text box and the displayed portrait of the speaking
       character which will be added before display. When initializing, order should be 1 --> 3 --> 0.
       Assumes the box is 200x600 px."""

    def __init__(self, x, y, files, borders, onEvent, ID):
        assert len(files) == 1, "Need one!"
        super().__init__(x, y, files, borders, onEvent, ID)

        self.active = False

        self.scripts = None
        self.display = ""
        self.portraits = None
        self.seq = ""

        self.current = -1
        self.letter = -1
        self.count = -1
        self.lines = 3

        self.frame = 0.03

        self.font_size = 35
        self.font = pygame.font.Font(rp("assets/VT323-Regular.ttf"), self.font_size)
        self.text_surface = self.font.render("", True, (0, 0, 0))

    def toggle_visible(self):
        """Toggle visibility of this dialogue box."""
        self.active = not self.active

    def add_portraits(self, images, seq):
        """Adds the displayed portraits to the dialogue box. Images should be 100x100px and should have length of 2.
           SEQ is a string consisting of '0' or '1' where the length should match with the length of scripts."""
        assert len(images) == 2, "Must have two!"
        self.portraits = images
        self.seq = seq

    def add_scripts(self, scripts):
        """Will set the scripts for the dialogue box. SCRIPTS is a list of strings where each
           string corresponds its own box. Note that if you use '`' in your scripts, the box
           will treat it as a delay character."""
        assert len(scripts) > 0, "Can't have no scripts!"

        self.scripts = scripts
        self.display = ""
        self.current = 0
        self.letter = 0
        self.count = 0

    def next_script(self):
        """Loads the next script. If we reached the end, turn off text box visibility and returns -1."""
        self.display = ""
        self.current += 1
        self.letter = 0
        self.count = 0

        if self.current >= len(self.scripts):
            self.toggle_visible()
            return -1

    def handle_event(self, event):
        """For this widget, other buttons will call this widget's functions."""
        pass

    def update(self, surface, dt):
        if not self.active:
            return

        # Draw text box
        surface.blit(self.images[0], (self.x, self.y))
        self.draw_border(surface)

        # Draw portrait
        if self.seq[self.current] == "0":
            surface.blit(self.portraits[0], (self.x, self.y - 100))
        else:
            surface.blit(self.portraits[1], (self.x + 500, self.y - 100))

        if self.letter < len(self.scripts[self.current]):
            self.count += dt
            if self.count >= self.frame:
                self.count = 0

                char = self.scripts[self.current][self.letter]
                if char != "`":
                    self.display += char
                    handle_sound("text.mp3")
                self.letter += 1

        x_left = 20
        for i in range(self.lines):
            self.text_surface = self.font.render(self.display[i*40:(i+1)*40], True, (0, 0, 0))
            y_up = 35 * (i + 1)
            surface.blit(self.text_surface, (self.reference.x + x_left, self.reference.y + y_up))


class DialogueBoxS(DialogueBox):
    """Dialogue box but only one line long with no portraits or sequences. Assumes box is 75x600 px."""

    def __init__(self, x, y, files, borders, onEvent, ID):
        assert len(files) == 1, "Need one!"
        super().__init__(x, y, files, borders, onEvent, ID)
        self.frame = 0.02

    def update(self, surface, dt):
        if not self.active:
            return

        # Draw text box
        surface.blit(self.images[0], (self.x, self.y))
        self.draw_border(surface)

        if self.letter < len(self.scripts[self.current]):
            self.count += dt
            if self.count >= self.frame:
                self.count = 0

                char = self.scripts[self.current][self.letter]
                if char != "`":
                    self.display += char
                    handle_sound("text.mp3")
                self.letter += 1

        x_left = 20
        self.text_surface = self.font.render(self.display[0:40], True, (0, 0, 0))
        y_up = 20
        surface.blit(self.text_surface, (self.reference.x + x_left, self.reference.y + y_up))


# MENUS
class SimpleMenu:
    """SimpleMenu is a container object for widgets. It is defined by the top border and a center for added widgets.
       This menu is simple because it only offers one column.
       spacing -- Integer -- Pixels in between widgets.
       top_border -- Integer -- The top border of the menu.
       center -- Integer -- The center of the menu. Note that by default, it should be half the screen width."""

    def __init__(self, spacing, top_border, center):
        self.current = top_border
        self.center = center
        self.spacing = spacing

        self.widgets = []

    def handle_event(self, event):
        """Handles events for all the widgets the menu has."""
        for widget in self.widgets:
            widget.handle_event(event)

    def update(self, surface, dt):
        """Draws the widgets."""
        for widget in self.widgets:
            widget.update(surface, dt)

    def validate(self, x, y, width, height):
        """Checks if a widget will not collide with another widget."""
        reference = pygame.Rect(x, y, width, height)
        for widget in self.widgets:
            if reference.colliderect(widget.reference):
                return False
        return True

    def add_widget(self, width, height, files, borders, onEvent, ID, widget_type, other=None):
        """Adds a widget to the menu using their respective constructor. Note that width and height is supposed to match
           the dimension of your images. If provided (x, y), widget is placed at that location instead.
           other -- (x, y) -- Location of the widget.
           widget_type -- Class Name -- Type of widget to make."""
        if other is not None:
            assert self.validate(other[0], other[1], width, height), "Conflicts with other widgets!"
            self.widgets.append(widget_type(other[0], other[1], files, borders, onEvent, ID))
        else:
            self.widgets.append(widget_type(self.center - (width / 2), self.current, files, borders, onEvent, ID))
            self.current += height + self.spacing

    def add_button_special(self, width, height, files, borders, onEvent, ID, param, other=None):
        """Functions like add_widget but with the sole purpose of adding the ButtonArg to the menu."""
        if other is not None:
            assert self.validate(other[0], other[1], width, height), "Conflicts with other widgets!"
            self.widgets.append(ButtonArg(other[0], other[1], files, borders, onEvent, ID, param))
        else:
            self.widgets.append(ButtonArg(self.center - (width / 2), self.current, files, borders, onEvent, ID, param))
            self.current += height + self.spacing

    def check_id(self, ID):
        """Checks if an elements exists with that ID."""
        return any([element.ID == ID for element in self.widgets])

    def do_text_input_id(self, ID):
        """Will call the submit function of the input text widget with that ID."""
        for widget in self.widgets:
            if widget.ID == ID:
                widget.submit_text()

    def do_dialogue_id(self, ID, *args):
        """Will perform a command on a DialogueBox that has that ID. For args: 0 is toggle, 1 is add_scripts,
        2 is next_script, 3 is add portraits."""
        for widget in self.widgets:
            if widget.ID == ID:
                if args[0] == 0:
                    return widget.toggle_visible()
                elif args[0] == 1:
                    return widget.add_scripts(args[1])
                elif args[0] == 2:
                    return widget.next_script()
                else:
                    return widget.add_portraits(args[1], args[2])

    def delete_widget(self, ID):
        """Deletes a widget from the menu with specified ID. Only one object in the menu must have
           that ID. Not safe as it doesn't change CURRENT. """
        for i in range(len(self.widgets)):
            if self.widgets[i].ID == ID:
                self.widgets.pop(i)
                break
