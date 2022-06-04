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