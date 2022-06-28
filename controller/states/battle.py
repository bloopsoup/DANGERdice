class Battle(State):
    """First construct it with an enemy, their dice_set and a bg elements. Destination is the
       state to move to after the battle is over.
       Animations will scale with the enemy dimensions."""

    def __init__(self, enemy, bg, destination):
        super().__init__()

        # When you defeat an enemy
        self.destination = destination

        # This attribute only gets set in generate_states thus the last level will lead to the ending state
        self.next_level = "ending"

        # A delay made for the AI's turn
        self.timer = DTimer(pygame.USEREVENT + 1)

        # For flashing notices on screen such as REROLLED
        self.flash_timer = DTimer(pygame.USEREVENT + 2)
        self.flash = 0

        # Animations
        self.anim_timer = DTimer(pygame.USEREVENT + 3)
        self.current_anim = None
        self.animations = {
            "rush": self.run_rush,
            "enemy_death": self.run_loot,
            "player_death": self.run_dead
        }
        self.anim = -1

        # Status
        self.status_timer = DTimer(pygame.USEREVENT + 4)
        self.current_status = None

        # Your foe you will fight
        self.enemy = enemy
        self.enemy.dice_set = [State.gen_dice(i) for i in self.enemy.preference]

        # Dimensions and references to set up
        self.bg = bg

        self.player_x = 60
        self.player_y = 257
        self.enemy_x = 800 - self.player_x - self.enemy.image.get_width()
        self.enemy_y = self.player_y - self.enemy.image.get_height() + 100

        # Is it your turn?
        self.turn_player = self.player

        # Can you touch dice
        self.active_dice = True

        # Mechanic Overrides
        self.can_end_turn = True
        self.can_refresh = True

        # The damage character will deal
        self.damage = 0
        self.poison_damage = 0
        self.heal_value = 0
        self.weaken_attack = 1

        # Fonts
        self.font = fonts[0]
        self.big_font = fonts[3]
        self.text_damage = self.font.render("DMG: {0} PSN: {1} HEAL: {2} WKN: {3}X".format(
            self.damage // self.turn_player.divided, self.poison_damage, self.heal_value,
            self.weaken_attack), True, (0, 0, 0))
        self.text_reward = ""

    def cleanup(self):
        """Resets the dice for both players, erases damage, revives the enemy, sets the dice
           to active and makes it the player's turn. Will only be used for replay purposes."""
        # Disables enemy AI timer
        self.timer.deactivate()

        self.enemy.current = self.enemy.health
        self.enemy.dead = False
        self.enemy.display_mode("")
        self.enemy.reset_dice()

        self.damage = 0
        self.poison_damage = 0
        self.heal_value = 0
        self.weaken_attack = 1

        self.player.reset_dice()

        self.turn_player = self.player

        self.active_dice = True

        self.current_anim = None
        self.current_status = None

        # Cleanse
        self.player.cleanse()
        self.enemy.cleanse()

    def startup(self):
        handle_music(random.choice(["huh.mp3", "ones.mp3", "stomp.mp3", "stomp2.mp3", "trittle.mp3", "doma.mp3",
                                    "calm.mp3", "Something.mp3", "hurt.mp3", "somedrums.mp3", "zins.mp3", "jong.mp3"]))

        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(StaticBG([load_img(load_s("{0}.png".format(self.bg)))], (0, 0)), 0)
        self.canvas.add_element(MovingBackgroundElement([load_img(load_s("cloud{0}.png".format(self.bg)))],
                                                        (-1, 0), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_img(load_s("phub0.png"))], (0, 0)), 1)

        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 0, 3), (730, 0), BUTTON_DEFAULT,
                                handle_music), 0)
        self.canvas.add_element(Butt(Control.sheets["button4"].load_some_images(0, 0, 3), (580, 370), BUTTON_DEFAULT,
                                     self.end_turn), -1)

        placeholder = [load_img(load_b("hold_die.png")) for _ in range(3)]
        self.canvas.add_element(Butt(placeholder, (369, 455), BUTTON_GHOST, lambda: self.roll_select(0)), 0)
        self.canvas.add_element(Butt(placeholder, (469, 455), BUTTON_GHOST, lambda: self.roll_select(1)), 0)
        self.canvas.add_element(Butt(placeholder, (569, 455), BUTTON_GHOST, lambda: self.roll_select(2)), 0)
        self.canvas.add_element(Butt(placeholder, (669, 455), BUTTON_GHOST, lambda: self.roll_select(3)), 0)

        # Setup Effects
        self.effects = EffectManager()
        spark = load_files("assets/screens/spark100x100/", 5)

        # Adding effects
        for i in range(20):
            # Sparks
            self.effects.add_effect(spark, 0, self.enemy_x - random.randint(-20, 20),
                                    self.enemy_y + random.randint(-80, 80))
            self.effects.add_effect(spark, 1, self.player_x - random.randint(-20, 20),
                                    self.player_y + random.randint(-80, 80))

        # Setup Players and Enemies
        self.player.direct_move(-300, self.player_y)
        self.player.command_move(10, 0, self.player_x, self.player_y)
        self.player.name_display(True)
        self.player.display_mode("player")
        self.player.health_display(True)
        self.player.reset_dice()

        self.enemy.direct_move(1000, self.enemy_y)
        self.enemy.command_move(10, 0, self.enemy_x, self.enemy_y)
        self.enemy.name_display(True)
        self.enemy.display_mode("")
        self.enemy.health_display(True)
        self.enemy.reset_dice()

        self.turn_player.blessed = random.randint(1, 4)

    def handle_event(self, event):
        """Handles events in this state. In this case, handles battling which comes with
           a lot more events."""
        self.canvas.handle_event(event)

        # INDICATORS

        if event.type == self.status_timer.event:
            if self.current_status == "poison":
                self.popup_poison()
            elif self.current_status == "death":
                if self.enemy.dead:
                    self.trigger_anim("enemy_death", 3)
                else:
                    self.trigger_anim("player_death", 1)

        # Gets rid of the indicator in time
        if event.type == self.flash_timer.event:
            if self.flash == -1 or self.flash == 4:
                self.enemy.status(True)
                self.player.status(True)
            if self.flash > 0:
                self.canvas.delete_group(self.flash)
            self.flash = 0

        # ANIMATIONS

        # Doing the attack animation
        if event.type == self.anim_timer.event:
            self.animations[self.current_anim]()

        # DYING STOP
        if self.enemy.dead or self.player.dead:
            # Maybe redundant, but NO dice rolling at all when enemy dies
            self.active_dice = False
            return

        # ROLLING

        if event.type == pygame.KEYDOWN and self.turn_player == self.player and self.active_dice:
            if event.key == pygame.K_RETURN:
                self.end_turn()
            elif event.key == pygame.K_a:
                self.roll(0)
            elif event.key == pygame.K_s:
                self.roll(1)
            elif event.key == pygame.K_d:
                self.roll(2)
            elif event.key == pygame.K_f:
                self.roll(3)

        # Making the AI roll periodically
        if self.turn_player == self.enemy and event.type == self.timer.event:
            self.ai_roll()

        # Checks if the dice have been all rolled
        if self.turn_player.needs_reset() and self.flash == 0 and self.can_refresh:
            self.turn_player.reset_dice()
            self.popup_refresh()

    def update(self, surface, dt):
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)
        self.enemy.update(surface, dt)
        self.effects.update(surface, dt)

        # Timers
        self.timer.update(dt)
        self.flash_timer.update(dt)
        self.anim_timer.update(dt)
        self.status_timer.update(dt)

        # Show current damage
        self.text_damage = self.font.render("DMG: {0} PSN: {1} HEAL: {2} WKN: {3}X".format(
            self.damage // self.turn_player.divided, self.poison_damage, self.heal_value,
            self.weaken_attack), True, (0, 0, 0))
        if self.turn_player == self.player:
            surface.blit(self.text_damage, (370, 435))
        else:
            surface.blit(self.text_damage, (50, 435))

        # Show loot if able
        if len(self.text_reward):
            text_reward = self.big_font.render(self.text_reward, True, (0, 0, 0))
            surface.blit(text_reward, (self.center(text_reward), 100))

    # BATTLE FUNCTIONS
    def roll_select(self, i):
        """Call roll with i."""
        if self.turn_player == self.player:
            self.roll(i)

    def ai_roll(self):
        """Has the enemy roll their own dice. Current is the index of the
           die the AI wants to roll. Can change current to be a different AI."""
        # In case there is an animation playing
        if not self.active_dice:
            return

        current = self.enemy.basic_ai(self.player.current, self.damage, self.poison_damage, self.heal_value,
                                      self.weaken_attack)
        if current == -1:
            self.end_turn()
        else:
            self.roll(current)

    def roll(self, index):
        """Handles actual rolling. Must have active_dice to roll in the first place.
           We get their roll and if it happens to be a one, we make the turn void. Else
           we add to the damage."""
        # In case there is an animation playing
        if not self.active_dice:
            return

        current = self.turn_player.roll_die(index)
        if current == 0:
            # If there is another popup, remove it and flash the ONE
            if self.flash != 0:
                self.canvas.delete_group(self.flash)
            self.popup_one()

            self.damage = 0
            self.poison_damage = 0
            self.heal_value = 0
            self.weaken_attack = 1

            self.rolled_one()
        elif current is not None:
            # Play the successful roll sound
            handle_sound("roll.mp3")

            # Since battling and Die types are separate, special dice effects are checked here
            if isinstance(self.turn_player.dice_set[index], Poison):
                self.poison_damage += current
            elif isinstance(self.turn_player.dice_set[index], Heal):
                handle_sound("heal.mp3")
                self.heal_value += current
            elif isinstance(self.turn_player.dice_set[index], Divider):
                self.weaken_attack = current
            elif isinstance(self.turn_player.dice_set[index], Multiplier):
                self.damage *= current
            else:
                self.damage += current

    def end_turn(self):
        """Function that's called when the player wants to end their turn."""
        if not self.can_end_turn or not self.active_dice:
            return

        if self.damage or self.poison_damage or self.weaken_attack > 1:
            self.trigger_anim("rush", 3)
        elif self.heal_value:
            self.rolled_one()

    def rolled_one(self):
        """Facilitates the turn switching by applying damage and then
           updating HUB and AI with process_status()."""
        self.active_dice = False

        # Apply divider
        self.damage //= self.turn_player.divided
        self.turn_player.divided = 1

        # Get rid of blessed status
        self.turn_player.blessed = 0

        # Deduct health from the other side
        if self.turn_player == self.player:
            self.enemy.current -= self.damage
            self.enemy.poison += self.poison_damage
            self.enemy.divided = self.weaken_attack
        else:
            self.player.current -= self.damage
            self.player.poison += self.poison_damage
            self.player.divided = self.weaken_attack

        # Healing
        self.turn_player.current = min(self.turn_player.health, self.turn_player.current + self.heal_value)
        self.turn_player.poison = max(0, self.turn_player.poison - self.heal_value)

        self.process_status()

    def process_status(self):
        """Process the statuses before ending the player's turn. If there is a status, turn will be postponed
           to display/process a status(es)."""
        if self.turn_player.poison > 0:
            self.current_status = "poison"
            self.status_timer.activate(0.7)
        else:
            self.reset_turn()

    def next_turn(self):
        """Switches the player's turn."""
        if self.turn_player == self.player:
            self.turn_player = self.enemy
        else:
            self.turn_player = self.player

    def switch(self):
        """Handles the hub and displays and also enables and disables the AI."""
        if self.turn_player == self.player:
            self.canvas.delete_group(2)
            self.canvas.add_element(StaticBG([load_img(load_s("phub0.png"))], (0, 0)), 1)
            self.player.display_mode("player")
            self.enemy.display_mode("")
            self.canvas.add_element(Butt(Control.sheets["button4"].load_some_images(0, 0, 3), (580, 370),
                                         BUTTON_DEFAULT, self.end_turn), -1)

            self.timer.deactivate()

            # A little rigging
            self.turn_player.blessed = random.randint(1, 4)
        else:
            self.canvas.delete_group(1)
            self.canvas.add_element(StaticBG([load_img(load_s("ehub0.png"))], (0, 0)), 2)
            self.player.display_mode("")
            self.enemy.display_mode("enemy")
            self.canvas.delete_group(-1)

            self.timer.activate(1, True)

    def handle_dying(self):
        """Handles who dies during turns. If one kills the opposing player and will subsequently die
           from statuses themself, they will live with 1 HP with no status."""
        if self.turn_player == self.player:
            if self.enemy.current <= 0:
                self.enemy.die()
                if self.turn_player.current <= 0:
                    self.turn_player.cleanse()
                    self.turn_player.current = 1
            elif self.turn_player.current <= 0:
                self.turn_player.die()
        else:
            if self.player.current <= 0:
                self.player.die()
                if self.turn_player.current <= 0:
                    self.turn_player.cleanse()
                    self.turn_player.current = 1
            elif self.turn_player.current <= 0:
                self.turn_player.die()

    def reset_turn(self):
        """Resets damage, the leaving player's dice, and switch the turn player and hub and enable
           active dice if needed."""
        # Check for deaths
        self.handle_dying()
        self.trigger_death()

        self.damage = 0
        self.poison_damage = 0
        self.heal_value = 0
        self.weaken_attack = 1

        self.turn_player.reset_dice()
        self.next_turn()
        self.switch()
        self.active_dice = True

    # DISPLAYS
    def remove_popups(self):
        """Remove the current popups."""
        self.canvas.delete_group(3)
        self.canvas.delete_group(4)

    def popup_one(self):
        """Pop up the one display."""
        handle_sound("one.mp3")
        self.remove_popups()
        self.canvas.add_element(StaticBG([load_img(load_s("one.png"))], (0, 210)), 4)
        self.flash_timer.activate(0.5)
        self.flash = 4

        # For flashing the character as hurt
        self.turn_player.status(False)
        self.turn_player.image = self.turn_player.images[13]

    def popup_refresh(self):
        """Pop up the refresh display."""
        self.remove_popups()
        self.canvas.add_element(StaticBG([load_img(load_s("refresh.png"))], (0, 210)), 3)
        self.flash_timer.activate(0.5)
        self.flash = 3

    def popup_poison(self):
        """Flash a poison display to show a character is hurt by poison."""
        self.remove_popups()

        handle_sound("poison.mp3")

        self.turn_player.current -= self.turn_player.poison
        self.turn_player.poison -= 1

        self.flash_timer.activate(0.5)
        self.flash = -1

        # For flashing the character as hurt
        self.turn_player.status(False)
        self.turn_player.image = self.turn_player.images[13]

        self.reset_turn()

    # ANIMATION FUNCTIONS
    def trigger_anim(self, animation, steps):
        """Trigger an animation."""
        self.active_dice = False
        self.anim_timer.activate(0.1)
        self.current_anim = animation
        self.anim = steps

    def trigger_death(self):
        """Trigger the death animation. This function is here just to provide a delay."""
        if self.enemy.dead:
            self.current_status = "death"
            self.status_timer.activate(0.5)
        elif self.player.dead:
            self.current_status = "death"
            self.status_timer.activate(0.5)

    def run_rush(self):
        """Run the RUSH attack animation. Time for animation stays the same while the speed is scaled."""
        # Setting the appropriate references
        if self.turn_player == self.player:
            direction = False
            target = self.enemy
            effect = 0

            back1 = 1
            back2 = int((self.enemy.image.get_width()) / 2) / 60

            og_x = self.player_x
            og_x2 = self.enemy_x
        else:
            direction = True
            target = self.player
            effect = 1

            back1 = int((self.enemy.image.get_width()) / 2) / 60
            back2 = 1

            og_x = self.enemy_x
            og_x2 = self.player_x

        # [0] Back, [1] Charge, [2] Return, [3] Kickback, [4] Return
        scale = (self.enemy_x - self.player_x - self.player.image.get_width()) / 440
        speeds = [5 * back1, 16 * scale, 16 * scale, 8 * back2, 5 * scale]
        times = [0.3, 0.626, 0.75]
        # [0] Angry, [1] Hurt
        images = [12, 13]

        # Run through the rush animation with knock back
        if self.anim == 0:
            target.rush(1, images[0], speeds[4], False, og_x2)

            self.current_anim = None
            self.rolled_one()
        elif self.anim == 1:
            target.rush(3, images[1], speeds[3], direction)
            self.turn_player.rush(1, images[0], speeds[2], False, og_x)

            # Play crash SFX and activate particle effects
            handle_sound("shatter.mp3")
            self.effects.activate_effect(effect)

            self.anim_timer.activate(times[2])
        elif self.anim == 2:
            self.turn_player.rush(2, images[0], speeds[1], not direction, target)

            handle_sound("charge.mp3")

            self.anim_timer.activate(times[1])
        else:
            self.turn_player.rush(3, images[0], speeds[0], not direction)

            self.anim_timer.activate(times[0])
        self.anim -= 1

    def run_loot(self):
        """After the enemy dies, have the player run towards the spawned chest and pop up the rewards."""
        times = [1.5, 2, 1]
        if self.anim == 0:
            self.current_anim = None
            self.player.current_level = self.next_level
            self.to(self.destination)
            self.text_reward = ""
        elif self.anim == 1:
            # Move player to the right off screen
            self.player.command_move(7, 0, 850, self.player_y)

            self.anim_timer.activate(times[2])
        elif self.anim == 2:
            # Play sound and popup the notice
            handle_sound("good.mp3")

            self.text_reward = "You got {0} gold! {1}".format(self.enemy.money, self.player.level_up_text())

            self.anim_timer.activate(times[1])
        elif self.anim == 3:
            # Move the player towards the chest and move the enemy upwards to signify death
            self.player.command_move(7, 0, self.enemy_x - self.player.image.get_width(), self.player_y)
            self.enemy.command_move(0, 10, self.enemy.x, -300)
            self.enemy.image = self.enemy.images[14]

            # Spawn the chest
            self.canvas.add_element(StaticBG([load_img(load_c("chest.png"))],
                                             (self.enemy_x, self.player_y)), 5)

            # Give the player money
            self.player.money += self.enemy.money

            # Give the player experience
            self.player.exp += self.enemy.level

            self.anim_timer.activate(times[0])
        self.anim -= 1

    def run_dead(self):
        """After the player dies, move them up out of the screen and then go to the GameOver state."""
        if self.anim == 0:
            self.current_anim = None
            self.to("game_over")
        elif self.anim == 1:
            # Move player upwards
            self.player.command_move(0, 10, self.player_x, -300)
            self.player.image = self.player.images[14]

            self.anim_timer.activate(1.7)
        self.anim -= 1

    # STATE
    def set_next_level(self, next_level):
        """Sets the next stage the player will go to after this battle. Not to be confused with destination which is
           where the player will go to at the end of every battle."""
        self.next_level = next_level
