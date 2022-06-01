""" Allow the user to input their name, get greeting, and then see menu
options with a header of their input choice. Continuously loop through
asking for header names and menu options until a valid one is picked.
"""


from enum import Enum


class EmptyDatasetError(Exception):
    pass


class NoMatchingItemsError(Exception):
    pass


class Stats(Enum):
    MIN = 0
    AVG = 1
    MAX = 2


class DataSet:

    max_header_length = 30

    def __init__(self, header=""):
        """  Initialize the class objects with header as string. """
        self.header = header
        self._data = None
        self._zips = {}
        self._times = []

    def get_zips(self):
        """  Return dictionary of zip codes. """
        return self._zips

    def toggle_zip(self, target_zip: str):
        """  Flip the value of specified zip code to T if F, F if T. """
        if target_zip not in self._zips:
            raise LookupError
        else:
            self._zips[target_zip] = not self._zips[target_zip]

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, new_header: str):
        if len(new_header) > DataSet.max_header_length:
            raise ValueError("Too long; try again.")
        else:
            self._header = new_header
        return

    def _initialize_labels(self):
        """ Populate self._ with properly formatted loaded data. """
        time_set = {i[1] for i in self._data}
        self._times = list(time_set)
        self._zips = {}
        for i in range(len(self._data)):
            self._zips[self._data[i][0]] = True
        return

    def load_default_data(self):
        """ Manually load the self._data. """
        self._data = [("12345", "Morning", 1.1),
                      ("94022", "Morning", 2.2),
                      ("94040", "Morning", 3.0),
                      ("94022", "Midday", 1.0),
                      ("94040", "Morning", 1.0),
                      ("94022", "Evening", 3.2)]
        self._initialize_labels()
        return

    def _cross_table_statistics(self,
                                descriptor_one: str,
                                descriptor_two: str) -> tuple:
        """ Filter out the matching items; calculate min, avg, max; and
        return the values in a tuple.

        Args:
            descriptor_one (str): Zip code
            descriptor_one (str): Time of day
        Returns:
            tuple: (min, avg, max)
        """
        if not self._data:
            raise EmptyDatasetError
        else:
            matching_data = [entry[2] for entry in self._data if
                             (entry[0] == descriptor_one) and
                             (entry[1] == descriptor_two)]
            if len(matching_data) == 0:
                raise NoMatchingItemsError
            else:
                min_data = min(matching_data)
                avg_data = sum(matching_data) / len(matching_data)
                max_data = max(matching_data)
                tuple_values = (min_data, avg_data, max_data)
                return tuple_values

    def display_cross_table(self, stat: Stats):
        """ Generate a display table of the queried value.

        Args:
            stat (Stats object): Enum class attribute that is our query value
        Returns:
            print statement: displayed table of queried value
        """
        if not self._data:
            print("Please load the data first (option 5)!")
        else:
            chr_width = 7

            # HEADER row
            for i in range(len(self._times) + 1):
                if i == 0:
                    print(f"       ", end="")
                else:
                    print(f" {self._times[i - 1]:>{chr_width}}", end="")
            print(f"\n", end="")

            # BODY rows
            for index, (key, value) in enumerate(self._zips.items()):
                if value:
                    print(f"{key:{chr_width}}", end="")
                    for k in range(0, 3):
                        try:
                            calc = self._cross_table_statistics(key,
                                                                self._times[k])
                            print(f" {calc[stat.value]:7.2f}", end="")
                        except NoMatchingItemsError:
                            print("     N/A", end="")
                    if index != len(self._zips):
                        print(f"\n", end="")


def manage_filters(my_dataset: DataSet):
    """ Print zip code filter menu and continuously ask the user for
    zip codes to change until user is done.
    """
    dict_of_zips = my_dataset.get_zips()
    if not dict_of_zips:
        print("This dataset is empty; please load data first.")
    else:
        while True:
            # PRINT ZIPCODE TABLE
            print("The following labels are in the dataset:")
            for index, element in enumerate(dict_of_zips, 1):
                readable_output = "ACTIVE" if dict_of_zips[element] is True\
                                   else "INACTIVE"
                print(f"{index}: {element:<10} {readable_output}")

            # ASK FOR ZIP CHANGE
            user_input = input("Select an item to toggle or press enter/return"
                               " to quit.")
            if user_input == "":
                print("Done adjusting filters; returning to Main Menu.")
                break
            else:
                try:
                    user_input_as_int = int(user_input)
                except ValueError:
                    print("'", user_input, "' is not an valid number.", sep="")
                    continue
                if user_input_as_int not in range(1, len(dict_of_zips)+1):
                    print("'", user_input, "' is not a menu item.", sep="")
                    continue
                else:
                    for index, element in enumerate(dict_of_zips, 1):
                        if user_input_as_int == index:
                            my_dataset.toggle_zip(element)
                            break


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
            my_dataset.display_cross_table(Stats.AVG)
        elif user_input_as_int == 2:
            my_dataset.display_cross_table(Stats.MIN)
        elif user_input_as_int == 3:
            my_dataset.display_cross_table(Stats.MAX)
        elif user_input_as_int == 4:
            manage_filters(my_dataset)
        elif user_input_as_int == 5:
            my_dataset.load_default_data()
        else:
            print("Hey,", user_input_as_int, "is not even on the list!")
    print(f"Goodbye, and thank you for using {my_dataset.header}!")


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


