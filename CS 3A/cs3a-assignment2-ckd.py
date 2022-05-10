""" Type Conversions and Exception Handling module that allows the user
to input their name, get greeting, and then see menu options. User then
inputs a response that is validated as integer or raised as exception.
statement.
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
    """ Runs print_menu() and try/except user's input into integer."""
    print_menu()
    user_input = input("What menu option do you want?")
    try:
        int(user_input)
    except ValueError:
        print("'", user_input, "' is not a number, please try again.", sep="")


def main():
    """ Inquires user's name, welcomes them, and then runs menu(). """
    print("Welcome to Christopher's first OOP program!")
    user_name = input("Please input your name.")
    print(user_name, ", welcome to the Air Quality Database. \n", sep="")
    menu()


if __name__ == "__main__":
    main()

r"""
--- valid sample run #1 ---
Welcome to Christopher's first OOP program!
Please input your name.John Smith
John Smith, welcome to the Air Quality Database. 

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What menu option do you want?4

--- invalid sample run #2 ---
Welcome to Christopher's first OOP program!
Please input your name.John Smith
John Smith, welcome to the Air Quality Database. 

Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
What menu option do you want?four
'four' is not a number, please try again.
"""