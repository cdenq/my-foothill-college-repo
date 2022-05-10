""" Allow the user to input their name, get greeting, and then see menu
options. Continuously loop through menu options until a valid one is
chosen (valid = integer).
"""


class DataSet:
    def __init__(self, header="yeye"):
        """  Initialize the class objects with header as string. """
        self._header = header
        self._data = None


def print_menu():
    """ Print all the menu options. """
    print("Main Menu")
    print("1 - Print Average Particulate Concentration by Zip Code and Time")
    print("2 - Print Minimum Particulate Concentration by Zip Code and Time")
    print("3 - Print Maximum Particulate Concentration by Zip Code and Time")
    print("4 - Adjust Zip Code Filters")
    print("5 - Load Data")
    print("9 - Quit")


def menu(my_dataset: DataSet):
    """ Continuously ask the user for menu options until a valid one is
    picked, giving different responses to each specific user input.
    """
    while True:
        print("")  # Inserted to match formatting of sample response
        print(my_dataset._header)
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
        elif user_input_as_int == 2:
            print("Sorry, option 2 is not yet implemented!")
        elif user_input_as_int == 3:
            print("Sorry, option 3 is not yet implemented!")
        elif user_input_as_int == 4:
            print("Sorry, option 4 is not yet implemented!")
        elif user_input_as_int == 5:
            print("Sorry, option 5 is not yet implemented!")
        else:
            print("Hey,", user_input_as_int, "is not even on the list!")
    print("Goodbye, and thank you for picking 9!")


def main():
    """ Inquire user's name, welcome them, and then run menu(). """
    print("Welcome to Christopher's first OOP program!")
    user_name = input("Please input your name.")
    print(user_name, ", welcome to the Air Quality Database.", sep="")
    user_header = input("What is the name of the header?")
    if user_header == "":
        purple_air = DataSet()
    else:
        purple_air = DataSet(user_header)
    menu(purple_air)


if __name__ == "__main__":
    main()

r"""
--- sample run #1 ---
Welcome to Christopher's first OOP program!
Please input your name.John
John, welcome to the Air Quality Database.
What is the name of the header?Purple Air

Purple Air
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.1
Sorry, option 1 is not yet implemented!

Purple Air
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
What is the name of the header?%&*@#^%*$&#

%&*@#^%*$&#
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.9999999
Hey, 9999999 is not even on the list!

%&*@#^%*$&#
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