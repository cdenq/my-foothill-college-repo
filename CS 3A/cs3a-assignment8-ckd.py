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
        self._zips = []
        self._times = []

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
        """ Turn loaded data into sets and populates self.lists. """
        zip_set = {i[0] for i in self._data}
        time_set = {i[1] for i in self._data}
        self._zips = list(zip_set)
        self._times = list(time_set)
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
                             (entry[0] == descriptor_one) &
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

            for i in range(len(self._times) + 1):  # Create header row
                if i == 0:
                    print(f"       ", end="")
                else:
                    print(f" {self._times[i - 1]:>{chr_width}}", end="")
            print(f"\n", end="")

            for j in range(len(self._zips)):  # Create rest of body rows
                print(f"{self._zips[j]:{chr_width}}", end="")
                for k in range(0, 3):
                    try:
                        calc = self._cross_table_statistics(self._zips[j],
                                                            self._times[k])
                        print(f" {calc[stat]:7.2f}", end="")
                    except NoMatchingItemsError:
                        print("     N/A", end="")
                if j != len(self._zips):
                    print(f"\n", end="")


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
            my_dataset.display_cross_table(Stats.AVG.value)
        elif user_input_as_int == 2:
            my_dataset.display_cross_table(Stats.MIN.value)
        elif user_input_as_int == 3:
            my_dataset.display_cross_table(Stats.MAX.value)
        elif user_input_as_int == 4:
            print("Sorry, option 4 is not yet implemented!")
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
Please input your name.John Smith
John Smith, welcome to the Air Quality Database.
Please input a header fewer than 30 characters.Purple Air Header

Purple Air Header
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.1
Please load the data first (option 5)!

Purple Air Header
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.5

Purple Air Header
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.1
        Morning Evening  Midday
94040      2.00     N/A     N/A
12345      1.10     N/A     N/A
94022      2.20    3.20    1.00

Purple Air Header
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.2
        Morning Evening  Midday
94040      1.00     N/A     N/A
12345      1.10     N/A     N/A
94022      2.20    3.20    1.00

Purple Air Header
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.3
        Morning Evening  Midday
94040      3.00     N/A     N/A
12345      1.10     N/A     N/A
94022      2.20    3.20    1.00

Purple Air Header
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.
'' is not a number, try again.

Purple Air Header
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.4
Sorry, option 4 is not yet implemented!

Purple Air Header
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.9
Goodbye, and thank you for using Purple Air Header!
"""