if __name__ == "__main__":
    main()


r"""
--- sample run #1 ---
Welcome to Christopher's first OOP program!
Please input your name.Gordo Rammy
Gordo Rammy, welcome to the Air Quality Database.
Please input a header fewer than 30 characters.Gordon Ramsay Lambsauce

Gordon Ramsay Lambsauce
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.4
This dataset is empty; please load data first.

Gordon Ramsay Lambsauce
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.5

Gordon Ramsay Lambsauce
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.1
        Morning  Midday Evening
12345      1.10     N/A     N/A
94022      2.20    1.00    3.20
94040      2.00     N/A     N/A

Gordon Ramsay Lambsauce
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.4
The following labels are in the dataset:
1: 12345      ACTIVE
2: 94022      ACTIVE
3: 94040      ACTIVE
Select an item to toggle or press enter/return to quit.1
The following labels are in the dataset:
1: 12345      INACTIVE
2: 94022      ACTIVE
3: 94040      ACTIVE
Select an item to toggle or press enter/return to quit.
Done adjusting filters; returning to Main Menu.

Gordon Ramsay Lambsauce
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.1
        Morning  Midday Evening
94022      2.20    1.00    3.20
94040      2.00     N/A     N/A

Gordon Ramsay Lambsauce
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.4
The following labels are in the dataset:
1: 12345      INACTIVE
2: 94022      ACTIVE
3: 94040      ACTIVE
Select an item to toggle or press enter/return to quit.2
The following labels are in the dataset:
1: 12345      INACTIVE
2: 94022      INACTIVE
3: 94040      ACTIVE
Select an item to toggle or press enter/return to quit.3
The following labels are in the dataset:
1: 12345      INACTIVE
2: 94022      INACTIVE
3: 94040      INACTIVE
Select an item to toggle or press enter/return to quit.
Done adjusting filters; returning to Main Menu.

Gordon Ramsay Lambsauce
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.1
        Morning  Midday Evening

Gordon Ramsay Lambsauce
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.4
The following labels are in the dataset:
1: 12345      INACTIVE
2: 94022      INACTIVE
3: 94040      INACTIVE
Select an item to toggle or press enter/return to quit.1
The following labels are in the dataset:
1: 12345      ACTIVE
2: 94022      INACTIVE
3: 94040      INACTIVE
Select an item to toggle or press enter/return to quit.
Done adjusting filters; returning to Main Menu.

Gordon Ramsay Lambsauce
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.1
        Morning  Midday Evening
12345      1.10     N/A     N/A

Gordon Ramsay Lambsauce
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.4
The following labels are in the dataset:
1: 12345      ACTIVE
2: 94022      INACTIVE
3: 94040      INACTIVE
Select an item to toggle or press enter/return to quit.0
'0' is not a menu item.
The following labels are in the dataset:
1: 12345      ACTIVE
2: 94022      INACTIVE
3: 94040      INACTIVE
Select an item to toggle or press enter/return to quit.4
'4' is not a menu item.
The following labels are in the dataset:
1: 12345      ACTIVE
2: 94022      INACTIVE
3: 94040      INACTIVE
Select an item to toggle or press enter/return to quit.-2
'-2' is not a menu item.
The following labels are in the dataset:
1: 12345      ACTIVE
2: 94022      INACTIVE
3: 94040      INACTIVE
Select an item to toggle or press enter/return to quit.1.1
'1.1' is not an valid number.
The following labels are in the dataset:
1: 12345      ACTIVE
2: 94022      INACTIVE
3: 94040      INACTIVE
Select an item to toggle or press enter/return to quit.wheres the lambsauce???
'wheres the lambsauce???' is not an valid number.
The following labels are in the dataset:
1: 12345      ACTIVE
2: 94022      INACTIVE
3: 94040      INACTIVE
Select an item to toggle or press enter/return to quit.
Done adjusting filters; returning to Main Menu.

Gordon Ramsay Lambsauce
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.9
Goodbye, and thank you for using Gordon Ramsay Lambsauce!
"""