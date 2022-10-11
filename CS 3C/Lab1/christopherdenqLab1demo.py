""" An object-oriented program that maintains a list of favorite movies.
Program provides menu that will allow client to: list movies, add movie,
delete movie.

This is the test driver.

Christopher Denq
CS 3C, 2022
Lab 1
"""


from christopherdenqLab1 import *


def main():
    # Setup program object
    test = Movie()

    # Run interactive section
    print("Welcome to Chris's Movie Lists!")
    print("")  # Add another newline for spacing
    while True:
        helperMenu()
        ans = input("Command:")
        if ans == "list":
            test.list()
        elif ans == "add":
            test.add()
        elif ans == "del":
            test.delete()
        elif ans == "exit":
            break
        else:
            print(f"{ans} is not a valid command. Please try again.")
            print("")  # Add another newline for spacing
    print("Thank you for using Chris's Movie Lists!")
    print("Bye!")
    return


if __name__ == "__main__":
    main()


r"""
----sample run----
Welcome to Chris's Movie Lists!

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:list
Movie list is currently empty.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:del
Movie list is currently empty.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:fake command
fake command is not a valid command. Please try again.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:add
Name:Movie with Long Name fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
Movie with Long Name fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff is over 50 characters.
Nothing was added.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:add
Name:Movie with Wrong Year P1
Year:3
3 is not between 1000 and 2023.
Nothing was added.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:add
Name:Movie with Wrong Year P2
Year:2000.5345
2000.5345 is not an integer nor can it be changed into one.
Nothing was added.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:add
Name:Movie with Wrong Year P3
Year:text
text is not an integer nor can it be changed into one.
Nothing was added.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:add
Name:LOTR: Fellowship of Ring
Year:2001
LOTR: Fellowship of Ring (2001) was added.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:add
Name:LOTR: Two Towers
Year:2002
LOTR: Two Towers (2002) was added.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:add
Name:LOTR: Return of King
Year:2003
LOTR: Return of King (2003) was added.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:list
1. LOTR: Fellowship of Ring (2001)
2. LOTR: Two Towers (2002)
3. LOTR: Return of King (2003)

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:del
Number:-1
-1 is not a valid number (too low, too high, or just not an integer); nothing is deleted.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:del
Number:999
999 is not a valid number (too low, too high, or just not an integer); nothing is deleted.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:del
Number:2.5
2.5 is not an integer nor can it be changed into one.
False is not a valid number (too low, too high, or just not an integer); nothing is deleted.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:del
Number:text
text is not an integer nor can it be changed into one.
False is not a valid number (too low, too high, or just not an integer); nothing is deleted.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:del
Number:2
LOTR: Two Towers (2002) was deleted.

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:list
1. LOTR: Fellowship of Ring (2001)
2. LOTR: Return of King (2003)

COMMAND MENU
list - List all movies
add -  Add a movie
del -  Delete a movie
exit - Exit program

Command:exit
Thank you for using Chris's Movie Lists!
Bye!
"""