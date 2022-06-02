class Shop(State):
    """Where the player can purchase dice. Dice are added directly to the inventory."""
    tier = [
        [["basic2", "poison1", "heal1"], False],
        [["basic2", "poison1", "heal2"], False],
        [["basic3", "poison2", "basic2"], False],
        [["basic3", "divider2", "multiplier1"], False],
        [["basic4", "basic5", "multiplier2"], False],
        [["basic5", "heal3", "multiplier3"], False]
    ]

    storage = {}
    for i in range(6):
        for j in range(4):
            storage["p{0}-{1}".format(i, j)] = tier[i]
            storage["l{0}-{1}".format(i, j)] = tier[i]

    inventory = []

    def __init__(self):
        super().__init__()

        # For flashing notices on screen such as BOUGHT
        self.flash_timer = DTimer(pygame.USEREVENT + 2)
        self.flash = 0

        # For selecting an option
        self.selected = -1

        # Shopkeeper for looks
        self.keeper = State.gen_enemy("shopkeeper", 0)

        # Fonts
        self.font = fonts[2]
        self.font_small = fonts[1]

        self.info = ""
        self.help = "Click on a Die you wish to purchase."

        self.text_info = self.font.render(self.info, True, (0, 0, 0))
        self.text_money = self.font.render("Gold: {0}".format(self.player.money), True, (0, 0, 0))
        self.text_help = self.font_small.render(self.help, True, (0, 0, 0))

    def cleanup(self):
        self.menu = None
        self.canvas = None

        self.selected = -1
        self.info = ""

    def startup(self):
        # Setup Menu
        self.menu = SimpleMenu(20, 250, 265)
        self.menu.add_widget(70, 70, Control.sheets["button"].load_some_images(0, 0, 3), True, self.back, 0, Button,
                             (0, 0))
        self.menu.add_widget(70, 70, Control.sheets["button"].load_some_images(1, 0, 3), True, handle_music, 0,
                             Button, (730, 530))

        placeholder = [load_b("hold_die.png") for _ in range(3)]
        self.menu.add_button_special(85, 85, placeholder, False, self.select, 0, 0, (104, 290))
        self.menu.add_button_special(85, 85, placeholder, False, self.select, 0, 1, (356, 290))
        self.menu.add_button_special(85, 85, placeholder, False, self.select, 0, 2, (611, 290))

        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(MovingBackgroundElement([load_img(load_s("back3.png"))], (0, -1), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_img(load_s("shop.png"))], (0, 0)), 0)

        # Setup Players
        self.player.direct_move(-100, -100)
        self.player.name_display(False)
        self.player.health_display(False)
        self.player.display_mode("")

        self.keeper.direct_move(650, 420)
        self.keeper.name_display(False)
        self.keeper.health_display(False)
        self.keeper.display_mode("")

        self.restock()

    def handle_event(self, event):
        """In addition to menu events, added button events for buying and deselecting dice."""
        self.menu.handle_event(event)

        # Buying and dice
        if event.type == pygame.KEYDOWN and self.selected != -1:
            # For purchasing
            if event.key == pygame.K_RETURN:
                self.buy()
            # For backing out
            if event.key == pygame.K_BACKSPACE:
                self.deselect()

        # Flash timers
        if event.type == self.flash_timer.event:
            self.canvas.delete_group(self.flash)
            self.flash = 0

    def update(self, surface, dt):
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)
        self.keeper.update(surface, dt)
        self.menu.update(surface, dt)
        self.flash_timer.update(dt)

        # Draw the dice
        self.draw_shop_dice(surface, dt)

        # Display info when selected

        # Displaying the Die Name
        self.text_info = self.font.render(self.info, True, (0, 0, 0))
        surface.blit(self.text_info, (self.center(self.text_info), 476))

        # Instructing player on what to do after selecting die
        if self.flash == 0:
            if self.selected == -1:
                surface.blit(self.text_help, (10, 544))

        # Displaying the player's money
        self.text_money = self.font.render("Gold: {0}".format(self.player.money), True, (0, 0, 0))
        surface.blit(self.text_money, (100, 170))

    # Shop-Related Functions

    @staticmethod
    def refill():
        """Refreshes the shop's storage. To be used when the player dies and wants to come back again."""
        for t in Shop.tier:
            t[1] = False

    def restock(self):
        """Refreshes the shop's inventory. To be called upon setup when certain conditions are met such as
           re-entering a shop."""
        if self.player.current_level in self.storage:
            if not self.storage[self.player.current_level][1]:
                self.storage[self.player.current_level][1] = True
                Shop.inventory = [State.gen_dice(i) for i in self.storage[self.player.current_level][0]]
        else:
            Shop.inventory = [None, None, None]

    def select(self, i):
        """Select a die."""
        if Shop.inventory[i] is not None:
            self.selected = i
            self.info = "{0} costing {1} gold.".format(Shop.inventory[i].name, Shop.inventory[i].price)

            self.current_button_remove()
            self.shop_buttons_popup()

    def buy(self):
        """Purchases the selected die."""
        # If you have enough money or not
        if Shop.inventory[self.selected].price <= self.player.money:
            self.player.money -= Shop.inventory[self.selected].price
            self.player.inventory.append(Shop.inventory[self.selected])
            Shop.inventory[self.selected] = None

            self.popup_bought()
            handle_sound("roll.mp3")
        else:
            self.popup_broke()
            handle_sound("one.mp3")

        self.selected = -1
        self.info = ""
        self.current_button_remove()

    def deselect(self):
        """Deselects the current die."""
        self.selected = -1
        self.info = ""
        self.current_button_remove()

    # Buttons
    def shop_buttons_popup(self):
        """Make the shop buttons appear."""
        self.menu.add_widget(70, 70, Control.sheets["button"].load_some_images(2, 3, 3), True, self.buy, -2,
                             Button, (320, 525))
        self.menu.add_widget(70, 70, Control.sheets["button"].load_some_images(1, 3, 3), True, self.deselect, -3,
                             Button, (410, 525))
        self.remove_popups()

    def current_button_remove(self):
        """Removes the current button(s)."""
        if self.menu.check_id(-2):
            self.menu.delete_widget(-2)
        if self.menu.check_id(-3):
            self.menu.delete_widget(-3)

    # Displays
    def draw_shop_dice(self, surface, dt):
        """Draws the shop dice."""
        reference_x = [104, 356, 611]
        reference_y = 290

        for i in range(len(Shop.inventory)):
            if Shop.inventory[i] is not None:
                # Animate the die if selected
                if self.selected == i:
                    Shop.inventory[i].status(True)
                else:
                    Shop.inventory[i].status(False)

                Shop.inventory[i].direct_move(reference_x[i], reference_y)
                Shop.inventory[i].update(surface, dt)

    def remove_popups(self):
        """Remove the current popups."""
        if self.canvas.group_exists(1):
            self.canvas.delete_group(1)
        if self.canvas.group_exists(2):
            self.canvas.delete_group(2)

    def popup_bought(self):
        """Pop up the bought display."""
        self.remove_popups()

        self.canvas.add_element(StaticBG([load_img(load_s("bought.png"))], (0, 130)), 1)
        self.flash_timer.activate(0.5)
        self.flash = 1

    def popup_broke(self):
        """Pop up the broke display."""
        self.remove_popups()

        self.canvas.add_element(StaticBG([load_img(load_s("broke.png"))], (0, 0)), 2)
        self.flash_timer.activate(0.5)
        self.flash = 2

    # Data
    @staticmethod
    def package_data():
        """Returns shop data for saving purposes. Format is [inventory, restocked]."""
        return [[die.ID if die else None for die in Shop.inventory], [i[1] for i in Shop.tier]]

    @staticmethod
    def load_data(data):
        """Loads data for shops."""
        Shop.inventory = [State.gen_dice(die) if die else None for die in data[0]]
        for i in range(len(data[1])):
            Shop.tier[i][1] = data[1][i]