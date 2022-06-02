from base import *

from gui.canvas.Themes import *
from gui.canvas.Canvas import Canvas
from gui.canvas.elements.StaticBG import StaticBG
from gui.canvas.elements.MovingBG import MovingBackgroundElement
from gui.canvas.elements.Button import Button as Butt
from gui.canvas.elements.InputText import InputText as InputT
from gui.canvas.elements.DialogueBox import DialogueData as DData
from gui.canvas.elements.DialogueBox import DialogueBox as DBox

from effects import *
from menu import *
from utils import *
from dtimer import *
from spritesheet import *

pygame.init()


# CONTROL
class Control:
    """Controls the game. Sets up settings and your starting state. Your controller will
       manage one state at a time where it will switch out states when prompted. This allows us to keep
       using one main game loop, greatly simplifying things.

       Courtesy of @metulburr's tutorial."""

    # Modifiable and accessible attributes
    sheets = None
    states = None
    state_data = None

    def __init__(self, start):
        self.DONE = False

        # Set resolution
        self.screen_width = 800
        self.screen_height = 600
        self.surface = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Set icon
        pygame.display.set_icon(pygame.image.load(rp("assets/icon.png")))
        pygame.display.set_caption("DANGERdice")

        # Set frames
        self.fps = 60
        self.clock = pygame.time.Clock()

        # Set keys
        pygame.key.set_repeat(500, 100)

        # Setup sprite sheets and players
        Control.sheets = {"mc": Spritesheet(load_c("mc100x3x5.png"), 100, 100, 3, 5),
                          "aaron": Spritesheet(load_c("ah120x3x5.png"), 120, 120, 3, 5),
                          "dorita": Spritesheet(load_c("dorita130x5x8.png"), 130, 130, 5, 8),
                          "wally": Spritesheet(load_c("whale200x250x5x5.png"), 200, 250, 5, 5),
                          "duck": Spritesheet(load_c("duck180x150x5x5.png"), 180, 150, 5, 5),
                          "migahexx.xml": Spritesheet(load_c("mik3x5x220x220.png"), 220, 220, 3, 5),
                          "shop": Spritesheet(load_c("shop45x3x5.png"), 45, 45, 3, 5),
                          "dice1": Spritesheet(load_c("1dice85x6x6.png"), 85, 85, 6, 6),
                          "dice2": Spritesheet(load_c("2dice85x6x6.png"), 85, 85, 6, 6),
                          "dice3": Spritesheet(load_c("3dice85x6x6.png"), 85, 85, 6, 6),
                          "ria": Spritesheet(load_c("ria140x3x5.png"), 140, 140, 3, 5),
                          "bursa": Spritesheet(load_c("bursa85x120x3x5.png"), 85, 120, 3, 5),
                          "wandre": Spritesheet(load_c("wandre100x160x3x5.png"), 100, 160, 3, 5),
                          "cena": Spritesheet(load_c("cena190x100x3x5.png"), 190, 100, 3, 5),
                          "sosh": Spritesheet(load_c("sosh70x140x3x5.png"), 70, 140, 3, 5),
                          "arca": Spritesheet(load_c("arca160x110x3x5.png"), 160, 110, 3, 5),
                          "ellie": Spritesheet(load_c("ellie100x3x5.png"), 100, 100, 3, 5),
                          "kiran": Spritesheet(load_c("kiran150x3x5.png"), 150, 150, 3, 5),
                          "connor": Spritesheet(load_c("connor85x100x3x5.png"), 85, 100, 3, 5),
                          "baggins": Spritesheet(load_c("baggins110x3x5.png"), 110, 110, 3, 5),
                          "portrait1": Spritesheet(load_c("chat100x3x6.png"), 100, 100, 2, 6),
                          "button": Spritesheet(load_b("1button70x3x6.png"), 70, 70, 3, 6),
                          "button2": Spritesheet(load_b("2button75x500x6x3.png"), 75, 500, 6, 3),
                          "button3": Spritesheet(load_b("3button70x3x6.png"), 70, 70, 3, 6),
                          "button4": Spritesheet(load_b("4button50x200x2x3.png"), 50, 200, 2, 3)
                          }
        State.init_player()

        # Setup beginning states
        Control.states = {"main_menu": MainMenu(),
                          "attributions": Attributions(),
                          "load": Load(),
                          "loot": Loot(),
                          "save": Save(),
                          "intro": Intro(),
                          "player_menu": PlayerMenu(),
                          "inventory": Inventory(),
                          "game_over": GameOver(),
                          "ending": Ending()
                          }

        self.state_name = start
        self.state = self.states[self.state_name]

        self.state.startup()

    def to_state(self):
        """The game will move to another state. Pretty much akin to linked-list hacks."""
        # Leaving current state
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state.cleanup()

        # Moving onto the next
        self.state = self.states[self.state_name]
        self.state.startup()
        self.state.previous = previous

    def update(self, dt):
        """Moves to another state when prompted. Then, update your screen."""
        # If I want to quit the actual game
        if self.state.quit:
            self.DONE = True
        # If my state is quitting
        elif self.state.done:
            self.to_state()
        # Make the screen beautiful again
        self.state.update(self.surface, dt)
        # self.display_fps()

    def event_loop(self):
        """Processes events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.DONE = True
            self.state.handle_event(event)

    def main_loop(self):
        """Where the game takes place."""
        while not self.DONE:
            dt = self.clock.tick(self.fps) / 1000
            # Lag checker
            if dt >= 0.05:
                continue
            self.event_loop()
            self.update(dt)
            pygame.display.update()

    @staticmethod
    def generate_states():
        """Generates the levels/preambles and adds them to self.states.
           Levels are grouped into stages where a stage dictates the tier of the generated enemy.
           Each stage ends with a boss fight. Sometimes after a level, you can get extra die loot."""

        enemies = ["aaron", "bursa", "cena", "dorita", "duck", "square", "wandre", "baggins", "arca", "ellie"]
        bosses = ["wally", "ria", "connor", "sosh"]

        number_of_levels = [4, 4, 4, 4, 4, 1]
        previous = None

        state_data = []

        for i in range(6):
            tmp = enemies[:]
            tmp2 = bosses[:]
            for j in range(number_of_levels[i]):
                if j == 0 and i == 0:
                    chosen = "aaron"
                    tmp.remove(chosen)
                    enemy = State.gen_enemy("aaron", i)
                    has_preamble = True
                    has_loot = "player_menu"
                elif j == number_of_levels[i] - 1:
                    has_preamble = True
                    if i == 5:
                        chosen = "kiran"
                    else:
                        chosen = random.choice(tmp2)
                        tmp2.remove(chosen)

                    enemy = State.gen_enemy(chosen, i)
                    has_loot = "loot"
                else:
                    chosen = random.choice(tmp)
                    tmp.remove(chosen)
                    enemy = State.gen_enemy(chosen, i)
                    has_preamble = bool(enemy.preamble and not random.randint(0, 2))
                    has_loot = random.choice(["loot", "player_menu", "player_menu", "player_menu"])

                state_data.append([chosen, has_preamble, has_loot, i, j])
                print([chosen, has_preamble, has_loot, i, j])

                # Linking the previous level to the next level
                prefix = "p" if has_preamble else "l"
                if previous:
                    previous.next_level = "{0}{1}-{2}".format(prefix, i, j)

                # Level Creation
                if has_preamble:
                    Control.states["p{0}-{1}".format(i, j)] = Preamble(enemy, i, "l{0}-{1}".format(i, j))
                if j == 0 and i == 0:
                    pass
                else:
                    previous = Battle(enemy, i, has_loot)
                Control.states["l{0}-{1}".format(i, j)] = previous
        Control.state_data = state_data

    @staticmethod
    def load_generated_states(state_data):
        """Reloads the levels using the state_data information. Format is as follows:
           [chosen, has_preamble, has_loot, i, j]"""

        previous = None
        for level in state_data:
            enemy = State.gen_enemy(level[0], level[3])
            has_preamble = level[1]
            has_loot = level[2]

            # Linking the previous level to the next level
            prefix = "p" if has_preamble else "l"
            if previous:
                previous.next_level = "{0}{1}-{2}".format(prefix, level[3], level[4])

            # Level Creation
            if has_preamble:
                Control.states["p{0}-{1}".format(level[3], level[4])] = Preamble(enemy, level[3],
                                                                                 "l{0}-{1}".format(level[3], level[4]))
            if level[3] == 0 and level[4] == 0:
                pass
            else:
                previous = Battle(enemy, level[3], has_loot)
            Control.states["l{0}-{1}".format(level[3], level[4])] = previous
        Control.state_data = state_data

    def display_fps(self):
        """For debugging purposes. Just displays the FPS at the center bottom of the screen."""
        self.surface.blit(fonts[0].render("FPS: " + str(int(self.clock.get_fps())), True, (0, 0, 0)), (365, 580))


# GAME STATES
class State:
    """A state abstract class. Persisting information goes here.
       done -- Boolean -- Indicates whether you are leaving a state or not.
       quit -- Boolean -- Indicates whether to quit the game.
       next -- String -- Indicates the next state you will go to.
       previous -- String -- The state you came from."""

    def __init__(self):
        self.done = False
        self.next = None
        self.previous = None

        self.menu = None
        self.canvas = None
        self.effects = None

    def cleanup(self):
        """Cleaning up components before leaving the state. This is not always necessary."""
        pass

    def startup(self):
        """Stuff to do when entering a state, such as loading songs or images."""
        raise NotImplementedError

    def handle_event(self, event):
        """Handles events in this state."""
        self.canvas.handle_event(event)

        self.menu.handle_event(event)

    def update(self, surface, dt):
        """Draws stuff pertaining to this state. Generally, menu options should be on top."""
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)
        self.menu.update(surface, dt)

    def to(self, to):
        """Goes to the target state."""
        self.next = to
        self.done = True

    def back(self):
        """Goes back to the previous state."""
        self.to(self.previous)

    # STATIC STUFF

    # Catalogs
    dice_catalog = {"basic1": 'Die(Control.sheets["dice1"].load_some_images(0, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 1, '
                              '"basic1")',
                    "basic2": 'Die(Control.sheets["dice1"].load_some_images(1, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 2, '
                              '"basic2")',
                    "basic3": 'Die(Control.sheets["dice1"].load_some_images(2, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 3, '
                              '"basic3")',
                    "basic4": 'Die(Control.sheets["dice1"].load_some_images(3, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 4, '
                              '"basic4")',
                    "basic5": 'Die(Control.sheets["dice1"].load_some_images(4, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 5, '
                              '"basic5")',
                    "poison1": 'Poison(Control.sheets["dice1"].load_some_images(5, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 1, '
                               '"poison1")',
                    "poison2": 'Poison(Control.sheets["dice2"].load_some_images(0, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 2, '
                               '"poison2")',
                    "poison3": 'Poison(Control.sheets["dice2"].load_some_images(1, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 3, '
                               '"poison3")',
                    "heal1": 'Heal(Control.sheets["dice2"].load_some_images(2, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 1, '
                             '"heal1")',
                    "heal2": 'Heal(Control.sheets["dice2"].load_some_images(3, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 2, '
                             '"heal2")',
                    "heal3": 'Heal(Control.sheets["dice2"].load_some_images(4, 0, 6), 0, 0, [1, 2, 3, 4, 5, 6], 3, '
                             '"heal3")',
                    "divider1": 'Divider(Control.sheets["dice3"].load_some_images(0, 0, 6), 0, 0, [1, 1, 1, 1, 2, 2], '
                                '1, "divider1", "")',
                    "divider2": 'Divider(Control.sheets["dice3"].load_some_images(1, 0, 6), 0, 0, [1, 1, 1, 2, 2, 2], '
                                '1, "divider2", "+")',
                    "divider3": 'Divider(Control.sheets["dice3"].load_some_images(2, 0, 6), 0, 0, [1, 1, 2, 2, 2, 3], '
                                '1, "divider3", "++")',
                    "multiplier1": 'Multiplier(Control.sheets["dice3"].load_some_images(3, 0, 6), 0, 0, [1, 1, 1, 1, '
                                   '2, 2], 1, "multiplier1", "")',
                    "multiplier2": 'Multiplier(Control.sheets["dice3"].load_some_images(4, 0, 6), 0, 0, [1, 1, 1, 2, '
                                   '2, 2], 1, "multiplier2", "+")',
                    "multiplier3": 'Multiplier(Control.sheets["dice3"].load_some_images(5, 0, 6), 0, 0, [1, 1, 2, 2, '
                                   '2, 3], 1, "multiplier3", "++")'
                    }

    enemy_catalog = {"player": 'Player(Control.sheets["mc"].load_all_images(), -100, -100)',
                     "aaron": 'Aaron(Control.sheets["aaron"].load_all_images(), -150, -150)',
                     "dorita": 'Dorita(Control.sheets["dorita"].load_all_images(), -150, -150)',
                     "shopkeeper": 'Shopkeeper(Control.sheets["shop"].load_all_images(), -150, -150)',
                     "wally": 'Wally(Control.sheets["wally"].load_all_images(), -300, -300)',
                     "square": 'GSquare(Control.sheets["dice1"].load_some_images(0, 0, 15), -100, -100)',
                     "duck": 'BadDuck(Control.sheets["duck"].load_all_images(), -300, -300)',
                     "michael": 'Michael(Control.sheets["migahexx.xml"].load_all_images(), -300, -300)',
                     "ria": 'Ria(Control.sheets["ria"].load_all_images(), -300, -300)',
                     "wandre": 'Wandre(Control.sheets["wandre"].load_all_images(), -300, -300)',
                     "cena": 'Cena(Control.sheets["cena"].load_all_images(), -300, -300)',
                     "bursa": 'Bursa(Control.sheets["bursa"].load_all_images(), -300, -300)',
                     "sosh": 'Sosh(Control.sheets["sosh"].load_all_images(), -300, -300)',
                     "arca": 'Arca(Control.sheets["arca"].load_all_images(), -300, -300)',
                     "ellie": 'Ellie(Control.sheets["ellie"].load_all_images(), -300, -300)',
                     "kiran": 'Kiran(Control.sheets["kiran"].load_all_images(), -300, -300)',
                     "connor": 'Connor(Control.sheets["connor"].load_all_images(), -300, -300)',
                     "baggins": 'Baggins(Control.sheets["baggins"].load_all_images(), -300, -300)'}

    # Note that player is a 100px x 100px png
    player = None
    quit = False

    @staticmethod
    def gen_enemy(key, tier):
        """Creates a new enemy object from enemy_catalog."""
        assert key in State.enemy_catalog
        enemy = eval(State.enemy_catalog[key])
        enemy.set_stats(tier)
        return enemy

    @staticmethod
    def gen_dice(key):
        """Creates a new die object from the dice_catalog."""
        assert key in State.dice_catalog
        return eval(State.dice_catalog[key])

    @staticmethod
    def init_player():
        """Initialize the player. A guy with only two basic dice."""
        State.player = State.gen_enemy("player", 0)
        State.player.dice_set = [State.gen_dice("basic5"), State.gen_dice("basic1")]
        State.player.inventory = [State.gen_dice("basic1") for _ in range(40)]

    @staticmethod
    def center(text_surface):
        """Given a surface, finds the horizontal center accounting for its width."""
        return int((800 - text_surface.get_width()) / 2)

    @staticmethod
    def v_center(text_surface):
        """Given a surface, finds the vertical center according to height."""
        return int((600 - text_surface.get_height()) / 2)

    @staticmethod
    def quit_game():
        """Quits the game."""
        State.quit = True


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


class Ending(State):
    """The ending sequence."""

    def __init__(self):
        super().__init__()

        self.timer = DTimer(pygame.USEREVENT + 1)
        self.step = 0

        self.font = fonts[3]
        self.text = self.font.render("AND AFTER THAT FIGHT", True, (255, 255, 255))

    def cleanup(self):
        self.player.stop_move()

    def startup(self):
        pygame.mixer.music.stop()

        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(StaticBG([load_img(load_s("black.png"))], (0, 0)), 0)

        # Setup Player
        self.player.change_name("")
        self.player.direct_move(-100, 472)
        self.player.display_mode("")
        self.player.command_move(5, 0, 1000, 472)

        handle_sound("one.mp3")
        self.timer.activate(2)

    def handle_event(self, event):
        if event.type == self.timer.event:
            if self.step == 0:
                self.text = self.font.render("YOU FOUND A LOT OF MONEY", True, (255, 255, 255))

                handle_sound("one.mp3")

                self.timer.activate(1.5)
                self.step += 1
            elif self.step == 1:
                self.text = self.font.render("IN THE MOUNTAINS", True, (255, 255, 255))

                handle_sound("one.mp3")

                self.timer.activate(2)
                self.step += 1
            elif self.step == 2:
                self.text = self.font.render("DEBTS HAVE BEEN REPAID", True, (255, 255, 255))

                handle_sound("one.mp3")

                self.timer.activate(1.5)
                self.step += 1
            elif self.step == 3:
                self.text = self.font.render("HAPPY END", True, (255, 255, 255))

                handle_sound("one.mp3")

                self.timer.activate(1.5)
                self.step += 1
            else:
                self.return_menu()

    def update(self, surface, dt):
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)
        self.timer.update(dt)

        surface.blit(self.text, (self.center(self.text), 220))

    def return_menu(self):
        """Goes back to the main menu. Resets the player since they beat the game!"""
        self.player.reset_player()
        self.player.dice_set = [State.gen_dice("basic1"), State.gen_dice("basic1")]
        self.to("main_menu")


class Load(State):
    """A load confirmation screen since people might want a warning before
       loading data that can override their current session."""

    def __init__(self):
        super().__init__()

        self.font = fonts[3]
        self.text = self.font.render("Load saved data?", True, (0, 0, 0))

    def startup(self):
        # Setup menu itself
        self.menu = SimpleMenu(15, 275, 400)

        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(StaticBG([load_img(load_s("placeholderbg.png"))], (0, 0)), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(2, 3, 3), (320, 280), BUTTON_DEFAULT,
                                     self.load_data), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 3, 3), (410, 280), BUTTON_DEFAULT,
                                     self.back), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 0, 3), (730, 530), BUTTON_DEFAULT,
                                     handle_music), 0)

        # Setup Player
        self.player.direct_move(-100, -100)
        self.player.display_mode("")

    def update(self, surface, dt):
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)
        self.menu.update(surface, dt)

        surface.blit(self.text, (self.center(self.text), 220))

    # Function
    def load_data(self):
        """Loads player save data. If there is no data, does nothing."""
        data = load_data("player_data")
        if data:
            # Loading player
            p_data = data[0]
            self.player.level = p_data[0]
            self.player.current = p_data[1]
            self.player.health = p_data[2]
            self.player.money = p_data[3]
            self.player.dice_set = [State.gen_dice(i) for i in p_data[4]]
            self.player.inventory = [State.gen_dice(i) for i in p_data[5]]
            self.player.current_level = p_data[6]
            self.player.exp = p_data[7]
            self.player.name = p_data[8]

            # Loading states
            s_data = data[1]
            Control.load_generated_states(s_data)

            # shop_data = data[2]
            # Shop.load_data(shop_data)

            self.to("player_menu")


class Save(State):
    """A save confirmation screen since people might want a warning before overwriting their current save."""

    def __init__(self):
        super().__init__()

        self.font = fonts[3]
        self.text = self.font.render("Save current data?", True, (0, 0, 0))

    def startup(self):
        # Setup menu itself
        self.menu = SimpleMenu(15, 275, 400)

        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(StaticBG([load_img(load_s("placeholderbg.png"))], (0, 0)), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(2, 3, 3), (320, 280), BUTTON_DEFAULT,
                                     self.save_data), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 3, 3), (410, 280), BUTTON_DEFAULT,
                                     self.back), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 0, 3), (730, 530), BUTTON_DEFAULT,
                                     handle_music()), 0)

        # Setup Player
        self.player.direct_move(-100, -100)
        self.player.display_mode("")

    def update(self, surface, dt):
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)
        self.menu.update(surface, dt)

        surface.blit(self.text, (self.center(self.text), 220))

    # Function
    def save_data(self):
        """Saves current player data."""
        save_data([self.player.package_data(), Control.state_data, None], "player_data")
        self.back()


class MainMenu(State):
    """Main menu."""

    def __init__(self):
        super().__init__()

    def startup(self):
        handle_music("trooper.mp3")

        # Setup menu itself
        self.menu = SimpleMenu(15, 275, 400)

        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(MovingBackgroundElement([load_img(load_s("back1.png"))], (0, 2), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_img(load_s("logo.png"))], (0, 0)), 0)

        self.canvas.add_element(Butt(Control.sheets["button2"].load_some_images(0, 0, 3), (0, 270), BUTTON_DEFAULT,
                                     self.campaign), 0)
        self.canvas.add_element(Butt(Control.sheets["button2"].load_some_images(2, 0, 3), (0, 340), BUTTON_DEFAULT,
                                     self.load), 0)
        self.canvas.add_element(Butt(Control.sheets["button2"].load_some_images(4, 0, 3), (0, 410), BUTTON_DEFAULT,
                                     self.quit_game), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 0, 3), (730, 530), BUTTON_DEFAULT,
                                     handle_music), 0)

        # Setup Player
        self.player.change_name("")
        self.player.direct_move(-100, -100)
        self.player.display_mode("")

        # Anytime the player enters the main menu, the levels all change
        Control.generate_states()

    # Functions. Some are redundant but whatever.
    def campaign(self):
        """Onto giving your character a name!"""
        self.to("intro")

    def load(self):
        """Go to the loading screen."""
        self.to("load")


class Intro(State):
    """Screen to give your character a name."""

    def __init__(self):
        super().__init__()
        self.timer = DTimer(pygame.USEREVENT + 1)

        self.destination = "player_menu"
        self.player.current_level = "l0-1"

        self.font = fonts[2]
        self.text = self.font.render("", True, (0, 0, 0))

    def cleanup(self):
        self.text = self.font.render("", True, (0, 0, 0))

    def startup(self):
        # Setup Menu
        self.menu = SimpleMenu(15, 130, 400)

        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(StaticBG([load_img(load_s("land1.png"))], (0, 0)), 0)
        self.canvas.add_element(MovingBackgroundElement([load_img(load_s("cloud0.png"))], (-1, 0), (800, 600)), 0)

        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 0, 3), (730, 530), BUTTON_DEFAULT,
                                     handle_music), 0)
        input_textbox = InputT([load_img(load_b("1600x75.png")), load_img(load_b("0600x75.png"))],
                               (0, 200), INPUT_DEFAULT, self.enter_name)
        self.canvas.add_element(input_textbox, 1)
        self.canvas.add_element(Butt(Control.sheets["button4"].load_some_images(1, 0, 3), (0, 300), BUTTON_DEFAULT,
                                     self.skip_tutorial), 2)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(0, 0, 3), (0, 0), BUTTON_DEFAULT,
                                     self.back), 3)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(2, 0, 3), (700, 130), BUTTON_DEFAULT,
                                     input_textbox.submit_text), 4)

        # Setup Player (should be hardcoded as Player dimensions are constant)
        self.player.name_display(True)
        self.player.health_display(False)
        self.player.display_mode("")
        self.player.direct_move(350, 472)

    def handle_event(self, event):
        """Needed a timer this time to finish the animation."""
        self.canvas.handle_event(event)

        if event.type == self.timer.event:
            self.to(self.destination)

    def update(self, surface, dt):
        """Needed for updating timer."""
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)
        self.timer.update(dt)

        surface.blit(self.text, (self.center(self.text), 220))

    def back(self):
        """Goes back to the previous state. Restores player settings to enable story."""
        self.player.current_level = "l0-1"
        self.destination = "player_menu"
        self.to(self.previous)

    # Functions

    def enter_name(self, text):
        """Once you entered a name, gives the player that name and moves him off screen. We then
           wait 2 seconds (to finish animation) and move onto the story state."""
        self.canvas.delete_group(1)
        self.canvas.delete_group(2)
        self.canvas.delete_group(3)
        self.canvas.delete_group(4)
        self.player.change_name(text)
        self.player.command_move(5, 0, 1000, 472)
        self.timer.activate(2)

    def skip_tutorial(self):
        """Skips the story and tutorial level."""
        self.player.current_level = "l0-1"
        self.destination = "player_menu"
        self.player.exp = 1
        self.canvas.delete_group(2)
        self.text = self.font.render("Tutorial will be skipped.", True, (0, 0, 0))


class PlayerMenu(State):
    """The player_menu. Return here after every battle to stock up or save."""

    def __init__(self):
        super().__init__()

        self.font = fonts[2]
        self.text = self.font.render("Next Level: {0}".format(self.player.current_level), True, (0, 0, 0))

    def startup(self):
        handle_music("note.mp3")

        # Setup Menu
        self.menu = SimpleMenu(20, 250, 400)

        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(MovingBackgroundElement([load_img(load_s("back2.png"))], (0, -1), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_img(load_s("mhub1.png"))], (0, 0)), 0)

        self.canvas.add_element(Butt(Control.sheets["button2"].load_some_images(3, 0, 3), (0, 250), BUTTON_DEFAULT,
                                     self.play), 0)
        self.canvas.add_element(Butt(Control.sheets["button2"].load_some_images(1, 0, 3), (0, 320), BUTTON_DEFAULT,
                                     self.inventory), 0)
        self.canvas.add_element(Butt(Control.sheets["button2"].load_some_images(5, 0, 3), (0, 390), BUTTON_DEFAULT,
                                     self.shop), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 0, 3), (730, 530), BUTTON_DEFAULT,
                                     handle_music), 0)
        self.canvas.add_element(Butt(Control.sheets["button3"].load_some_images(1, 0, 3), (0, 530), BUTTON_DEFAULT,
                                     self.save), 0)
        self.canvas.add_element(Butt(Control.sheets["button3"].load_some_images(1, 3, 3), (70, 530), BUTTON_DEFAULT,
                                     self.load), 0)

        # Setup Player (should be hardcoded as Player dimensions are constant)
        self.player.stop_move()
        self.player.direct_move(38, 72)
        self.player.name_display(False)
        self.player.health_display(False)
        self.player.display_mode("menu")

    def update(self, surface, dt):
        """Draws stuff pertaining to this state. Generally, menu options should be on top."""
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)

        self.text = self.font.render("Next Level: {0}".format(self.player.current_level), True, (0, 0, 0))
        surface.blit(self.text, (self.center(self.text), 210))

    # Functions. Some are redundant but whatever.
    def play(self):
        """Onto battle!"""
        self.to(self.player.current_level)

    def shop(self):
        """Let's go shopping!"""
        # self.to("shop")
        pass

    def inventory(self):
        """Let's see your inventory."""
        self.to("inventory")

    def save(self):
        """Saves the game."""
        self.to("save")

    def load(self):
        """Loads the game."""
        self.to("load")


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
        # Setup Menu
        self.menu = SimpleMenu(20, 250, 265)

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


