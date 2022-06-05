import random
from utils.path import *


# NPCs and Players
class Player(Enemy):
    """The main character of the game. Has an inventory and is the most nonchalant about it."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)

        self.exp_needed = [0, 8, 10, 12, 14, 17, 19, 22, 25, 30, 500]
        self.exp = 0

        # PLAYER EXCLUSIVE
        self.inventory = []
        self.current_level = "p0-0"

        self.tier = [[1, 100, 100, ["basic1", "basic1"], None]]

        self.idle_anim = [[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0, 0, 0],
                          [5, 6, 7, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 0, 0, 0, 0],
                          [9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 10, 10, 10, 10, 10, 9, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.idle_run = random.choice(self.idle_anim)

    def level_up(self):
        """If the player's exp meets the requirement, levels up the player and returns True.
           Otherwise returns False."""
        if self.exp >= self.exp_needed[self.level]:
            self.level += 1
            self.exp = self.exp - self.exp_needed[self.level]

            self.health += self.health // 10
            self.current = self.health

            return True
        return False

    def level_up_text(self):
        """Wrapper for level_up. When true, returns a string. Otherwise, returns an empty string."""
        return "Leveled up!" if self.level_up() else ""

    def reset_player(self):
        """Resets the player to basic stats."""
        self.inventory = []
        self.current_level = "p0-0"
        self.exp = 0
        self.dead = False
        self.set_stats(0)

    def package_data(self):
        """Returns a list of player data to save.
           [level, current, health, money, dice set, inventory, current level, exp, name]"""
        return [self.level, self.current, self.health, self.money,
                [i.ID for i in self.dice_set],
                [i.ID for i in self.inventory],
                self.current_level, self.exp, self.name]


class Aaron(Enemy):
    """Placeholder enemy for testing battling."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)

        self.tier = [[1, 20, 0, ["basic1", "basic1"],
                      [["Greetings! ``````I am the tutorial man.",
                        "And it looks like you need a tutorial!",
                        "Uh... `````weren't you the one that got the  last of my money?",
                        "Yes, ````but many others haven't gotten     their money.",
                        "They want to fight you for it, so let's prepare you!",
                        "Sure..."], "110110", (0, 1)]],
                     [random.randint(6, 8), 11, 40, ["basic2", "basic2"],
                      [["Well well well.",
                        "We meet again."], "11", (0, 1)]],
                     [random.randint(8, 11), 9, 60, ["basic3", "basic3", "basic2"],
                      [["Got any good places for food?",
                        "I know a good curry place.",
                        "Ew."], "101", (0, 1)]],
                     [random.randint(10, 13), 10, 70, ["basic4", "basic3", "basic3"],
                      [["It sure is hot over here.",
                        "Then go home.",
                        "No."], "101", (0, 1)]],
                     [random.randint(13, 16), 11, 75, ["basic4", "basic5"],
                      [["Chips at the store are 50% off.",
                        "Then let's go.",
                        "I've been starving."], "100", (0, 1)]],
                     [random.randint(16, 17), 12, 80, ["basic5", "basic5"],
                      [["And so the student",
                        "becomes the master.",
                        "And all masters must die.",
                        "You okay?"], "1110", (0, 1)]]
                     ]

        self.change_name("Aaron")

        self.idle_anim = [[1, 2, 3, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0, 0, 0, 0],
                          [5, 6, 7, 8, 9, 9, 9, 9, 9, 8, 7, 6, 5, 0, 0, 0, 0],
                          [10, 11, 12, 12, 12, 12, 12, 12, 12, 11, 10, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.idle_run = random.choice(self.idle_anim)


class Dorita(Enemy):
    """A floating nacho chip surrounded by balls. Likes to roll crap dice."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)
        self.frame = 0.015

        self.tier = [[random.randint(3, 4), 6, 20, ["basic1", "basic1"],
                      [["You know, I might consider that I.O.U.",
                        "On the condition that I get to beat you up.",
                        "Crap."], "110", (0, 4)]],
                     [random.randint(4, 6), 10, 40, ["basic2", "basic2", "divider2"],
                      [["I wish I was a square.",
                        "Good luck with that."], "10", (0, 4)]],
                     [random.randint(7, 9), 11, 60, ["basic2", "basic3", "divider3"],
                      [["You have to stop running.",
                        "Never!",
                        "What is even your end goal?",
                        "Beating the final boss.",
                        "And then everything goes back to normal."], "10100", (0, 4)]],
                     [random.randint(10, 12), 12, 80, ["basic4", "basic3", "basic3", "divider3"],
                      [["Why are you here?",
                        "Sightseeing.",
                        "I heard you can see idiots here.",
                        "Rude."], "0110", (0, 4)]],
                     [random.randint(12, 15), 12, 90, ["basic5", "divider3"],
                      [["A tale of two cities...",
                        "There is one city doofus."], "10", (0, 4)]],
                     [random.randint(15, 17), 14, 100, ["basic5", "basic5", "divider3"],
                      [["Can't believe you ran off.",
                        "But I still caught up."], "11", (0, 4)]]
                     ]

        self.change_name("Dorita")

        self.idle_anim = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                           28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]]
        self.idle_run = random.choice(self.idle_anim)


class Wally(Enemy):
    """Sometimes whales like to play craps. Hits hard with one die."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)
        self.frame = 0.07

        self.tier = [[random.randint(3, 4), 15, 70, ["basic2"],
                      [["You know the drill.",
                        "Can't we talk things out?",
                        "No."], "101", (1, 5)]],
                     [random.randint(5, 8), 10, 80, ["basic2", "heal1"],
                      [["Going to the beach. ```````Wanna come?",
                        "Not really in the mood.",
                        "Well, screw you then."], "101", (1, 5)]],
                     [random.randint(8, 11), 10, 100, ["basic2", "basic2", "heal1", "heal1"],
                      [["You have to fight me. ```````Unfortunate.",
                        "No need to be an ass about it."], "10", (1, 5)]],
                     [random.randint(11, 13), 11, 120, ["basic3", "basic3"],
                      [["I am way out of my elements.",
                        "And yet you are still picking fights."], "10", (1, 5)]],
                     [random.randint(13, 16), 12, 140, ["basic5", "basic5"],
                      [["After I get my money,",
                        "I shall get wasted at the bar.",
                        "Can I come?",
                        "Sure."], "1101", (1, 5)]],
                     [random.randint(15, 17), 13, 150, ["basic5", "basic5", "heal2"],
                      [["Time to sleep little buddy.",
                        ":("], "10", (1, 5)]]
                     ]

        self.change_name("Wally")

        self.idle_anim = [[0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 7, 8, 7, 4, 3, 2, 1, 0, 0, 0],
                          [0, 0, 9, 9, 0, 0, 10, 11, 12, 12, 16, 16, 16, 12, 12, 12, 16, 12, 11, 10, 0, 0],
                          [0, 0, 9, 9, 15, 9, 15, 9, 0, 0],
                          [0, 0, 17, 18, 19, 20, 21, 22, 23, 24, 17, 18, 19, 20, 21, 22, 23, 24, 0, 0],
                          [0, 0, 0, 0, 0]]
        self.idle_run = random.choice(self.idle_anim)


class BadDuck(Enemy):
    """Not bulky but annoying."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)
        self.frame = 0.06

        self.tier = [[random.randint(2, 4), 7, 25, ["poison1", "poison1"],
                      [["Quack quack. I'm duck.",
                        "Yes you are.",
                        "Ugh. `````You give off bad vibes.",
                        "..."], "1010", (0, 5)]],
                     [random.randint(5, 7), 8, 30, ["poison2", "poison2", "poison2"],
                      [["I'm toxic in online games.",
                        "I find it funny.",
                        "..."], "110", (0, 5)]],
                     [random.randint(7, 10), 8, 30, ["poison2", "poison2", "divider3"],
                      [["You should get that rash checked out.",
                        "What rash?",
                        "That red dot on your body.",
                        "That's a birthmark dingus."], "1010", (0, 5)]],
                     [random.randint(11, 13), 10, 50, ["poison3", "poison2", "divider3"],
                      [["Accept my friend request.",
                        "I will later."], "10", (0, 5)]],
                     [random.randint(13, 15), 12, 70, ["poison3", "poison3", "divider3"],
                      [["I wonder if the game shop is open.",
                        "Just order online like everyone else."], "10", (0, 5)]],
                     [random.randint(15, 17), 13, 80, ["poison3", "poison3", "poison3", "divider3"],
                      [["They really should nerf poison."], "1", (0, 5)]]
                     ]

        self.change_name("Baduck")

        self.idle_anim = [[0, 0, 0, 0, 1, 2, 3, 4, 4, 3, 2, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 5, 6, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 6, 6, 0, 0, 0],
                          [0, 0, 8, 9, 10, 11, 11, 11, 10, 9, 8, 0, 0, 5, 6, 7, 6, 5, 0],
                          [0, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 0],
                          [0, 0, 0, 0, 0]]
        self.idle_run = random.choice(self.idle_anim)


class Michael(Enemy):
    """Do not fight."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)
        self.frame = 0.001

        self.tier = [[random.randint(5, 7), 6, 55, ["basic1", "multiplier1"], None],
                     [random.randint(6, 8), 7, 70, ["basic2", "multiplier2"], None],
                     [random.randint(8, 11), 8, 80, ["basic2", "basic2", "multiplier2"], None],
                     [random.randint(11, 13), 10, 90, ["basic3", "multiplier3"], None],
                     [random.randint(13, 15), 12, 110, ["basic4", "basic4", "multiplier3"], None],
                     [random.randint(15, 17), 13, 120, ["basic5", "basic5", "multiplier3"], None]
                     ]

        self.change_name("migahexx.xml")

        self.idle_anim = [[0, 0, 0, 0, 1, 2, 3, 4, 4, 3, 2, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 5, 6, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 6, 6, 0, 0, 0],
                          [0, 0, 8, 9, 10, 11, 11, 11, 10, 9, 8, 0, 0, 5, 6, 7, 6, 5, 0],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
        self.idle_run = random.choice(self.idle_anim)


class Shopkeeper(Enemy):
    """A small cube maintaining a store full of deadly cubes."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)

        self.tier = [[random.randint(8, 10), 13, 300, ["basic2", "basic2", "multiplier1", "multiplier1"], None],
                     [random.randint(10, 13), 15, 500, ["basic3", "multiplier1", "poison2", "poison2"], None],
                     [random.randint(13, 15), 17, 800, ["basic3", "multiplier2", "heal2", "poison2"], None],
                     [random.randint(15, 17), 19, 1000, ["basic4", "multiplier3", "heal3", "poison3"], None],
                     [random.randint(17, 19), 21, 1200, ["basic5", "multiplier3", "multiplier3", "heal3"], None],
                     [random.randint(20, 21), 23, 1500, ["basic5", "basic5", "multiplier3", "multiplier3"], None]
                     ]

        self.change_name("Shopkeeper")

        self.idle_anim = [[0, 0, 0, 1, 2, 3, 4, 3, 2, 1, 0, 0, 0, 0, 0],
                          [0, 5, 6, 7, 6, 5, 0, 0, 0, 0, 0],
                          [0, 8, 9, 10, 9, 8, 0, 0, 0, 0, 0],
                          [0, 11, 11, 11, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.idle_run = random.choice(self.idle_anim)


class GSquare(Enemy):
    """A sentient die that doesn't want to roll anymore. Though it also uses dice."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)

        self.tier = [[random.randint(3, 4), 7, 10, ["basic1", "poison1", "heal1"],
                      [["Choices.",
                        "Just another word for chance.",
                        "???"], "110", (2, 2)]],
                     [random.randint(6, 7), 9, 30, ["basic2", "poison2", "heal2", "divider2"],
                      [["Dice.",
                        "Messengers of fate.",
                        "Is this how dice talk?"], "110", (2, 2)]],
                     [random.randint(7, 9), 9, 40, ["basic2", "poison2", "heal2", "basic3"],
                      [["Money.",
                        "The blood of progress.",
                        "You intrigue me."], "110", (2, 2)]],
                     [random.randint(10, 12), 9, 60, ["basic3", "poison3", "divider3", "basic3"],
                      [["...",
                        "..."], "10", (2, 2)]],
                     [random.randint(12, 15), 10, 80, ["basic4", "basic5", "divider3", "heal3"],
                      [["Beauty.",
                        "Something you don't have.",
                        "Shut up."], "110", (2, 2)]],
                     [random.randint(15, 17), 12, 90, ["basic5", "poison3", "divider3", "heal3"],
                      [["Let's die.",
                        "What?"], "10", (2, 2)]]
                     ]

        self.change_name("Gamble Square")

        self.idle_anim = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                          [3, 4, 1, 2, 0, 5, 7, 1, 2, 3, 10, 11],
                          [5, 2, 1, 3, 4, 0, 7, 2, 6, 8, 8],
                          [1, 2, 5, 3, 0, 4, 1, 1, 2, 6, 2, 3]]
        self.idle_run = random.choice(self.idle_anim)


class Ria(Enemy):
    """A kind spirit. But also a sadist."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)
        self.frame = 0.1

        self.tier = [[random.randint(5, 6), 9, 40, ["basic1", "basic1", "heal1"],
                      [["Let me guess. `````````You want to fight.",
                        "I'll kill you."], "01", (1, 1)]],
                     [random.randint(6, 8), 8, 50, ["basic2", "basic2", "heal2"],
                      [["I'll kill you.",
                        "But why?",
                        "Girl, ``````I dunno."], "101", (1, 1)]],
                     [random.randint(8, 11), 10, 70, ["basic3", "basic2", "basic1", "heal2"],
                      [["You should go skydiving",
                        "without a parachute. <3",
                        "At least you're not outright saying it."], "110", (1, 1)]],
                     [random.randint(11, 13), 11, 90, ["basic3", "basic3", "heal2"],
                      [["I'll steal your heart",
                        "literally.",
                        "Oh no."], "110", (1, 1)]],
                     [random.randint(13, 15), 13, 110, ["basic4", "basic4", "heal3"],
                      [["Maybe trying to kill you isn't a good   idea.",
                        "You need a hobby.",
                        "I'll kill you."], "101", (1, 1)]],
                     [random.randint(15, 17), 10, 120, ["basic5", "basic5", "heal2", "heal3"],
                      [["Violence.",
                        "You speak violence.",
                        "I'll kill you."], "001", (1, 1)]]
                     ]

        self.change_name("Ria")

        self.idle_anim = [[0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
                          [0, 0, 2, 3, 4, 4, 4, 4, 3, 2, 0, 0, 0, 0, 1, 1, 0, 0],
                          [0, 0, 0, 5, 6, 6, 6, 5, 0, 0, 0, 0, 0, 7, 8, 9, 8, 7, 0, 0, 0],
                          [0, 0, 0, 10, 11, 10, 11, 10, 0, 0, 0]]
        self.idle_run = random.choice(self.idle_anim)


class Wandre(Enemy):
    """A cloud with an attitude. Very upfront about her motives."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)
        self.frame = 0.09

        self.tier = [[random.randint(3, 5), 8, 30, ["basic1", "basic1", "divider3"],
                      [["Woah. ```````A cloud with a hoop.",
                        "And what about it?"], "01", (1, 4)]],
                     [random.randint(6, 7), 9, 40, ["basic2", "basic2", "divider2"],
                      [["You look like a mess.",
                        "That's very mean."], "101", (1, 4)]],
                     [random.randint(7, 10), 9, 60, ["basic3", "basic2", "divider3"],
                      [["So are you getting the new album?",
                        "Hell no.",
                        "So you do wanna die."], "101", (1, 4)]],
                     [random.randint(10, 12), 10, 80, ["basic4", "basic3", "divider3"],
                      [["You built like a box.",
                        "What?"], "10", (1, 4)]],
                     [random.randint(13, 15), 12, 100, ["basic5", "basic4", "divider3", "heal2"],
                      [["I'm craving some food right now.",
                        "Then go get some food.",
                        "I would if you PAID me",
                        "broke ass."], "1011", (1, 4)]],
                     [random.randint(15, 17), 15, 110, ["basic5", "basic5", "divider3", "heal3"],
                      [["Money?",
                        "No."], "10", (1, 4)]]
                     ]

        self.change_name("Wandre")

        self.idle_anim = [[0, 0, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 0, 0],
                          [0, 0, 0, 5, 6, 7, 8, 8, 8, 9, 9, 8, 8, 7, 6, 5, 0, 0, 0],
                          [0, 0, 0, 0, 0, 10, 0, 0, 10, 0, 0, 0, 10, 10, 0, 0, 0],
                          [0, 0, 0, 11, 0, 11, 0, 11, 0, 0, 0],
                          [4, 4, 4, 4, 4, 4]]
        self.idle_run = random.choice(self.idle_anim)


class Cena(Enemy):
    """Not associated with John Cena."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)

        self.tier = [[random.randint(3, 4), 5, 15, ["basic1", "poison1"],
                      [["Wonderful day isn't it?",
                        "Perfect weather to beat you up!",
                        "So violent."], "110", (0, 3)]],
                     [random.randint(6, 8), 7, 30, ["basic2", "poison2", "poison2"],
                      [["I need to sleep.",
                        "Same."], "10", (0, 3)]],
                     [random.randint(8, 11), 8, 40, ["basic2", "poison2", "poison3", "heal2"],
                      [["Photosynthesis.",
                        "Study it. ``````Live by it.",
                        "..."], "110", (0, 3)]],
                     [random.randint(11, 13), 9, 60, ["poison3", "poison3", "heal2"],
                      [["Have you seen my cactus friend?",
                        "He owes me lunch."], "11", (0, 3)]],
                     [random.randint(13, 15), 10, 75, ["poison3", "poison3", "heal3"],
                      [["Can't wait to return home.",
                        "I hate seeing people I know.",
                        "I hate seeing people I don't know."], "110", (0, 3)]],
                     [random.randint(15, 17), 12, 80, ["poison3", "poison3", "poison3", "heal3"],
                      [["If you beat me...",
                        "then what?",
                        "Debts don't disappear you know.",
                        "I'll find a way."], "1110", (0, 3)]]
                     ]

        self.change_name("Cena")

        self.idle_anim = [[0, 0, 0, 1, 2, 3, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 3, 2, 1, 0, 0],
                          [0, 0, 0, 5, 6, 7, 8, 7, 6, 7, 6, 5, 0, 0, 0],
                          [0, 0, 0, 9, 10, 11, 11, 11, 10, 9, 9, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.idle_run = random.choice(self.idle_anim)


class Bursa(Enemy):
    """Bursa has not seen his vegan brother. Must've gone to a different game."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)
        self.frame = 0.1

        self.tier = [[random.randint(4, 5), 6, 25, ["basic1"],
                      [["Burgers suck.",
                        "You suck."], "01", (0, 2)]],
                     [random.randint(6, 7), 8, 30, ["basic2", "basic2", "heal1"],
                      [["I got a bone to pick with you.",
                        "I don't think I have any bones.",
                        "Shut up."], "101", (0, 2)]],
                     [random.randint(7, 10), 9, 45, ["basic3", "basic2", "heal2"],
                      [["Money talks",
                        "and it looks like you have nothing to say.",
                        "Wow."], "110", (0, 2)]],
                     [random.randint(11, 13), 10, 65, ["basic3", "basic3", "heal3"],
                      [["I feel like I'm being cooked.",
                        "Wouldn't recommend this feeling."], "11", (0, 2)]],
                     [random.randint(13, 15), 12, 75, ["basic4", "basic4", "heal3"],
                      [["I don't want to be a lawyer.",
                        "What",
                        "Making small talk."], "101", (0, 2)]],
                     [random.randint(15, 17), 14, 85, ["basic5", "basic5", "heal3"],
                      [["End of the line.",
                        "Doesn't have to end this way."], "10", (0, 2)]]
                     ]

        self.change_name("Bursa")

        self.idle_anim = [[0, 0, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0, 0],
                          [0, 0, 0, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 0, 0, 0],
                          [0, 0, 0, 0, 8, 8, 0, 0, 8, 0, 0, 0, 8, 0, 0, 0, 0],
                          [0, 0, 0, 9, 10, 9, 11, 9, 10, 9, 0, 0, 0]]
        self.idle_run = random.choice(self.idle_anim)


class Sosh(Enemy):
    """He's more likely to help you out than try to kill you. But sometimes that doesn't line up."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)
        self.frame = 0.09

        self.tier = [[random.randint(3, 4), 7, 15, ["basic1", "basic1"],
                      [["Hello!",
                        "Running from your debts I see.",
                        "It's just a crappy day."], "110", (1, 3)]],
                     [random.randint(5, 6), 9, 20, ["basic2", "multiplier2"],
                      [["I wonder... ``````why do you fight?",
                        "...",
                        "I dunno."], "100", (1, 3)]],
                     [random.randint(7, 9), 9, 40, ["basic2", "basic2", "multiplier3"],
                      [["You still seem stressed.",
                        "It doesn't help that everyone's trying to fight me."], "10", (1, 3)]],
                     [random.randint(10, 12), 10, 60, ["basic3", "multiplier3"],
                      [["I shall strike you down",
                        "and you will know peace.",
                        "Great."], "110", (1, 3)]],
                     [random.randint(12, 15), 12, 80, ["basic4", "basic4", "multiplier3"],
                      [["Hello!",
                        "Good afternoon."], "10", (1, 3)]],
                     [random.randint(15, 17), 14, 90, ["basic5"],
                      [["I'll go easy on you.",
                        "Thanks."], "10", (1, 3)]]
                     ]

        self.change_name("Sosh")

        self.idle_anim = [[0, 0, 0, 1, 2, 3, 2, 1, 2, 3, 2, 1, 0, 0, 0],
                          [0, 0, 0, 4, 5, 6, 6, 6, 6, 6, 5, 4, 4, 0, 0, 0],
                          [0, 0, 0, 0, 7, 8, 9, 8, 9, 8, 7, 7, 0, 0, 0, 0],
                          [0, 0, 0, 10, 0, 0, 10, 10, 0, 0, 0, 0, 0],
                          [0, 0, 0, 11, 0, 0, 11, 0, 0, 0, 0, 0, 0]]
        self.idle_run = random.choice(self.idle_anim)


class Arca(Enemy):
    """Sucks at fighting games. Will you let him beat you?"""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)
        self.frame = 0.09

        self.tier = [[random.randint(2, 3), 8, 15, ["basic1", "basic1"],
                      [["I will cleave your hype.",
                        "Please don't."], "10", (2, 0)]],
                     [random.randint(5, 6), 10, 25, ["basic1", "basic1"],
                      [["I made a song.",
                        "Will you post it?",
                        "Nope."], "101", (2, 0)]],
                     [random.randint(7, 9), 12, 30, ["basic1", "basic1"],
                      [["Bario is not real.",
                        "Who?"], "10", (2, 0)]],
                     [random.randint(10, 12), 12, 50, ["basic1", "basic1"],
                      [["I am bloodstain."], "1", (2, 0)]],
                     [random.randint(12, 15), 14, 70, ["basic1", "basic1"],
                      [["Let's eat spaghetti.",
                        "Now you're speaking my language."], "10", (2, 0)]],
                     [random.randint(15, 20), 18, 80, ["basic1", "basic1"],
                      [["Quack quack",
                        "Quack"], "10", (2, 0)]]
                     ]

        self.change_name("Arca")

        self.idle_anim = [[0, 0, 0, 1, 2, 3, 3, 3, 2, 1, 0, 0, 0],
                          [0, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 0],
                          [0, 0, 0, 5, 6, 7, 7, 7, 6, 5, 0, 0, 8, 9, 10, 10, 10, 9, 8, 0, 0, 0],
                          [0, 0, 0, 11, 0, 0, 11, 0, 0, 0, 0, 0, 0]]
        self.idle_run = random.choice(self.idle_anim)


class Ellie(Enemy):
    """You have a sister. Apparently."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)

        self.tier = [[random.randint(2, 3), 9, 16, ["basic1"],
                      [["We got no money.",
                        "And we owe some more.",
                        "Yikes."], "001", (2, 1)]],
                     [random.randint(4, 5), 9, 25, ["basic1", "basic2"],
                      [["Beaches are fun.",
                        "You used to hate beaches.",
                        "Well, ``````things change."], "101", (2, 1)]],
                     [random.randint(6, 8), 10, 40, ["basic1", "basic2", "basic2", "heal1"],
                      [["Square up!",
                        "And you want to fight because...",
                        "Practice."], "101", (2, 1)]],
                     [random.randint(9, 11), 12, 55, ["basic1", "basic3", "poison2", "heal2"],
                      [["Did you bring any water?",
                        "Nope."], "10", (2, 1)]],
                     [random.randint(11, 15), 14, 65, ["basic1", "basic4", "basic4", "heal3"],
                      [["We should head home.",
                        "But we just got here."], "10", (2, 1)]],
                     [random.randint(15, 17), 15, 75, ["basic1", "basic5", "heal3"],
                      [["I'm not supposed to be a boss.",
                        "Too bad."], "10", (2, 1)]]
                     ]

        self.change_name("Ellie")

        self.idle_anim = [[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0, 0, 0],
                          [5, 6, 7, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 0, 0, 0, 0],
                          [9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 10, 10, 10, 10, 10, 9, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.idle_run = random.choice(self.idle_anim)


class Kiran(Enemy):
    """A rich star. Also a random final boss."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)

        self.tier = [[random.randint(3, 5), 10, 20, ["basic1", "heal1"],
                      [["Wish upon a shooting star.",
                        "I wish you are out of my way."], "10", (2, 3)]],
                     [random.randint(5, 6), 11, 25, ["basic2", "basic2", "heal1"],
                      [["I only buy the BEST headbands.",
                        "The BEST.",
                        "..."], "110", (2, 3)]],
                     [random.randint(6, 8), 12, 45, ["basic3", "basic3", "heal2"],
                      [["What time is it?",
                        "Don't you have a watch?",
                        "It broke."], "101", (2, 3)]],
                     [random.randint(9, 10), 12, 55, ["basic4", "basic4", "heal2"],
                      [["rawr XD",
                        "Oh no."], "10", (2, 3)]],
                     [random.randint(11, 13), 15, 75, ["basic5", "basic5", "heal3"],
                      [["Ever try to eat gold?",
                        "No.",
                        "You're missing out."], "101", (2, 3)]],
                     [random.randint(15, 17), 15, 85, ["basic5", "basic5", "divider3", "multiplier3"],
                      [["I'm a final boss.",
                        "Har har.",
                        "..."], "110", (2, 3)]]
                     ]

        self.change_name("Kiran")

        self.idle_anim = [[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0, 0, 0],
                          [5, 6, 7, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 0, 0, 0, 0],
                          [9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 10, 10, 10, 10, 10, 9, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.idle_run = random.choice(self.idle_anim)


class Connor(Enemy):
    """A six-sided enthusiast."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)

        self.tier = [[random.randint(3, 4), 9, 15, ["basic1", "basic1", "basic1", "basic1"],
                      [["What rhymes with sex?",
                        "Six!",
                        "Huh?"], "110", (2, 4)]],
                     [random.randint(5, 7), 9, 20, ["basic2", "basic2", "basic1", "basic1"],
                      [["How many legs do insects have?",
                        "Six!"], "11", (2, 4)]],
                     [random.randint(6, 8), 11, 40, ["basic3", "basic2", "basic1"],
                      [["Everyone's connected",
                        "by at least six people.",
                        "Interesting."], "110", (2, 4)]],
                     [random.randint(9, 11), 11, 50, ["basic4", "basic2"],
                      [["I've seen you many times.",
                        "No you have not."], "10", (2, 4)]],
                     [random.randint(11, 12), 13, 70, ["basic5", "basic5", "basic2"],
                      [["You need more sides.",
                        "Be more well-rounded.",
                        "No."], "110", (2, 4)]],
                     [random.randint(13, 15), 15, 85, ["basic4", "multiplier3", "multiplier3"],
                      [["This game has six stages.",
                        "Great..."], "10", (2, 4)]]
                     ]

        self.change_name("Connor")

        self.idle_anim = [[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0, 0, 0],
                          [6, 7, 8, 8, 9, 9, 8, 8, 7, 7, 7, 7, 7, 7, 7, 6, 5, 0, 0, 0, 0],
                          [10, 10, 10, 10, 10, 10, 11, 11, 11, 10, 10, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.idle_run = random.choice(self.idle_anim)


class Baggins(Enemy):
    """Bag with a heart of gold."""

    def __init__(self, files, x, y):
        super().__init__(files, x, y)

        self.tier = [[random.randint(3, 4), 13, 30, ["basic2"],
                      [["You can solve all my problems.",
                        "All of them.",
                        "I don't feel safe."], "001", (2, 5)]],
                     [random.randint(5, 6), 14, 35, ["basic3"],
                      [["I should go to a dentist."], "1", (2, 5)]],
                     [random.randint(6, 7), 14, 55, ["basic4"],
                      [["Dice have been getting more expensive.",
                        "I think I see a solution."], "10", (2, 5)]],
                     [random.randint(8, 9), 15, 65, ["basic5"],
                      [["You are on my rob list.",
                        "Please reconsider."], "01", (2, 5)]],
                     [random.randint(10, 11), 16, 80, ["basic5", "heal3"],
                      [["More money",
                        "more problems."], "11", (2, 5)]],
                     [random.randint(11, 14), 16, 100, ["basic5", "heal3", "heal3"],
                      [["It's you, `````the broke guy.",
                        "I should end your rampage."], "11", (2, 5)]]
                     ]

        self.change_name("Baggins")

        self.idle_anim = [[1, 2, 3, 3, 3, 4, 4, 5, 5, 6, 5, 5, 6, 5, 5, 4, 4, 3, 3, 3, 2, 1, 0, 0, 0, 0],
                          [7, 8, 7, 8, 7, 8, 8, 8, 9, 9, 9, 8, 9],
                          [10, 10, 10, 10, 10, 10, 11, 11, 11, 10, 10, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.idle_run = random.choice(self.idle_anim)


# Dice
class Die(Base):
    """The DIE object is what players roll to deal damage to one another. Has sides and a
       multiplier if provided. Enemy classes contain dice with their dice_set.

       For dice, files must consist of 6 pictures indexed from 0.
       Note: For no-1 dice, we can roll the index to obtain the picture and then add to it
       so that it meets the minimum.

       In addition, each die has a price and a name (generated upon construction)."""

    def __init__(self, files, x, y, sides, multiple, ID):
        super().__init__(files, x, y)

        self.idle_anim = [[0, 1, 2, 3, 4, 5],
                          [3, 4, 1, 2, 0, 5],
                          [5, 2, 1, 3, 4, 0],
                          [1, 2, 5, 3, 0, 4]]
        self.idle_run = random.choice(self.idle_anim)

        self.sides = sides
        self.multiple = multiple
        self.safe = False

        self.price = int(130 * 1.5 * (multiple + 0.5))
        self.name = "Basic {0}X Die".format(self.multiple)

        # For saving purposes
        self.ID = ID

        self.rolled = False

    def roll(self, failsafe, number=None):
        """Rolls this die. If it is one, we return 0 since rolling a one immediately ends your turn.
           If number is provided, die will always output that side.
           If failsafe > 0, a rolled one gets changed to the value of the die's fifth side."""
        self.rolled = True

        # Set the image accordingly
        if number is not None:
            side = number
        else:
            side = random.randint(0, 5)

        value = self.sides[side]
        self.image = self.images[side]

        # Check for a one
        if value == 1 and not self.safe:
            if failsafe > 0:
                self.image = self.images[4]
                return self.sides[4] * self.multiple
            else:
                return 0
        else:
            return value * self.multiple


class Poison(Die):
    """When rolled, deals the displayed damage and then poisons the opponent
       with a counter to keep track.
       Opponent takes poison damage = counter at the end of their turn (so after
       they attack or fail one). Counter is then floor divided by 2 every turn until
       it is 0. Rolling subsequent poison dice can add to the counter."""

    def __init__(self, files, x, y, sides, multiple, ID):
        super().__init__(files, x, y, sides, multiple, ID)

        self.price += 400
        self.name = "Poison {0}X Die".format(self.multiple)


class Heal(Die):
    """When rolled, it will restore your health by the rolled value. In addition,
       it decreases your poison counter by the value as well. Cannot forfeit your turn with this die."""

    def __init__(self, files, x, y, sides, multiple, ID):
        super().__init__(files, x, y, sides, multiple, ID)
        self.safe = True

        self.price += 600
        self.name = "Heal {0}X Die".format(self.multiple)


class Divider(Die):
    """When rolled successfully, the die will divide your opponent's next damage roll by the rolled value.
       The effect WILL happen even if your opponent forfeits their turn or does not have any damage.
       Note that level should be '', '+' or '++'."""

    def __init__(self, files, x, y, sides, multiple, ID, level):
        super().__init__(files, x, y, sides, multiple, ID)

        self.price += (2000 * (len(level) + 1))
        self.name = "Divider Die{0}".format(level)


class Multiplier(Die):
    """When rolled successfully, the die will multiply your current DMG by the rolled value.
       Note that level should be '', '+' or '++'."""

    def __init__(self, files, x, y, sides, multiple, ID, level):
        super().__init__(files, x, y, sides, multiple, ID)

        self.price += (3000 * (len(level) + 1))
        self.name = "Multiplier Die{0}".format(level)
