"""
This module was edited to make testing more clear + realistic to the
games. Eg) Before, Pokemon could still attack while fainted; the edits
to this module correct "bugs" like that.
- Christopher Denq
"""
class Pokemon:
    basic_attack = 'Tackle'
    damage = 40

    def __init__(self, name, trainer, hp=50):
        self.name = name
        self.trainer = trainer
        self.level = 1
        self.max_hp = float(hp)
        self.hp = float(hp)
        self.paralyzed = False

    def speak(self):
        print(self.name + '!')

    def attack(self, other):
        if not self.paralyzed and self.hp > 0:
            self.speak()
            print(self.name, ' used ', self.basic_attack, 'on', other.name,
                  '!')
            other.receive_damage(type(self).damage, self)
        elif self.paralyzed:
            self.speak()
            print(f"{self.name} is paralyzed and can't attack!")
        else:
            print(f"{self.name}...?")
            print(f"{self.name} has fainted and can't attack!")
   
    def receive_damage(self, damage, attacker):
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
                print(self.name, ' fainted!')

    def __str__(self):
        print("---")
        print(f"{self.trainer}'s {self.name}")
        print(f"Level: {self.level}, HP: {self.hp}/{self.max_hp}")
        print(f"Moves: {self.basic_attack}")
        print(f"Status: Paralyzed - {self.paralyzed}")
        print("---")
        return self.name