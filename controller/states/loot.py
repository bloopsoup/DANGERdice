class Loot(State):
    """A screen that can show up if the player has won a die from the previous battle."""
    tier = [
        ["basic1", "basic1", "basic1", "basic1", "basic1", "basic2", "poison1", "poison1"],
        ["basic1", "basic1", "basic1", "basic1", "basic2", "poison1", "poison1", "poison2", "heal1"],
        ["basic1", "basic1", "basic1", "basic1", "basic2", "basic2", "basic3", "poison1", "poison1", "poison2"],
        ["basic1", "basic1", "basic2", "basic2", "basic2", "basic3", "basic3", "poison1", "poison1", "poison2",
         "multiplier1", "divider1"],
        ["basic2", "basic2", "basic3", "basic3", "basic3", "basic4", "basic4", "basic5", "poison1", "poison1",
         "poison2", "poison3", "multiplier2", "divider3"],
        ["basic5"]
    ]

    storage = {}
    for i in range(6):
        for j in range(4):
            storage["p{0}-{1}".format(i, j)] = tier[i]
            storage["l{0}-{1}".format(i, j)] = tier[i]

    def __init__(self):
        super().__init__()

        self.timer = DTimer(pygame.USEREVENT + 1)
        self.step = 0

        self.font = fonts[3]
        self.text = self.font.render("", True, (0, 0, 0))

        self.dice_name = ""

        self.player_x = 300
        self.player_y = 257

    def cleanup(self):
        self.step = 0
        self.text = self.font.render("", True, (0, 0, 0))
        self.dice_name = ""

    def startup(self):
        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(StaticBG([load_img(load_s("land2.png"))], (0, 0)), 0)
        self.canvas.add_element(StaticBG([load_img(load_s("ground0.png"))], (0, 0)), 0)

        # Setup Player
        self.player.direct_move(-300, self.player_y)
        self.player.command_move(10, 0, self.player_x, self.player_y)
        self.player.name_display(False)
        self.player.display_mode("")

        # Prepare the loot
        self.give_loot()

        self.timer.activate(1.5)

    def handle_event(self, event):
        if event.type == self.timer.event:
            if self.step == 0:
                handle_sound("good.mp3")
                self.text = self.font.render("You got {0}!".format(self.dice_name), True, (0, 0, 0))
                self.timer.activate(2)
                self.step += 1
            elif self.step == 1:
                self.to("player_menu")

    def update(self, surface, dt):
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)
        self.timer.update(dt)

        surface.blit(self.text, (self.center(self.text), 100))

    # Function
    def give_loot(self):
        """Gives the player the loot. Randomly."""
        if self.player.current_level in self.storage:
            die = State.gen_dice(random.choice(self.storage[self.player.current_level]))
        else:
            die = State.gen_dice("basic1")

        self.dice_name = die.name
        self.player.inventory.append(die)