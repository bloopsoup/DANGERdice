def rush(self, sequence, img, x_speed, right=False, mode=None):
    """Animates the rush animation for a character.
       1. Character moves backwards.
       2. Character rushes to the nearest enemy character.
       3. Character returns to original position.
       Note that mode can be either a target sprite or an og_x."""
    self.status(False)
    self.image = self.images[img]

    # Backing Up
    if sequence == 3:
        if right:
            self.command_move(x_speed, 0, int((self.x - self.image.get_width()) / 2), self.y)
        else:
            self.command_move(x_speed, 0, self.x + int((self.image.get_width()) / 2), self.y)
    # Charging towards the target sprite (but not intersecting it)
    elif sequence == 2:
        if right:
            self.command_move(x_speed, 0, mode.x - self.image.get_width(), self.y)
        else:
            self.command_move(x_speed, 0, mode.x + mode.image.get_width(), self.y)

    # Returning to original position
    else:
        self.command_move(x_speed, 0, mode, self.y)
