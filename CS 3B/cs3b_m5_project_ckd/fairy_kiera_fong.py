"""
Mandatory Discussion - Pokemon
Submitted by Kiera Fong
Submitted: July 13, 2022

Objective: Create a class FairyType that inherits from class Pokemon.
"""

from pokemon import *
from random import *
from psychic_christopher_denq import *
from poison_emily_macway import *  # credit Emily Macway
from ghost_jonathon_green import *  # credit Jonathan Green


class Fighting(Pokemon):
    pass


class Fire(Pokemon):
    pass


class Dark(Pokemon):
    pass


class Dragon(Pokemon):
    pass


class FairyType(Pokemon):
    damage = 40

    def __init__(self, name, trainer, hp):
        # reference Pokemon __init__ using super()
        super().__init__(name, trainer)
        self.hp = hp
        self.basic_attack = 'Sweet Kiss'
        self.prob = 1
        self.type = 'FairyType'

    def attack(self, other):
        """Used to attack other pokemon and deal damage."""
        super().attack(other)
        if isinstance(self, FairyType):
            if rand.random() < self.prob and type(other) != FairyType and (other.hp != 0):
                other.paralyzed = True
                print(f"{other.name} is confused!")

    def receive_damage(self, damage, attacker):
        """Deals damage to a pokemon that has been attacked."""
        # FairyType is strong against:
        if isinstance(self, (Fighting, Dragon, Dark)):
            damage = damage * 2
        # FairyType is weak against:
        if isinstance(self, (Poison, Fire)):
            damage = damage / 2
        # deal damage after modifications to damage are made
        super().receive_damage(damage, attacker)

    def __str__(self):
        print("---")
        print(f"{self.trainer}'s {self.name}")
        print(f"Level: {self.level}, HP: {self.hp}/{self.max_hp}")
        print(f"Moves: {self.basic_attack}")
        print(f"Status: Paralyzed - {self.paralyzed}")
        print("---")
        return self.name


# Unit test
if __name__ == "__main__":
    jiggly = FairyType("Jigglypuff", "Kiera", 100)
    lickitung = Pokemon("Lickitung", "John")

    jiggly.attack(lickitung)
    print()
    jiggly.attack(lickitung)
    print()

    print(jiggly)
