"""
The main module to play the PokeGame.
- Christopher Denq
"""
from pokegame import *
import random as rand
# The drawn pokemon for opponent is random; setting the random seed to
# make testing consistent.
rand.seed(42)


def opponent_gen():
    print("Creating and drawing Pokemon!")
    game = PokeGame()
    drawn = game.draw_pokemon()
    drawn.trainer = "Opponent"
    print(drawn)
    return drawn


def menu():
    print("Now your turn to pick a Pokemon.")
    while True:
        ans = input("0 - Pokemon\n"
                    "1 - Psychic\n"
                    "2 - Ghost\n"
                    "3 - Fairy\n"
                    "4 - Poison\n"
                    "Which Pokemon class do you want?")
        if ans not in ["0", "1", "2", "3", "4"]:
            print("Please pick a valid response.")
        else:
            break
    new = your_pokemon(ans)
    print("This is your new Pokemon!")
    print(new)
    return new

def your_pokemon(ans):
    if ans == "0":
        your_poke = Pokemon("Normal Ditto", "Me", 500)
    elif ans == "1":
        your_poke = Psychic("Psychic Ditto", "Me", 500)
    elif ans == "2":
        your_poke = GhostType("Ghost Ditto", "Me", 500)
    elif ans == "3":
        your_poke = FairyType("Fairy Ditto", "Me", 500)
    else:
        your_poke = Poison("Poison Ditto", "Me", 500)
    return your_poke


def main():
    you = menu()
    for i in range(0,7):
        print(f"-------------------Round {i+1}")
        opp = opponent_gen()
        you.attack(opp)
        opp.attack(you)
        print(you)
        print("Moving onto next round, healing status effects.")
        you.paralyzed = False
    print("You survived all 7 opponent's pokemon!")
    return


if __name__ == "__main__":
    main()

r"""
--- sample run of unit_test() ---

"""