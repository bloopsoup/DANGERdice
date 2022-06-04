class Save(State):
    """A save confirmation screen since people might want a warning before overwriting their current save."""

    def __init__(self):
        super().__init__()

        self.font = fonts[3]
        self.text = self.font.render("Save current data?", True, (0, 0, 0))

    def startup(self):
        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(StaticBG([load_img(load_s("placeholderbg.png"))], (0, 0)), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(2, 3, 3), (320, 280), BUTTON_DEFAULT,
                                     self.save_data), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 3, 3), (410, 280), BUTTON_DEFAULT,
                                     self.back), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 0, 3), (730, 530), BUTTON_DEFAULT,
                                     handle_music()), 0)

        # Setup Player
        self.player.direct_move(-100, -100)
        self.player.display_mode("")

    def update(self, surface, dt):
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)

        surface.blit(self.text, (self.center(self.text), 220))

    # Function
    def save_data(self):
        """Saves current player data."""
        save_data([self.player.package_data(), Control.state_data, None], "player_data")
        self.back()