import pygame

from entities.base_entity import BaseEntity


class Enemy(BaseEntity):
    """Base class for enemy characters of the game. In this case, they have a name, level, health, and dice_set.
       Enemies also serve as a container object for dice sprites. In addition, files should follow a format for best
       results. Each enemy character should consist of 15+ pictures (indexed from 0). Picture 12 should be attack
       picture. Picture 13 and 14 should be hurt and dead. Picture 0 - 11 are free spaces for idle animations. You can
       add more for smoother animations but don't use 12, 13, or 14 in your idle animations."""

    def __init__(self, images: list[pygame.Surface], pos: tuple[float, float]):
        super().__init__(images, pos)

        # Tier: [[level, health multiplier, money multiplier, list of dice names, preamble], ...]
        # Preference: Dice an enemy starts with. Player can always change their actual dice.
        # Preamble: A list where it's [list of dialogue, seq, portrait locations]
        self.tier = None
        self.preference = None
        self.preamble = None

        # GAMEPLAY PARAMETERS
        self.name = ""
        self.level = 0
        self.health = 0
        self.current = 0
        self.money = 0
        self.dice_set = None

        # DISPLAY
        self.mode = ""
        self.show_name = True
        self.show_hp = False

        self.poison = 0
        self.divided = 1
        self.blessed = 0
        self.dead = False

        self.font_size = 23
        self.font = pygame.font.Font(rp("assets/VT323-Regular.ttf"), self.font_size)

    # Displays
    def change_name(self, name):
        """Change the player's name."""
        self.name = name

    def name_display(self, show):
        """Whether to display the name above the character or not."""
        self.show_name = show

    def health_display(self, show):
        """Whether to display the health."""
        self.show_hp = show

    # Game Related Functions

    def set_stats(self, tier):
        """To be called after the enemy is created. Tier determines what stats and dice the enemy will get."""
        self.level = self.tier[tier][0]
        self.health = self.level * self.tier[tier][1]
        self.current = self.health
        self.money = self.level * self.tier[tier][2]
        self.preference = self.tier[tier][3]
        self.preamble = self.tier[tier][4]

    def roll_die(self, index):
        """Roll the index die in your inventory."""
        if len(self.dice_set) > index and not self.dice_set[index].rolled:
            value = self.dice_set[index].roll(failsafe=self.blessed)
            if self.blessed > 0:
                self.blessed -= 1
            return value

    def roll_die_forced(self, index, number):
        """Roll the index die in your inventory where outcome is the specified side."""
        if len(self.dice_set) > index and not self.dice_set[index].rolled:
            return self.dice_set[index].roll(failsafe=0, number=number)

    def needs_reset(self):
        """Have all the dice been rolled?"""
        return all([die.rolled for die in self.dice_set])

    def reset_dice(self):
        """Reset dice to be unrolled."""
        for die in self.dice_set:
            die.rolled = False
        return True

    def cleanse(self):
        """Removes all status elements."""
        self.poison = 0
        self.divided = 1
        self.blessed = 0

    def die(self):
        """Kills the character. All status elements are removed."""
        self.cleanse()
        self.dead = True

    # AI Behavior

    def basic_ai(self, player_health, damage, poison, heal, weaken):
        """Returns a random index value of the dice they want to roll. -1 signals ending a turn.
        END CONDITIONS: 25% chance, guaranteed lethal, will weaken, heal 20, damage more than 20"""
        if random.randint(0, 3) == 0 \
                or max(damage, poison) >= player_health \
                or weaken > 1 \
                or heal >= 20 \
                or damage > 30:
            return -1
        else:
            if not self.needs_reset():
                return random.choice([i for i in range(len(self.dice_set)) if not self.dice_set[i].rolled])
            else:
                return 0

    # Displays

    def find_center(self, text_surface):
        """Returns the centering with respect to the player."""
        return int((self.image.get_width() - text_surface.get_width()) / 2)

    def update(self, surface, dt):
        """Drawing the elements."""
        # Draw the elements
        self.move(dt)
        self.idle_animate(dt)
        surface.blit(self.image, (self.x, self.y))
        self.rect.move_ip(self.x, self.y)

        # Then draw the text above character
        if self.show_name:
            self.text_name = self.font.render(self.name, True, (0, 0, 0))
            surface.blit(self.text_name, (self.x + self.find_center(self.text_name),
                                          self.y - self.text_name.get_height() - 5))
        if self.show_hp:
            text_hp = self.font.render("{0} / {1}".format(self.current, self.health), True, (0, 0, 0))
            surface.blit(text_hp, (self.x + self.find_center(text_hp), self.y - text_hp.get_height() - 25))
        if self.poison > 0:
            text_poison = self.font.render("PSN: {0}".format(self.poison), True, (84, 22, 180))
            surface.blit(text_poison, (self.x + self.find_center(text_poison), self.y - text_poison.get_height() - 45))
        if self.divided > 1:
            text_divided = self.font.render("WEAKENED {0}X".format(self.divided), True, (0, 0, 0))
            surface.blit(text_divided,
                         (self.x + self.find_center(text_divided), self.y - text_divided.get_height() - 65))