class Preamble(State):
    """Sometimes you have a chit-chat before battle."""

    def __init__(self, enemy, bg, destination):
        super().__init__()

        self.destination = destination
        self.enemy = enemy
        self.bg = bg

        self.text_info = self.enemy.preamble
        self.portraits = [Control.sheets["portrait1"].load_image(0, 0),
                          Control.sheets["portrait1"].load_image(self.text_info[2][0], self.text_info[2][1])]
        self.d_box = None

        self.player_x = 60
        self.player_y = 257
        self.enemy_x = 800 - self.player_x - self.enemy.image.get_width()
        self.enemy_y = self.player_y - self.enemy.image.get_height() + 100

        self.timer = DTimer(pygame.USEREVENT + 1)

    def startup(self):
        pygame.mixer.music.stop()

        self.menu = SimpleMenu(15, 330, 400)
        self.timer.activate(1)

        self.canvas = Canvas()
        self.canvas.add_element(StaticBG([load_img(load_s("{0}.png".format(self.bg)))], (0, 0)), 0)
        self.canvas.add_element(MovingBackgroundElement([load_img(load_s("cloud{0}.png".format(self.bg)))],
                                                        (-1, 0), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_img(load_s("ground0.png"))], (0, 0)), 1)

        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 0, 3), (730, 530), BUTTON_DEFAULT,
                                     handle_music), 0)
        d_data = DData(self.text_info[0], self.portraits, self.text_info[1])
        self.d_box = DBox([load_img(load_b("text600x200.png"))], (0, 100), DIALOGUE_DEFAULT, self.next_dialogue, d_data)
        self.canvas.add_element(self.d_box, 1)

        self.player.direct_move(-300, self.player_y)
        self.player.command_move(10, 0, self.player_x, self.player_y)
        self.player.name_display(False)
        self.player.display_mode("")
        self.player.health_display(False)

        self.enemy.direct_move(1000, self.enemy_y)
        self.enemy.command_move(10, 0, self.enemy_x, self.enemy_y)
        self.enemy.name_display(False)
        self.enemy.display_mode("")
        self.enemy.health_display(False)

    def handle_event(self, event):
        """Handles events in this state."""
        self.canvas.handle_event(event)
        if event.type == self.timer.event:
            self.d_box.toggle_visibility()

    def update(self, surface, dt):
        """Draws stuff pertaining to this state. Generally, menu options should be on top."""
        self.canvas.update(surface, dt)
        State.player.update(surface, dt)
        self.enemy.update(surface, dt)
        self.timer.update(dt)

    # Functions
    def next_dialogue(self):
        """Signals to dialogue widget to move to the next script. Reaching end of script triggers something."""
        if not self.d_box.next_script():
            self.to(self.destination)


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

        # Setup Menu
        self.menu = SimpleMenu(20, 250, 265)

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
            self.canvas.add_element(StaticBG([load_img(load_c("chest100x100.png"))],
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


class GameOver(State):
    """You died. Quit or load past save."""

    def __init__(self):
        super().__init__()

    def startup(self):
        handle_music("menu.mp3")

        # Setup menu itself
        self.menu = SimpleMenu(15, 170, 400)

        # Setup Canvas
        self.canvas = Canvas()
        self.canvas.add_element(MovingBackgroundElement([load_img(load_s("back1.png"))], (0, 2), (800, 600)), 0)
        self.canvas.add_element(StaticBG([load_img(load_s("bricks.png"))], (0, 0)), 0)
        self.canvas.add_element(StaticBG([load_img(load_s("gameover.png"))], (0, 0)), 0)

        self.canvas.add_element(Butt(Control.sheets["button2"].load_some_images(4, 0, 3), (0, 0), BUTTON_DEFAULT,
                                     self.return_menu), 0)
        self.canvas.add_element(Butt(Control.sheets["button"].load_some_images(1, 0, 3), (730, 530), BUTTON_DEFAULT,
                                     handle_music), 0)

        # Setup Player (should be hardcoded as Player dimensions are constant)
        self.player.name_display(True)
        self.player.health_display(False)
        self.player.display_mode("")

        self.player.status(False)
        self.player.image = self.player.images[13]
        self.player.direct_move(350, 472)

    # Functions. Some are redundant but whatever.

    def return_menu(self):
        """Goes back to the main menu. Since the player died, everything is reset for the next run if
           the user still wants to be in the same session."""
        self.player.reset_player()
        self.player.dice_set = [State.gen_dice("basic1"), State.gen_dice("basic1")]
        # Shop.refill()
        self.to("main_menu")


# UTILS
def load_img(path):
    return pygame.Surface.convert_alpha(pygame.image.load(path))


def quit_game():
    """Quits the game."""
    pygame.quit()
    sys.exit()


# FONTS
fonts = [pygame.font.Font(rp("assets/VT323-Regular.ttf"), 25),
         pygame.font.Font(rp("assets/VT323-Regular.ttf"), 30),
         pygame.font.Font(rp("assets/VT323-Regular.ttf"), 40),
         pygame.font.Font(rp("assets/VT323-Regular.ttf"), 50)]

if __name__ == "__main__":
    game = Control("attributions")
    game.main_loop()
    quit_game()
