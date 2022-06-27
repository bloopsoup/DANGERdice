class PlayerMenu(State):
    """The player_menu. Return here after every battle to stock up or save."""

    def __init__(self):
        super().__init__()

        self.font = fonts[2]
        self.text = self.font.render("Next Level: {0}".format(self.player.current_level), True, (0, 0, 0))

    def startup(self):
        handle_music("note.mp3")

        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(MovingBackgroundElement([load_img(load_s("back2.png"))], (0, -1), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_img(load_s("mhub1.png"))], (0, 0)), 0)

        self.canvas.add_element(Butt(Control.sheets["button2"].load_some_images(3, 0, 3), (0, 250), BUTTON_DEFAULT,
                                     self.play), 0)
        self.canvas.add_element(Butt(Control.sheets["button2"].load_some_images(1, 0, 3), (0, 320), BUTTON_DEFAULT,
                                     self.inventory), 0)
        self.canvas.add_element(Butt(Control.sheets["button2"].load_some_images(5, 0, 3), (0, 390), BUTTON_DEFAULT,
                                     self.shop), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 0, 3), (730, 530), BUTTON_DEFAULT,
                                     handle_music), 0)
        self.canvas.add_element(Butt(Control.sheets["button3"].load_some_images(1, 0, 3), (0, 530), BUTTON_DEFAULT,
                                     self.save), 0)
        self.canvas.add_element(Butt(Control.sheets["button3"].load_some_images(1, 3, 3), (70, 530), BUTTON_DEFAULT,
                                     self.load), 0)

        # Setup Player (should be hardcoded as Player dimensions are constant)
        self.player.stop_move()
        self.player.direct_move(38, 72)
        self.player.name_display(False)
        self.player.health_display(False)
        self.player.display_mode("menu")

    def update(self, surface, dt):
        """Draws stuff pertaining to this state. Generally, menu options should be on top."""
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)

        self.text = self.font.render("Next Level: {0}".format(self.player.current_level), True, (0, 0, 0))
        surface.blit(self.text, (self.center(self.text), 210))

    # Functions. Some are redundant but whatever.
    def play(self):
        """Onto battle!"""
        self.to(self.player.current_level)

    def shop(self):
        """Let's go shopping!"""
        # self.to("shop")
        pass

    def inventory(self):
        """Let's see your inventory."""
        self.to("inventory")

    def save(self):
        """Saves the game."""
        self.to("save")

    def load(self):
        """Loads the game."""
        self.to("load")