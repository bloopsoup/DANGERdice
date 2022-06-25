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