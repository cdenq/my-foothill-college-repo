""" Emily Macway
Pokemon Class: Poison
CS 3B, July 13, 2022
"""
import random
from pokemon import *
from fairy_kiera_fong import *  # credit Kiera Fong


class Grass(Pokemon):
    pass


class Poison(Pokemon):
    """ Poison Type Pokemon"""

    def __init__(self, name, trainer, hp=50):
        super().__init__(name, trainer, hp)
        self.basic_attack = 'poison jab'
        self.damage = 40
        self.prob = 0.3

    def attack(self, other):
        """Override Attack for specific Poison Type"""
        if isinstance(self, Poison):
            if not self.paralyzed:
                self.speak()
                print(self.name, ' used ', self.basic_attack, '!')
                if isinstance(other, Grass) or isinstance(other, Fairy):
                    other.receive_damage(self.damage*2)
                if isinstance(other, Poison) or isinstance(other, Ghost):
                    other.receive_damage(self.damage*0.5)
                else:
                    other.receive_damage(self.damage)
            if random()<self.prob and type(other) != Poison:
                print(other.name, 'is poisoned')

    def __str__(self):
        print("---")
        print(f"{self.trainer}'s {self.name}")
        print(f"Level: {self.level}, HP: {self.hp}/{self.max_hp}")
        print(f"Moves: {self.basic_attack}")
        print(f"Status: Paralyzed - {self.paralyzed}")
        print("---")
        return self.name