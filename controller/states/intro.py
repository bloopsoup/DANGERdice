class Intro(State):
    """Screen to give your character a name."""

    def __init__(self):
        super().__init__()
        self.timer = DTimer(pygame.USEREVENT + 1)

        self.destination = "player_menu"
        self.player.current_level = "l0-1"

        self.font = fonts[2]
        self.text = self.font.render("", True, (0, 0, 0))

    def cleanup(self):
        self.text = self.font.render("", True, (0, 0, 0))

    def startup(self):
        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(StaticBG([load_img(load_s("land1.png"))], (0, 0)), 0)
        self.canvas.add_element(MovingBackgroundElement([load_img(load_s("cloud0.png"))], (-1, 0), (800, 600)), 0)

        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 0, 3), (730, 530), BUTTON_DEFAULT,
                                     handle_music), 0)
        input_textbox = InputT([load_img(load_b("1600x75.png")), load_img(load_b("0600x75.png"))],
                               (0, 200), INPUT_DEFAULT, self.enter_name)
        self.canvas.add_element(input_textbox, 1)
        self.canvas.add_element(Butt(Control.sheets["button4"].load_some_images(1, 0, 3), (0, 300), BUTTON_DEFAULT,
                                     self.skip_tutorial), 2)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(0, 0, 3), (0, 0), BUTTON_DEFAULT,
                                     self.back), 3)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(2, 0, 3), (700, 130), BUTTON_DEFAULT,
                                     input_textbox.submit_text), 4)

        # Setup Player (should be hardcoded as Player dimensions are constant)
        self.player.name_display(True)
        self.player.health_display(False)
        self.player.display_mode("")
        self.player.direct_move(350, 472)

    def handle_event(self, event):
        """Needed a timer this time to finish the animation."""
        self.canvas.handle_event(event)

        if event.type == self.timer.event:
            self.to(self.destination)

    def update(self, surface, dt):
        """Needed for updating timer."""
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)
        self.timer.update(dt)

        surface.blit(self.text, (self.center(self.text), 220))

    def back(self):
        """Goes back to the previous state. Restores player settings to enable story."""
        self.player.current_level = "l0-1"
        self.destination = "player_menu"
        self.to(self.previous)

    # Functions

    def enter_name(self, text):
        """Once you entered a name, gives the player that name and moves him off screen. We then
           wait 2 seconds (to finish animation) and move onto the story state."""
        self.canvas.delete_group(1)
        self.canvas.delete_group(2)
        self.canvas.delete_group(3)
        self.canvas.delete_group(4)
        self.player.change_name(text)
        self.player.command_move(5, 0, 1000, 472)
        self.timer.activate(2)

    def skip_tutorial(self):
        """Skips the story and tutorial level."""
        self.player.current_level = "l0-1"
        self.destination = "player_menu"
        self.player.exp = 1
        self.canvas.delete_group(2)
        self.text = self.font.render("Tutorial will be skipped.", True, (0, 0, 0))