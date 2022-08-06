"""
Module that creates a PokeGame via importing all values from other
classes.
- Christopher Denq
"""
# Importing all the different Pokemon types
import random as rand
from pokemon import *
from psychic_christopher_denq import *
from poison_emily_macway import *  # credit Emily Macway
from ghost_jonathon_green import *  # credit Jonathan Green
from fairy_kiera_fong import *  # credit Kiera Fong


class PokeGame:
    @staticmethod
    def setup():
        p1 = Pokemon("Eevee", "Ash")
        p2 = Psychic("Abra", "Ash", 50)
        p3 = GhostType("Ghastly", "Misty", 50)
        p4 = FairyType("Clefairy", "Misty", 50)
        p5 = Psychic("Hypno", "Brock", 50)
        p6 = Poison("Gengar", "Brock", 50)
        p7 = FairyType("Cleffa", "Chad", 50)
        return [p1, p2, p3, p4, p5, p6, p7]

    def __init__(self):
        self.game_master = self.setup()

    def draw_pokemon(self):
        index = rand.randint(0, len(self.game_master))
        drawn = self.game_master.pop(index)
        return drawn


def main():
    game = PokeGame()
    print(game.draw_pokemon())
    return


if __name__ == "__main__":
    main()

r"""
--- sample run of unit_test() ---

"""