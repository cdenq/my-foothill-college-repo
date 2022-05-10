""" Allows the user to input their name, get greeting, and then see menu
options. User then inputs a response that is validated as integer or
raised as exception statement. Module will continuously loop through
menu options until a valid one is chosen.
"""


def print_menu():
    """ Prints all the menu options. """
    print("Main Menu")
    print("1 - Print Average Particulate Concentration by Zip Code and Time")
    print("2 - Print Minimum Particulate Concentration by Zip Code and Time")
    print("3 - Print Maximum Particulate Concentration by Zip Code and Time")
    print("4 - Adjust Zip Code Filters")
    print("5 - Load Data")
    print("9 - Quit")


def menu():
    """ Continuously asks user for menu options until a valid one is picked.
    'Valid' is the number 9. Will give different responses to user inputs that
    are integers on the menu, integers not on the menu, and non-integers.
    """
    while True:
        print("")  # Inserted to match formatting of sample response
        print_menu()
        user_input = input("Please pick a menu option.")
        try:
            user_input_as_int = int(user_input)
        except ValueError:
            print("'", user_input, "' is not a number, try again.", sep="")
            continue
        if user_input_as_int == 9:
            break
        elif user_input_as_int == 1:
            print("Sorry, option 1 is not yet implemented!")
            continue
        elif user_input_as_int == 2:
            print("Sorry, option 2 is not yet implemented!")
            continue
        elif user_input_as_int == 3:
            print("Sorry, option 3 is not yet implemented!")
            continue
        elif user_input_as_int == 4:
            print("Sorry, option 4 is not yet implemented!")
            continue
        elif user_input_as_int == 5:
            print("Sorry, option 5 is not yet implemented!")
            continue
        else:
            print("Hey,", user_input_as_int, "is not even on the list!")
            continue
    print("Goodbye, and thank you for picking 9!")


def main():
    """ Inquires user's name, welcomes them, and then runs menu(). """
    print("Welcome to Christopher's first OOP program!")
    user_name = input("Please input your name.")
    print(user_name, ", welcome to the Air Quality Database.", sep="")
    menu()


if __name__ == "__main__":
    main()

r"""
--- sample run #1 ---
Welcome to Christopher's first OOP program!
Please input your name.John
John, welcome to the Air Quality Database.

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.9
Goodbye, and thank you for picking 9!

--- sample run #2 ---
Welcome to Christopher's first OOP program!
Please input your name.John
John, welcome to the Air Quality Database.

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.1
Sorry, option 1 is not yet implemented!

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.999999
Hey, 999999 is not even on the list!

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.string
'string' is not a number, try again.

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.9
Goodbye, and thank you for picking 9!

--- sample run #3 ---
Welcome to Christopher's first OOP program!
Please input your name.John
John, welcome to the Air Quality Database.

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.1
Sorry, option 1 is not yet implemented!

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.2
Sorry, option 2 is not yet implemented!

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.3
Sorry, option 3 is not yet implemented!

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.4
Sorry, option 4 is not yet implemented!

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.5
Sorry, option 5 is not yet implemented!

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.9
Goodbye, and thank you for picking 9!
"""