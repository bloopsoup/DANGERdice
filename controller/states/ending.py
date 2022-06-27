class Ending(State):
    """The ending sequence."""

    def __init__(self):
        super().__init__()

        self.timer = DTimer(pygame.USEREVENT + 1)
        self.step = 0

        self.font = fonts[3]
        self.text = self.font.render("AND AFTER THAT FIGHT", True, (255, 255, 255))

    def cleanup(self):
        self.player.stop_move()

    def startup(self):
        pygame.mixer.music.stop()

        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(StaticBG([load_img(load_s("black.png"))], (0, 0)), 0)

        # Setup Player
        self.player.change_name("")
        self.player.direct_move(-100, 472)
        self.player.display_mode("")
        self.player.command_move(5, 0, 1000, 472)

        handle_sound("one.mp3")
        self.timer.activate(2)

    def handle_event(self, event):
        if event.type == self.timer.event:
            if self.step == 0:
                self.text = self.font.render("YOU FOUND A LOT OF MONEY", True, (255, 255, 255))

                handle_sound("one.mp3")

                self.timer.activate(1.5)
                self.step += 1
            elif self.step == 1:
                self.text = self.font.render("IN THE MOUNTAINS", True, (255, 255, 255))

                handle_sound("one.mp3")

                self.timer.activate(2)
                self.step += 1
            elif self.step == 2:
                self.text = self.font.render("DEBTS HAVE BEEN REPAID", True, (255, 255, 255))

                handle_sound("one.mp3")

                self.timer.activate(1.5)
                self.step += 1
            elif self.step == 3:
                self.text = self.font.render("HAPPY END", True, (255, 255, 255))

                handle_sound("one.mp3")

                self.timer.activate(1.5)
                self.step += 1
            else:
                self.return_menu()

    def update(self, surface, dt):
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)
        self.timer.update(dt)

        surface.blit(self.text, (self.center(self.text), 220))

    def return_menu(self):
        """Goes back to the main menu. Resets the player since they beat the game!"""
        self.player.reset_player()
        self.player.dice_set = [State.gen_dice("basic1"), State.gen_dice("basic1")]
        self.to("main_menu")