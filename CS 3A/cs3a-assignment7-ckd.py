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
    my_dataset = DataSet()
    my_dataset.load_default_data()
    print("The following Zip Codes are loaded:")
    for zip_code in my_dataset._zips:
        print(zip_code)
    print("The following Times of Day are loaded:")
    for time_of_day in my_dataset._times:
        print(time_of_day)
    my_zip = "94040"
    my_time = "Morning"
    data_tuple = my_dataset._cross_table_statistics(my_zip, my_time)
    for item in Stats:
        print(f"The {item.name} for {my_zip}, {my_time} is {data_tuple[item.value]}.")
    return


if __name__ == "__main__":
    unit_tester()
    # main() is commented out for the assignment

r"""
--- sample run #1 ---
The following Zip Codes are loaded:
94022
94040
12345
The following Times of Day are loaded:
Evening
Morning
Midday
The MIN for 94040, Morning is 1.0.
The AVG for 94040, Morning is 2.0.
The MAX for 94040, Morning is 3.0.
"""