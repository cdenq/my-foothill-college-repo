""" Allow the user to input their name, get greeting, and then see menu
options with a header of their input choice. Continuously loop through
asking for header names and menu options until a valid one is picked.
"""


class DataSet:

    max_header_length = 30

    def __init__(self, header=""):
        """  Initialize the class objects with header as string. """
        self.header = header
        self._data = None

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, new_header: str):
        if len(new_header) > DataSet.max_header_length:
            raise ValueError(f"Too long; try again.")
        else:
            self._header = new_header
        return


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
        print(my_dataset.header)
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
    """ Inquire user's name, welcome them, ask for correct header name,
    and then run menu().
    """
    print("Welcome to Christopher's first OOP program!")
    user_name = input("Please input your name.")
    print(user_name, ", welcome to the Air Quality Database.", sep="")
    purple_air = DataSet()
    while True:
        user_header = input("Please input a header fewer than 30 characters.")
        try:
            purple_air.header = user_header
            break
        except ValueError:
            print("Try again; it's too long!")
            continue
    menu(purple_air)


def unit_tester():
    """ Print out successful unit tests before a trial run. """
    # constructor("") -> header = ""
    test_object_1 = DataSet()
    if test_object_1.header == "":
        print("Testing constructor with empty string: SUCCESS.")
    else:
        print("Testing constructor with empty string: FAILED.")

    # constructor("validstring") -> header = "validstring"
    test_object_2 = DataSet("validstring")
    if test_object_2.header == "validstring":
        print("Testing constructor with valid string: SUCCESS.")
    else:
        print("Testing constructor with valid string: FAILED.")

    # constructor(veryinvalidandlongstringthatisover30") -> ValueError
    try:
        test_object_3 = DataSet("veryinvalidandlongstringthatisover30")
        print("Testing constructor with invalid string: FAILED, no errors.")
    except ValueError:
        print("Testing constructor with invalid string: SUCCESS, ValueError.")

    # setter("newvalidstring") -> header = "newvalidstring"
    try:
        test_object_1.header = "newvalidstring"
        if test_object_1.header == "newvalidstring":
            print("Testing setter with valid assignment: SUCCESS, changed "
                  "header.")
        else:
            print("Testing setter with valid assignment: FAILED, changed header "
                  "incorrectly.")
    except ValueError:
        print("Testing setter with valid assignment: FAILED, ValueError.")

    # setter("veryinvalidandlongstringthatisover30") -> header unchanged
    try:
        test_object_1.header = "veryinvalidandlongstringthatisover30"
        print("Testing setter with invalid assignment: FAILED, changed "
              "header.")
    except ValueError:
        print("Testing setter with invalid assignment: SUCCESS, "
              "ValueError")


if __name__ == "__main__":
    unit_tester()
    main()

r"""
--- sample run #1 ---
Testing constructor with empty string: SUCCESS.
Testing constructor with valid string: SUCCESS.
Testing constructor with invalid string: SUCCESS, ValueError.
Testing setter with valid assignment: SUCCESS, changed header.
Testing setter with invalid assignment: SUCCESS, ValueError
Welcome to Christopher's first OOP program!
Please input your name.John
John, welcome to the Air Quality Database.
Please input a header fewer than 30 characters.Short Header

Short Header
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.9
Goodbye, and thank you for picking 9!

--- sample #2 ---
Testing constructor with empty string: SUCCESS.
Testing constructor with valid string: SUCCESS.
Testing constructor with invalid string: SUCCESS, ValueError.
Testing setter with valid assignment: SUCCESS, changed header.
Testing setter with invalid assignment: SUCCESS, ValueError
Welcome to Christopher's first OOP program!
Please input your name.John
John, welcome to the Air Quality Database.
Please input a header fewer than 30 characters.;flsdkjf;laksdjf;lkasdjf;lkjasdf;lkjasdf;ldkjsf;ldjsfjsfk
Try again; it's too long!
Please input a header fewer than 30 characters.;dkjsf;ldjsf;djsfsdf;asdklfj;asklfj;dlsfj;dlasg;dlasbgnd;ljsbfabefubaef
Try again; it's too long!
Please input a header fewer than 30 characters.okay short

okay short
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