class Load(State):
    """A load confirmation screen since people might want a warning before
       loading data that can override their current session."""

    def __init__(self):
        super().__init__()

        self.font = fonts[3]
        self.text = self.font.render("Load saved data?", True, (0, 0, 0))

    def startup(self):
        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(StaticBG([load_img(load_s("placeholderbg.png"))], (0, 0)), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(2, 3, 3), (320, 280), BUTTON_DEFAULT,
                                     self.load_data), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 3, 3), (410, 280), BUTTON_DEFAULT,
                                     self.back), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 0, 3), (730, 530), BUTTON_DEFAULT,
                                     handle_music), 0)

        # Setup Player
        self.player.direct_move(-100, -100)
        self.player.display_mode("")

    def update(self, surface, dt):
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)

        surface.blit(self.text, (self.center(self.text), 220))

    # Function
    def load_data(self):
        """Loads player save data. If there is no data, does nothing."""
        data = load_data("player_data")
        if data:
            # Loading player
            p_data = data[0]
            self.player.level = p_data[0]
            self.player.current = p_data[1]
            self.player.health = p_data[2]
            self.player.money = p_data[3]
            self.player.dice_set = [State.gen_dice(i) for i in p_data[4]]
            self.player.inventory = [State.gen_dice(i) for i in p_data[5]]
            self.player.current_level = p_data[6]
            self.player.exp = p_data[7]
            self.player.name = p_data[8]

            # Loading states
            s_data = data[1]
            Control.load_generated_states(s_data)

            # shop_data = data[2]
            # Shop.load_data(shop_data)

            self.to("player_menu")