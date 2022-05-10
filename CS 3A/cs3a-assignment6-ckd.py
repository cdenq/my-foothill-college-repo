""" Allow the user to input their name, get greeting, and then see menu
options with a header of their input choice. Continuously loop through
asking for header names and menu options until a valid one is picked.
"""


class EmptyDatasetError(Exception):
    pass


class NoMatchingItemsError(Exception):
    pass


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
            raise ValueError("Too long; try again.")
        else:
            self._header = new_header
        return

    def load_default_data(self):
        """ Manually load the self._data. """
        self._data = [("12345", "Morning", 1.1),
                      ("94022", "Morning", 2.2),
                      ("94040", "Morning", 3.0),
                      ("94022", "Midday", 1.0),
                      ("94040", "Morning", 1.0),
                      ("94022", "Evening", 3.2)]
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
    my_set = DataSet()

    # my_set._cross_table_statistics() -> EmptyDatasetError
    try:
        my_set._cross_table_statistics("94023", "Night")
        print("unloaded data + run method returns: FAILED")
    except EmptyDatasetError:
        print("unloaded data + run method raises Empty: SUCCESS")
    except NoMatchingItemsError:
        print("unloaded data + run method raises NoMatch: FAILED")
    except:
        print("unloaded data + run method raises unknown error: FAILED")

    my_set.load_default_data()

    # my_set._cross_table_statistics("94022", "Supper") -> NoMatchingItemsError
    try:
        my_set._cross_table_statistics("94022", "Supper")
        print("loaded data + run method(valid, invalid) returns: FAILED")
    except EmptyDatasetError:
        print("loaded data + run method(valid, invalid) raises Empty: FAILED")
    except NoMatchingItemsError:
        print("loaded data + run method(valid, invalid) raises NoMatch: "
              "SUCCESS")
    except:
        print("loaded data + run method(valid, invalid) raises unknown error: "
              "FAILED")

    # my_set._cross_table_statistics("94023", "Night") -> NoMatchingItemsError
    try:
        my_set._cross_table_statistics("94023", "Night")
        print("loaded data + run method(invalid, valid) returns: FAILED")
    except EmptyDatasetError:
        print("loaded data + run method(invalid, valid) raises Empty: FAILED")
    except NoMatchingItemsError:
        print("loaded data + run method(invalid, valid) raises NoMatch: "
              "SUCCESS")
    except:
        print("loaded data + run method(invalid, valid) raises unknown error: "
              "FAILED")

    # my_set._cross_table_statistics("94040", "Night") -> NoMatchingItemsError
    try:
        my_set._cross_table_statistics("94040", "Night")
        print("loaded data + run method(valid, valid) no match returns: "
              "FAILED")
    except EmptyDatasetError:
        print("loaded data + run method(valid, valid) no match raises Empty: "
              "FAILED")
    except NoMatchingItemsError:
        print("loaded data + run method(valid, valid) no match raises NoMatch:"
              " SUCCESS")
    except:
        print("loaded data + run method(valid, valid) no match raises unknown"
              "error: FAILED")

    # my_set._cross_table_statistics("12345", "Morning") -> (1.1, 1.1, 1.1)
    try:
        test_1 = my_set._cross_table_statistics("12345", "Morning")
    except EmptyDatasetError:
        print("loaded data + run method(valid, valid) 1 match raises Empty: "
              "FAILED")
    except NoMatchingItemsError:
        print("loaded data + run method(valid, valid) 1 match raises NoMatch:"
              " FAILED")
    except:
        print("loaded data + run method(valid, valid) 1 match raises unknown "
              "error: FAILED")
    else:
        if test_1 == (1.1, 1.1, 1.1):
            print("loaded data + run method(valid, valid) 1 match returns value: "
                  "SUCCESS")
        else:
            print("loaded data + run method(valid, valid) 1 match returns wrong"
                  "value: FAILED")


    # my_set._cross_table_statistics("94040", "Morning") -> (1, 2, 3)
    try:
        test_2 = my_set._cross_table_statistics("94040", "Morning")
    except EmptyDatasetError:
        print("loaded data + run method(valid, valid) 1+ match raises Empty: "
              "FAILED")
    except NoMatchingItemsError:
        print("loaded data + run method(valid, valid) 1+ match raises NoMatch:"
              " FAILED")
    except:
        print("loaded data + run method(valid, valid) 1+ match raises unknown "
              "error: FAILED")
    else:
        if test_2 == (1, 2, 3):
            print("loaded data + run method(valid, valid) 1+ match returns value: "
                  "SUCCESS")
        else:
            print("loaded data + run method(valid, valid) 1+ match returns wrong"
                  "value: FAILED")


if __name__ == "__main__":
    unit_tester()
    # main() is commented out for the assignment

r"""
--- sample run #1 ---
unloaded data + run method raises Empty: SUCCESS
loaded data + run method(valid, invalid) raises NoMatch: SUCCESS
loaded data + run method(invalid, valid) raises NoMatch: SUCCESS
loaded data + run method(valid, valid) no match raises NoMatch: SUCCESS
loaded data + run method(valid, valid) 1 match returns value: SUCCESS
loaded data + run method(valid, valid) 1+ match returns value: SUCCESS
"""