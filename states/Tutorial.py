class Tutorial(Battle):
    """A more restricted version of Battle with the aim of teaching the player the basic mechanics."""

    def __init__(self, enemy, bg, destination):
        super().__init__(enemy, bg, destination)

        # Players can't roll immediately
        self.active_dice = False

        # Lock some stuff for tutorial purposes
        self.can_end_turn = False
        self.can_refresh = False

        # Scripted die rolling. Order determines what is outputted from each roll, whether coming from you or an enemy.
        # Allowed determines which die slot you can actually use. Fixed is what the upcoming die will output.
        self.order = [5, 3, 2, 1, 3, 3, 3, 0, 2, 3, 5]
        self.fixed = -1
        self.allowed = -1

        self.text_info = ["Here's you.",
                          "Here's the enemy.",
                          "Right now it's your turn.",
                          "Click on the first die to roll it.",
                          "Rolling dice builds up damage.",
                          "Roll the other die.",
                          "Let's attack to unleash that damage!",
                          "Now it's the enemy's turn.",
                          "You can roll as much dice as you want",
                          "in order to keep building damage.",
                          "but rolling a ONE forfeits your turn.",
                          "So don't get too greedy.",
                          "Time to finish him. Keep rolling!",
                          "Destroy him."]

        # Used with tutorial_sequence() to determine what happens at a specific moment
        self.step = 0

        # A delay between the characters showing up and the dialogue box appearing.
        self.dialogue_timer = DTimer(pygame.USEREVENT + 10)

    def cleanup(self):
        """Reset tutorial to the beginning."""
        super().cleanup()

        self.step = 0
        self.active_dice = False
        self.can_end_turn = False
        self.can_refresh = False

        self.order = [5, 3, 2, 1, 3, 3, 3, 0, 2, 3, 5]
        self.fixed = -1
        self.allowed = -1

    def startup(self):
        super().startup()

        self.menu.add_widget(600, 200, [load_b("0600x75.png")], True, None, 2, DialogueBoxS, (30, 0))
        self.menu.do_dialogue_id(2, 1, self.text_info)
        self.dialogue_timer.activate(1)

    def update(self, surface, dt):
        super().update(surface, dt)
        self.dialogue_timer.update(dt)

    def handle_event(self, event):
        # Time triggered dialogue box / button display
        if event.type == self.dialogue_timer.event:
            self.advance()
            self.menu.do_dialogue_id(2, 0)
            self.menu.add_widget(70, 70, Control.sheets["button"].load_some_images(2, 0, 3), True,
                                 self.next_dialogue, 3, Button, (630, 0))

        super().handle_event(event)

    # Functions
    def ai_roll(self):
        """Scripted AI."""
        # In case there is an animation playing
        if not self.active_dice:
            return

        self.roll(self.allowed)

    def roll(self, index):
        """Much more restrictive version of roll. Connects with tutorial sequence."""
        if not self.active_dice or (index != self.allowed and self.allowed is not None):
            return

        current = self.turn_player.roll_die_forced(index, self.fixed)
        if current == 0:
            # If there is another popup, remove it and flash the ONE
            if self.flash != 0:
                self.canvas.delete_group(self.flash)

            self.popup_one()

            self.damage = 0

            self.rolled_one()
        elif current is not None:
            # Play the successful roll sound
            handle_sound("roll.mp3")
            self.damage += current

            self.advance()

    def end_turn(self):
        """Added the advance."""
        if not self.can_end_turn or not self.active_dice:
            return
        if self.damage:
            self.trigger_anim("rush", 3)
            self.advance()

    def reset_turn(self):
        """Added the advance."""
        super().reset_turn()
        self.active_dice = False
        self.advance()

    def next_dialogue(self):
        """Button function. Signals to dialogue widget to move to the next script.
           Also advances the sequence."""
        self.advance()
        self.menu.do_dialogue_id(2, 2)

    def advance(self):
        """Runs the step and then advances the step in the sequence."""
        self.tutorial_sequence()
        self.step += 1

    def tutorial_sequence(self):
        """The tutorial sequence which is linked with the textbox. Controls the Battle state."""
        if self.step == 0:
            self.canvas.add_element(StaticBG([load_img(load_s("arrowdown.png"))],
                                             (self.player_x, self.player_y - 150)), 10)
        elif self.step == 1:
            self.canvas.delete_group(10)
            self.canvas.add_element(StaticBG([load_img(load_s("arrowdown.png"))],
                                             (self.enemy_x + 10, self.enemy_y - 150)), 10)
        elif self.step == 2:
            self.canvas.delete_group(10)
        elif self.step == 3:
            self.canvas.add_element(StaticBG([load_img(load_s("arrowdown.png"))], (370, 330)), 10)
            self.menu.delete_widget(3)

            self.active_dice = True
            self.allowed = 0
            self.fixed = self.order.pop(0)
        elif self.step == 4:
            self.canvas.delete_group(10)
            self.menu.do_dialogue_id(2, 2)
            self.menu.add_widget(70, 70, Control.sheets["button"].load_some_images(2, 0, 3), True,
                                 self.next_dialogue, 3, Button, (630, 0))

            self.active_dice = False
        elif self.step == 5:
            self.canvas.add_element(StaticBG([load_img(load_s("arrowdown.png"))], (470, 330)), 10)
            self.menu.delete_widget(3)

            self.active_dice = True
            self.allowed = 1
            self.fixed = self.order.pop(0)
        elif self.step == 6:
            self.canvas.delete_group(10)
            self.menu.do_dialogue_id(2, 2)

            self.allowed = -1
            self.can_end_turn = True
        elif self.step == 7:
            self.menu.do_dialogue_id(2, 2)
            self.can_end_turn = False
        elif self.step == 8:
            self.can_refresh = True
            self.active_dice = True
            self.allowed = 0
            self.fixed = self.order.pop(0)
        elif self.step == 9:
            self.allowed = 1
            self.fixed = self.order.pop(0)
        elif self.step == 10:
            self.menu.do_dialogue_id(2, 2)
            self.allowed = 0
            self.fixed = self.order.pop(0)
        elif self.step == 11:
            self.allowed = 1
            self.fixed = self.order.pop(0)
        elif self.step == 12:
            self.menu.do_dialogue_id(2, 2)
            self.allowed = 0
            self.fixed = self.order.pop(0)
        elif self.step == 13:
            self.allowed = 1
            self.fixed = self.order.pop(0)
        elif self.step == 14:
            self.menu.do_dialogue_id(2, 2)
            self.menu.add_widget(70, 70, Control.sheets["button"].load_some_images(2, 0, 3), True,
                                 self.next_dialogue, 3, Button, (630, 0))
        elif self.step == 16:
            self.menu.delete_widget(3)
            self.active_dice = True
            self.allowed = None
            self.fixed = self.order.pop(0)
        elif self.step == 17:
            self.fixed = self.order.pop(0)
        elif self.step == 18:
            self.fixed = self.order.pop(0)
        elif self.step == 19:
            self.menu.do_dialogue_id(2, 2)
            self.can_end_turn = True
