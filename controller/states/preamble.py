class Preamble(State):
    """Sometimes you have a chit-chat before battle."""

    def __init__(self, enemy, bg, destination):
        super().__init__()

        self.destination = destination
        self.enemy = enemy
        self.bg = bg

        self.text_info = self.enemy.preamble
        self.portraits = [Control.sheets["portrait1"].load_image(0, 0),
                          Control.sheets["portrait1"].load_image(self.text_info[2][0], self.text_info[2][1])]
        self.d_box = None

        self.player_x = 60
        self.player_y = 257
        self.enemy_x = 800 - self.player_x - self.enemy.image.get_width()
        self.enemy_y = self.player_y - self.enemy.image.get_height() + 100

        self.timer = DTimer(pygame.USEREVENT + 1)

    def startup(self):
        pygame.mixer.music.stop()

        self.timer.activate(1)

        self.canvas = Canvas()
        self.canvas.add_element(StaticBG([load_img(load_s("{0}.png".format(self.bg)))], (0, 0)), 0)
        self.canvas.add_element(MovingBackgroundElement([load_img(load_s("cloud{0}.png".format(self.bg)))],
                                                        (-1, 0), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_img(load_s("ground0.png"))], (0, 0)), 1)

        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 0, 3), (730, 530), BUTTON_DEFAULT,
                                     handle_music), 0)
        d_data = DData(self.text_info[0], self.portraits, self.text_info[1])
        self.d_box = DBox([load_img(load_b("text600x200.png"))], (0, 100), DIALOGUE_DEFAULT, self.next_dialogue, d_data)
        self.canvas.add_element(self.d_box, 1)

        self.player.direct_move(-300, self.player_y)
        self.player.command_move(10, 0, self.player_x, self.player_y)
        self.player.name_display(False)
        self.player.display_mode("")
        self.player.health_display(False)

        self.enemy.direct_move(1000, self.enemy_y)
        self.enemy.command_move(10, 0, self.enemy_x, self.enemy_y)
        self.enemy.name_display(False)
        self.enemy.display_mode("")
        self.enemy.health_display(False)

    def handle_event(self, event):
        """Handles events in this state."""
        self.canvas.handle_event(event)
        if event.type == self.timer.event:
            self.d_box.toggle_visibility()

    def update(self, surface, dt):
        """Draws stuff pertaining to this state. Generally, menu options should be on top."""
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)
        self.enemy.update(surface, dt)
        self.timer.update(dt)

    # Functions
    def next_dialogue(self):
        """Signals to dialogue widget to move to the next script. Reaching end of script triggers something."""
        if not self.d_box.next_script():
            self.to(self.destination)