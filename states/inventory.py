class Inventory(State):
    """Where the player can change up their dice set and view their inventory of dice.
       Features pagination for better inventory management."""

    def __init__(self):
        super().__init__()

        # For selecting one of your dice
        self.selected = -1
        self.inv_selected = -1

        self.added_buttons = []
        self.reference_index = 0

        # Fonts
        self.font_small = fonts[1]
        self.font = fonts[2]

        self.info = ""

        self.text_info = self.font.render(self.info, True, (0, 0, 0))
        self.text_page = self.font.render("Page {0}".format((self.reference_index // 12) + 1), True, (0, 0, 0))
        self.text_amount = self.font_small.render("{0} Dice".format(len(self.player.inventory)), True, (0, 0, 0))
        self.text_money = self.font_small.render("{0} G".format(self.player.money), True, (0, 0, 0))

    def cleanup(self):
        self.selected = -1
        self.inv_selected = -1
        self.reference_index = 0

    def startup(self):
        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(MovingBackgroundElement([load_img(load_s("back3.png"))], (0, -1), (800, 600)), -1)
        self.canvas.add_element(StaticBG([load_img(load_s("inventory.png"))], (0, 0)), -1)

        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(0, 0, 3), (0, 0), BUTTON_DEFAULT,
                                     self.back), -1)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 0, 3), (730, 530), BUTTON_DEFAULT,
                                     handle_music), -1)

        placeholder = [load_img(load_b("hold_die.png")) for _ in range(3)]
        self.canvas.add_element(Butt(placeholder, (205, 75), BUTTON_GHOST, lambda: self.select_own(0)), -1)
        self.canvas.add_element(Butt(placeholder, (308, 75), BUTTON_GHOST, lambda: self.select_own(1)), -1)
        self.canvas.add_element(Butt(placeholder, (408, 75), BUTTON_GHOST, lambda: self.select_own(2)), -1)
        self.canvas.add_element(Butt(placeholder, (509, 75), BUTTON_GHOST, lambda: self.select_own(3)), -1)

        self.reset_buttons()

        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(2, 0, 3), (625, 530), BUTTON_DEFAULT,
                                     self.scroll_right), -1)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(0, 3, 3), (105, 530), BUTTON_DEFAULT,
                                     self.scroll_left), -1)

        # Setup Players
        self.player.direct_move(-100, -100)
        self.player.name_display(False)
        self.player.health_display(False)
        self.player.display_mode("")

    def handle_event(self, event):
        """We added a BACKSPACE event to cancel the player's selection."""
        self.canvas.handle_event(event)

        # Deselecting dice
        if event.type == pygame.KEYDOWN and (self.selected != -1 or self.inv_selected != -1):
            if event.key == pygame.K_BACKSPACE:
                self.deselect()

    def update(self, surface, dt):
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)

        # Draw the player's current dice
        self.draw_own_dice(surface, dt)

        # Draw the dice in the player's inventory
        self.draw_inventory_dice(surface, dt)

        # Displaying the Die Name
        self.text_info = self.font.render(self.info, True, (0, 0, 0))
        surface.blit(self.text_info, (0 + self.center(self.text_info), 10))

        # Page you are on
        self.text_page = self.font.render("Page {0}".format((self.reference_index // 12) + 1), True, (0, 0, 0))
        surface.blit(self.text_page, (self.center(self.text_page), 560))

        # Amount of dice you have in your inventory
        self.text_amount = self.font_small.render("{0} Dice".format(len(self.player.inventory)), True, (0, 0, 0))
        surface.blit(self.text_amount, (100, 100))

        # Displaying Money
        self.text_money = self.font_small.render("{0} G".format(self.player.money), True, (0, 0, 0))
        surface.blit(self.text_money, (610, 100))

    # Selection
    def select_own(self, i):
        """Select ith die from the set."""
        if len(self.player.dice_set) > i:
            self.inv_selected = -1
            self.selected = i
            self.info = "{0} (Sells for {1} gold)".format(self.player.dice_set[i].name,
                                                          self.player.dice_set[i].price // 3)

            self.current_button_remove()
            self.set_button_popup()

    def select_inventory(self, i):
        """Select ith die from the inventory."""
        self.selected = -1
        self.inv_selected = i
        self.info = "{0} (Sells for {1} gold)".format(self.player.inventory[i].name,
                                                      self.player.inventory[i].price // 3)
        self.current_button_remove()
        self.inventory_buttons_popup()

    def deselect(self):
        """Call when deselecting dice."""
        self.current_button_remove()
        self.selected = -1
        self.inv_selected = -1
        self.info = ""

    # Inventory Buttons
    def make_inventory_buttons(self):
        """Creates the buttons so we can interact with the inventory."""
        reference_x = [205, 305, 405, 505]
        reference_y = [270, 370, 470]
        placeholder = [load_img(load_b("hold_die.png")) for _ in range(3)]

        # Uses a (row, col) system for a 4 x 3 grid
        row, col = 0, 0
        for i in range(self.reference_index, len(self.player.inventory)):
            if col == 4:
                col = 0
                row += 1
            if row == 3:
                break

            def select_maker(x: int):
                def select():
                    return self.select_inventory(x)
                return select

            button = Butt(placeholder, (reference_x[col], reference_y[row]), BUTTON_GHOST,
                          select_maker(i))
            self.canvas.add_element(button, i)
            self.added_buttons.append(i)
            col += 1

    def delete_buttons(self):
        """Deletes the inventory buttons."""
        for i in self.added_buttons:
            self.canvas.delete_group(i)
        self.added_buttons.clear()

    def reset_buttons(self):
        """Just resets the die buttons."""
        self.delete_buttons()
        self.make_inventory_buttons()

    # Inventory Interactions
    def inventory_buttons_popup(self):
        """Make the inventory die buttons appear."""
        self.canvas.add_element(Butt(Control.sheets["button3"].load_some_images(0, 3, 3), (105, 200), BUTTON_DEFAULT,
                                self.delete_die), -2)
        self.canvas.add_element(Butt(Control.sheets["button3"].load_some_images(0, 0, 3), (105, 280), BUTTON_DEFAULT,
                                     self.equip_die), -3)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 3, 3), (105, 360), BUTTON_DEFAULT,
                                     self.deselect), -5)

    def set_button_popup(self):
        """Make the unequip button appear."""
        self.canvas.add_element(Butt(Control.sheets["button3"].load_some_images(2, 0, 3), (105, 200), BUTTON_DEFAULT,
                                     self.unequip_die), -4)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 3, 3), (105, 280), BUTTON_DEFAULT,
                                     self.deselect), -5)

    def current_button_remove(self):
        """Removes the current button(s)."""
        self.canvas.delete_group(-2)
        self.canvas.delete_group(-3)
        self.canvas.delete_group(-4)
        self.canvas.delete_group(-5)

    def delete_die(self):
        """Deletes the selected die where the player is compensated with 1/3 the price of the die.
           To be used with the buttons."""
        self.player.money += self.player.inventory.pop(self.inv_selected).price // 3
        self.current_button_remove()
        self.reset_buttons()

        # If we remove all die from a screen, goes back to the previous screen
        if len(self.player.inventory) <= self.reference_index:
            self.scroll_left()

        self.selected = -1
        self.inv_selected = -1
        self.info = ""

    def equip_die(self):
        """Equips the selected die. To be used with the buttons."""
        if len(self.player.dice_set) < 4:
            self.player.dice_set.append(self.player.inventory.pop(self.inv_selected))
            self.current_button_remove()
            self.reset_buttons()

            # If we remove all die from a screen, goes back to the previous screen
            if len(self.player.inventory) <= self.reference_index:
                self.scroll_left()

            self.selected = -1
            self.inv_selected = -1
            self.info = ""

    def unequip_die(self):
        """Unequips the selected die. To be used with the buttons."""
        if len(self.player.dice_set) > 1 and self.selected != 0:
            self.player.inventory.append(self.player.dice_set.pop(self.selected))
            self.current_button_remove()
            self.reset_buttons()

            # If the added die goes to a new screen, move to it
            if len(self.player.inventory) > self.reference_index:
                self.scroll_right()

            self.selected = -1
            self.inv_selected = -1
            self.info = ""

    # Pagination
    def scroll_left(self):
        """Scroll to the left to go back a page."""
        if self.reference_index > 0:
            self.reference_index -= 12
            self.reset_buttons()

    def scroll_right(self):
        """Scroll to the right to reveal more dice from your inventory."""
        if len(self.player.inventory) > self.reference_index + 12:
            self.reference_index += 12
            self.reset_buttons()

    # Displays
    def draw_own_dice(self, surface, dt):
        """Draws your dice set."""
        reference_x = [205, 308, 408, 509]
        reference_y = 75

        for i in range(len(self.player.dice_set)):
            # Animate if selected
            if self.selected == i:
                self.player.dice_set[i].status(True)
            else:
                self.player.dice_set[i].status(False)

            self.player.dice_set[i].direct_move(reference_x[i], reference_y)
            self.player.dice_set[i].update(surface, dt)

    def draw_inventory_dice(self, surface, dt):
        """Draws the inventory dice."""
        reference_x = [205, 305, 405, 505]
        reference_y = [270, 370, 470]

        # Uses a (row, col) system for a 4 x 3 grid
        row = 0
        col = 0
        for i in range(self.reference_index, len(self.player.inventory)):
            if col == 4:
                col = 0
                row += 1
            if row == 3:
                break

            # Animate if selected
            if self.inv_selected == i:
                self.player.inventory[i].status(True)
            else:
                self.player.inventory[i].status(False)

            self.player.inventory[i].direct_move(reference_x[col], reference_y[row])
            self.player.inventory[i].update(surface, dt)
            col += 1