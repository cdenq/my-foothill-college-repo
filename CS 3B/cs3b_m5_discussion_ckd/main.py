"""
Module that tests Psychic subclass from the Pokemon superclass found
in pokemon.py.
- Christopher Denq
"""
import random as rand
from pokemon import Pokemon


# Creating temporary classes to deal with strong/weak against
class Fighting(Pokemon):
    pass


class Poison(Pokemon):
    pass


class Bug(Pokemon):
    pass


class Ghost(Pokemon):
    pass


class Dark(Pokemon):
    pass


# Fully created Psychic class
class Psychic(Pokemon):
    PROB = 1
    basic_attack = 'Psychic Shift'
    strong_against = (Fighting, Poison)
    weak_against = (Bug, Ghost, Dark)

    def __init__(self, name, trainer, hp=50):
        super().__init__(name, trainer, hp)

    def attack(self, other):
        # determining weak/strong against
        # NOTE: pokemon.py doesn't have damage being passed into attack(),
        # thus why type(self).damage *= 2 etc. is necessary
        if isinstance(other, Psychic.strong_against):
            type(self).damage *= 2
            super().attack(other)
            type(self).damage /= 2
            print("The attack was super effective!")
        elif isinstance(other, Psychic.weak_against):
            type(self).damage /= 2
            super().attack(other)
            type(self).damage *= 2
            print("The attack was not very effective...")
        else:
            super().attack(other)

        # determining status effect
        if rand.random() < self.PROB and not isinstance(other, Psychic):
            other.paralyzed = True
            print(f"{other.name} is psycho-paralyzed!")
        if other.hp == 0:
            print(f"...or at least would be if {other.name} hadn't yet"
                  f" fainted.")
            other.paralyzed = False

    def receive_damage(self, damage, attacker):
        # determining weak/strong against
        if isinstance(attacker, type(self).strong_against):
            super().receive_damage(damage/2, attacker)
            print("Hah, the attack was not very effective.")
        elif isinstance(attacker, type(self).weak_against):
            super().receive_damage(damage*2, attacker)
            print("The attack was super effective! Ouch!")
        else:
            super().receive_damage(damage, attacker)

    def __str__(self):
        print("---")
        print(f"{self.trainer}'s {self.name}")
        print(f"Level: {self.level}, HP: {self.hp}/{self.max_hp}")
        print(f"Moves: {self.basic_attack}")
        print(f"Status: Paralyzed - {self.paralyzed}")
        print("---")
        return self.name


def main():
    # Instantiating Pokemon
    fight = Fighting("Machamp", "Brock")
    psy = Psychic("Alakazam", "Ash", 300)
    dark = Dark("Darkrai", "Brock")
    psy2 = Psychic("Mew", "Brock", 150)
    pokemon = Pokemon("Eevee", "Misty")

    # Testing Pokemon
    print("Psychic receives attacks from various types.")
    fight.attack(psy)
    dark.attack(psy)
    psy2.attack(psy)
    pokemon.attack(psy)
    print("--")
    print("Psychic attack results on various types.")
    psy.attack(fight)
    psy.attack(dark)
    psy.attack(psy2)
    psy.attack(pokemon)
    print("--")
    print("Testing paralysis + fainting.")
    fight.attack(psy)
    dark.attack(psy)
    pokemon.attack(psy)
    print("--")
    print("Checking all resulting stats using __str__.")
    str(psy)
    str(fight)
    str(dark)
    str(psy2)
    str(pokemon)


if __name__ == "__main__":
    main()

r"""
--- sample run of unit_test() ---
Psychic receives attacks from various types.
Machamp!
Machamp  used  Tackle on Alakazam !
Hah, the attack was not very effective.
Darkrai!
Darkrai  used  Tackle on Alakazam !
The attack was super effective! Ouch!
Mew!
Mew  used  Psychic Shift on Alakazam !
Eevee!
Eevee  used  Tackle on Alakazam !
--
Psychic attack results on various types.
Alakazam!
Alakazam  used  Psychic Shift on Machamp !
Machamp  fainted!
The attack was super effective!
Machamp is psycho-paralyzed!
...or at least would be if Machamp hadn't yet fainted.
Alakazam!
Alakazam  used  Psychic Shift on Darkrai !
The attack was not very effective...
Darkrai is psycho-paralyzed!
Alakazam!
Alakazam  used  Psychic Shift on Mew !
Alakazam!
Alakazam  used  Psychic Shift on Eevee !
Eevee is psycho-paralyzed!
--
Testing paralysis + fainting.
Machamp...?
Machamp has fainted and can't attack!
Darkrai!
Darkrai is paralyzed and can't attack!
Eevee!
Eevee is paralyzed and can't attack!
--
Checking all resulting stats using __str__.
---
Ash's Alakazam
Level: 1, HP: 120.0/300.0
Moves: Psychic Shift
Status: Paralyzed - False
---
---
Brock's Machamp
Level: 1, HP: 0/50.0
Moves: Tackle
Status: Paralyzed - False
---
---
Brock's Darkrai
Level: 1, HP: 30.0/50.0
Moves: Tackle
Status: Paralyzed - True
---
---
Brock's Mew
Level: 1, HP: 110.0/150.0
Moves: Psychic Shift
Status: Paralyzed - False
---
---
Misty's Eevee
Level: 1, HP: 10.0/50.0
Moves: Tackle
Status: Paralyzed - True
---
"""