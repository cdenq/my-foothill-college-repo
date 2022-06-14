""" Allow the user to input name and table header name. Has options for
filtering specific data and then displaying table of summary statistics.
"""
from enum import Enum
import csv
filename = './purple_air.csv'


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

    def load_file(self):
        """ Automatically load the imported data from csv file. """
        with open(filename, "r") as file:
            csvreader = csv.reader(file)
            next(csvreader)
            full_list = [(row[1], row[4], float(row[5])) for row in csvreader]
        self._data = full_list
        self._initialize_labels()
        print(f"Successfully loaded {len(full_list)} lines.")
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
                    for k in range(len(self._times)):
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
    while True:
        dict_of_zips = my_dataset.get_zips()
        if not dict_of_zips:
            print("This dataset is empty; please load data first.")
        else:
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
            my_dataset.load_file()
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
Please input your name.Gordon Ramsay
Gordon Ramsay, welcome to the Air Quality Database.
Please input a header fewer than 30 characters.Kitchen Air Quality

Kitchen Air Quality
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.1
Please load the data first (option 5)!

Kitchen Air Quality
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.5
Successfully loaded 6147 lines.

Kitchen Air Quality
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.1
          Night  Midday Morning Evening
94028      1.58    2.92    1.54    2.26
94304      1.23    2.89    1.36    1.17
94022      1.32    2.92    1.50    1.22
94024      1.69    3.27    1.71    3.42
94040      2.47    3.28    1.86    4.57
94087      2.31    3.92    2.24    4.77
94041      3.43    3.52    2.41    4.53
95014      2.19    3.29    1.06    2.38

Kitchen Air Quality
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.2
          Night  Midday Morning Evening
94028      0.00    0.00    0.00    0.00
94304      0.00    0.00    0.00    0.00
94022      0.00    0.00    0.00    0.00
94024      0.00    0.00    0.00    0.00
94040      0.00    0.00    0.00    0.00
94087      0.00    0.00    0.00    0.00
94041      0.00    0.00    0.00    0.00
95014      0.00    0.00    0.00    0.00

Kitchen Air Quality
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.3
          Night  Midday Morning Evening
94028     25.00   24.21   25.72   79.88
94304      9.92   20.93    9.66    9.73
94022     14.38   26.59   12.90   11.53
94024      9.67   29.17   15.12   37.57
94040     20.34   25.95   10.49   44.05
94087     13.14   26.48    9.39   38.11
94041     19.67   25.89    8.02   31.82
95014     37.82   25.00    9.95   69.05

Kitchen Air Quality
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.4
The following labels are in the dataset:
1: 94028      ACTIVE
2: 94304      ACTIVE
3: 94022      ACTIVE
4: 94024      ACTIVE
5: 94040      ACTIVE
6: 94087      ACTIVE
7: 94041      ACTIVE
8: 95014      ACTIVE
Select an item to toggle or press enter/return to quit.8
The following labels are in the dataset:
1: 94028      ACTIVE
2: 94304      ACTIVE
3: 94022      ACTIVE
4: 94024      ACTIVE
5: 94040      ACTIVE
6: 94087      ACTIVE
7: 94041      ACTIVE
8: 95014      INACTIVE
Select an item to toggle or press enter/return to quit.3
The following labels are in the dataset:
1: 94028      ACTIVE
2: 94304      ACTIVE
3: 94022      INACTIVE
4: 94024      ACTIVE
5: 94040      ACTIVE
6: 94087      ACTIVE
7: 94041      ACTIVE
8: 95014      INACTIVE
Select an item to toggle or press enter/return to quit.
Done adjusting filters; returning to Main Menu.

Kitchen Air Quality
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.3
          Night  Midday Morning Evening
94028     25.00   24.21   25.72   79.88
94304      9.92   20.93    9.66    9.73
94024      9.67   29.17   15.12   37.57
94040     20.34   25.95   10.49   44.05
94087     13.14   26.48    9.39   38.11
94041     19.67   25.89    8.02   31.82

Kitchen Air Quality
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
Please pick a menu option.9
Goodbye, and thank you for using Kitchen Air Quality!
"""