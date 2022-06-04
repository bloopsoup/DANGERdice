class Attributions(State):
    """First thing you see when you open the game. Basically a place to give credit to people."""

    def __init__(self):
        super().__init__()

        self.timer = DTimer(pygame.USEREVENT + 1)
        self.step = 0

        self.font = fonts[3]
        self.text = self.font.render("A BMB GAME", True, (255, 255, 255))

    def startup(self):
        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(StaticBG([load_img(load_s("black.png"))], (0, 0)), 0)
        self.canvas.add_element(StaticBG([load_img(load_c("badmc100x100.png"))], (350, 280)), 1)

        # Setup Player
        self.player.change_name("")
        self.player.direct_move(-100, -100)
        self.player.display_mode("")

        handle_sound("one.mp3")
        self.timer.activate(1.2)

    def handle_event(self, event):
        if event.type == self.timer.event:
            if self.step == 0:
                self.text = self.font.render("Inspired by TinyDiceDungeons", True, (255, 255, 255))
                self.canvas.delete_group(1)

                handle_sound("one.mp3")

                self.timer.activate(1.2)
                self.step += 1
            elif self.step == 1:
                self.to("main_menu")

    def update(self, surface, dt):
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)
        self.timer.update(dt)

        surface.blit(self.text, (self.center(self.text), 220))