class Story(State):
    """Today is not your lucky day."""

    def __init__(self):
        super().__init__()

        self.enemy = State.gen_enemy("dorita", 0)
        self.enemy_extra = State.gen_enemy("aaron", 0)

        self.text_info = [["Ah Monday.",
                           "Another day running my shady casino.",
                           "Good morning.",
                           "Wow, you're already here.",
                           "Don't you think it's a bit early for    gambling everything away?",
                           "It's never too early.",
                           "And besides, ````````I'm feeling lucky.",
                           "And so do other people.",
                           "There goes the last of my money.",
                           "Why do people keep getting jackpots?",
                           "Told you so.",
                           "Got my jackpot as well, ````so where's my   money?",
                           "Well... ``````",
                           "Do you take I.O.U's?",
                           "No.",
                           "Then I have another solution.",
                           "What is it?",
                           "What the...",
                           "MY MONEY!"], "0010011100110010111", [0, 4]]
        self.portraits = [Control.sheets["portrait1"].load_image(0, 0),
                          Control.sheets["portrait1"].load_image(self.text_info[2][0], self.text_info[2][1])]

        self.timer = DTimer(pygame.USEREVENT + 1)
        self.step = 0

        self.player_y = 257
        self.enemy_y = self.player_y - self.enemy.image.get_height() + 100
        self.enemy_extra_y = self.player_y - self.enemy_extra.image.get_height() + 100

        self.font = fonts[3]
        self.text = self.font.render("", True, (255, 255, 255))

    def cleanup(self):
        self.menu = None
        self.canvas = None

        self.step = 0

    def startup(self):
        pygame.mixer.music.stop()

        # Setup Menu
        self.menu = SimpleMenu(15, 330, 400)
        self.menu.add_widget(70, 70, Control.sheets["button"].load_some_images(1, 0, 3), True, handle_music, 0,
                             Button, (730, 530))
        self.menu.add_widget(600, 200, [load_b("text600x200.png")], True, None, 1, DialogueBox)
        self.menu.do_dialogue_id(1, 1, self.text_info[0])
        self.menu.do_dialogue_id(1, 3, self.portraits, self.text_info[1])
        self.timer.activate(2.5)

        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(StaticBG([load_img(load_s("land0.png"))], (0, 0)), 0)
        self.canvas.add_element(MovingBackgroundElement([load_img(load_s("cloud1.png"))], (-1, 0), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_img(load_s("ground0.png"))], (0, 0)), 0)

        # Setup Player (should be hardcoded as Player dimensions are constant)
        self.player.direct_move(-100, 257)
        self.player.command_move(2, 0, 100, 257)
        self.player.name_display(True)
        self.player.health_display(False)
        self.player.display_mode("")

        # Setup enemies
        self.enemy.direct_move(900, self.enemy_y)
        self.enemy.name_display(True)
        self.enemy.health_display(False)
        self.enemy.display_mode("")

        self.enemy_extra.direct_move(900, self.enemy_y)
        self.enemy_extra.name_display(True)
        self.enemy_extra.health_display(False)
        self.enemy_extra.display_mode("")

    def handle_event(self, event):
        """Needed a timer this time to finish the movement."""
        self.menu.handle_event(event)

        # Story sequence works with timer so this is used
        if event.type == self.timer.event:
            if self.step == 0:
                self.menu.do_dialogue_id(1, 0)
                self.menu.add_widget(70, 70, Control.sheets["button"].load_some_images(2, 0, 3), True,
                                     self.next_dialogue, 2, Button, (700, 330))
            elif self.step == 2:
                self.menu.do_dialogue_id(1, 0)
                self.menu.add_widget(70, 70, Control.sheets["button"].load_some_images(2, 0, 3), True,
                                     self.next_dialogue, 2, Button, (700, 330))
            elif self.step == 8:
                self.canvas.delete_group(1)

                self.text = self.font.render("", True, (255, 255, 255))
                self.enemy_extra.direct_move(300, self.enemy_extra_y)
                self.enemy_extra.command_move(5, 0, 1000, self.enemy_extra_y)

                self.advance()
                self.timer.activate(2)
            elif self.step == 9:
                self.player.command_move(5, 0, 100, 257)

                self.advance()
                self.timer.activate(1.2)
            elif self.step == 10:
                self.menu.do_dialogue_id(1, 0)
                self.menu.add_widget(70, 70, Control.sheets["button"].load_some_images(2, 0, 3), True,
                                     self.next_dialogue, 2, Button, (700, 330))
            elif self.step == 12:
                self.menu.do_dialogue_id(1, 0)
                self.menu.add_widget(70, 70, Control.sheets["button"].load_some_images(2, 0, 3), True,
                                     self.next_dialogue, 2, Button, (700, 330))
            elif self.step == 19:
                self.menu.do_dialogue_id(1, 0)
                self.menu.add_widget(70, 70, Control.sheets["button"].load_some_images(2, 0, 3), True,
                                     self.next_dialogue, 2, Button, (700, 330))
            elif self.step == 21:
                self.to(self.player.current_level)

    def update(self, surface, dt):
        """Needed for updating timer."""
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)
        self.enemy.update(surface, dt)
        self.enemy_extra.update(surface, dt)
        self.menu.update(surface, dt)
        self.timer.update(dt)

        surface.blit(self.text, (self.center(self.text), 220))

    # Functions
    def next_dialogue(self):
        """Button function. Signals to dialogue widget to move to the next script.
           Also advances the sequence."""
        self.advance()
        self.menu.do_dialogue_id(1, 2)

    def advance(self):
        """Runs the step and then advances the step in the sequence."""
        self.story_sequence()
        self.step += 1

    def story_sequence(self):
        """Controls how the cutscene executes."""
        if self.step == 1:
            self.menu.delete_widget(2)
            self.menu.do_dialogue_id(1, 0)

            self.enemy.command_move(3, 0, 580, self.enemy_y)

            self.timer.activate(2)
        elif self.step == 7:
            self.menu.delete_widget(2)
            self.menu.do_dialogue_id(1, 0)

            self.canvas.add_element(StaticBG([load_img(load_s("black.png"))], (0, 0)), 1)
            self.text = self.font.render("2 HOURS LATER", True, (255, 255, 255))
            handle_sound("one.mp3")

            self.player.direct_move(-100, 257)
            self.enemy.direct_move(900, self.enemy_y)

            self.timer.activate(1.5)
        elif self.step == 11:
            self.menu.delete_widget(2)
            self.menu.do_dialogue_id(1, 0)

            self.enemy.command_move(4, 0, 580, self.enemy_y)

            self.timer.activate(1.5)
        elif self.step == 18:
            self.menu.delete_widget(2)
            self.menu.do_dialogue_id(1, 0)

            self.player.command_move(10, 0, 1000, 257)

            self.timer.activate(1.2)
        elif self.step == 20:
            self.menu.delete_widget(2)

            self.enemy.command_move(10, 0, 1000, self.enemy_y)

            self.timer.activate(1.2)