def display_mode(self, mode):
    """Set dice display mode."""
    self.mode = mode


def show_dice_set(self, surface, dt):
    """Displaying your set of dice. Note that the parameters provided are linked to a png already made.
       There are modes to do so.
       menu -- When in the player menu.
       player -- When it's the player's turn.
       enemy -- When it's the enemy's turn."""

    # Manually set the dimensions if we change it later
    # This is the size of the hub dice elements
    x_size = 100
    y_size = 100
    # Stroke (if applicable)
    stroke = 1

    if self.mode == "menu":
        # Location
        reference_y = 72
        reference_x = 369
        active = False
    elif self.mode == "player":
        # Location
        reference_y = 455
        reference_x = 369
        active = True
    elif self.mode == "enemy":
        # location
        reference_y = 455
        reference_x = 33
        active = True
    else:
        return

    current = 0
    for die in self.dice_set:
        # Check for already rolled die
        if not die.rolled:
            die.status(active)
        else:
            die.status(False)

        # Does the math for adding additional dice to the hub
        x_center = int((x_size - die.image.get_width()) / 2)
        y_center = int((y_size - die.image.get_height()) / 2)
        die.direct_move(reference_x + x_center + current, reference_y + y_center)
        current += die.image.get_width() + (2 * x_center) + stroke

    for die in self.dice_set:
        die.update(surface, dt)


def show_info(self, surface):
    """Displays the info. Kept it separate from the set to make it easier to manage."""
    if self.mode == "menu":
        # Location
        reference_y = 72
        reference_x = 145
    elif self.mode == "player":
        reference_y = 460
        reference_x = 38
    elif self.mode == "enemy":
        reference_y = 460
        reference_x = 450
    else:
        return

    self.text_name = self.font.render(self.name, True, (0, 0, 0))
    self.text_level = self.font.render("LVL: {0}".format(self.level), True, (0, 0, 0))
    self.text_health = self.font.render("HP: {0} / {1}".format(self.current, self.health), True, (0, 0, 0))
    self.text_money = self.font.render("Gold: {0}".format(self.money), True, (0, 0, 0))

    surface.blit(self.text_name, (reference_x, reference_y))
    surface.blit(self.text_level, (reference_x, reference_y + self.text_name.get_height()))
    surface.blit(self.text_health, (reference_x, reference_y + (2 * self.text_name.get_height())))
    surface.blit(self.text_money, (reference_x, reference_y + (3 * self.text_name.get_height())))

    def find_center(self, text_surface: pygame.Surface) -> int:
        """Returns the width to use in order to center text with respect to the entity."""
        return int((self.image.get_width() - text_surface.get_width()) / 2)

    def change_name(self, name: str):
        """Change the player's name."""
        self.name = name

    def display_name(self, show: bool):
        """Whether to display the name."""
        self.show_name = show

    def display_health(self, show: bool):
        """Whether to display the health."""
        self.show_hp = show

    def display_all_text(self, surface: pygame.Surface):
        """Displays all entity-related text on the surface."""
        if self.show_name:
            ts = self.font.render(self.name, True, (0, 0, 0))
            surface.blit(ts, (self.pos.x + self.find_center(ts), self.pos.y - ts.get_height() - 5))
        if self.show_hp:
            ts = self.font.render("{0} / {1}".format(self.health, self.max_health), True, (0, 0, 0))
            surface.blit(ts, (self.pos.x + self.find_center(ts), self.pos.y - ts.get_height() - 25))
        if self.poison > 0:
            ts = self.font.render("PSN: {0}".format(self.poison), True, (84, 22, 180))
            surface.blit(ts, (self.pos.x + self.find_center(ts), self.pos.y - ts.get_height() - 45))
        if self.divided > 1:
            ts = self.font.render("WEAKENED {0}X".format(self.divided), True, (0, 0, 0))
            surface.blit(ts, (self.pos.x + self.find_center(ts), self.pos.y - ts.get_height() - 65))