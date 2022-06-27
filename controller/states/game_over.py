class GameOver(State):
    """You died. Quit or load past save."""

    def __init__(self):
        super().__init__()

    def startup(self):
        handle_music("menu.mp3")

        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(MovingBackgroundElement([load_img(load_s("back1.png"))], (0, 2), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_img(load_s("bricks.png"))], (0, 0)), 0)
        self.canvas.add_element(StaticBG([load_img(load_s("gameover.png"))], (0, 0)), 0)

        self.canvas.add_element(Butt(Control.sheets["button2"].load_some_images(4, 0, 3), (0, 0), BUTTON_DEFAULT,
                                     self.return_menu), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 0, 3), (730, 530), BUTTON_DEFAULT,
                                     handle_music), 0)

        # Setup Player (should be hardcoded as Player dimensions are constant)
        self.player.name_display(True)
        self.player.health_display(False)
        self.player.display_mode("")

        self.player.status(False)
        self.player.image = self.player.images[13]
        self.player.direct_move(350, 472)

    # Functions. Some are redundant but whatever.

    def return_menu(self):
        """Goes back to the main menu. Since the player died, everything is reset for the next run if
           the user still wants to be in the same session."""
        self.player.reset_player()
        self.player.dice_set = [State.gen_dice("basic1"), State.gen_dice("basic1")]
        # Shop.refill()
        self.to("main_menu")