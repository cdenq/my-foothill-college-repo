""" An object-oriented program that can extract a translation guide from
a text file. The translation guide is a dictionary, and we can test the
time complexity of dictionary functions.

This is the code solution.

Christopher Denq
CS 3C, 2022
Lab 2
"""


import timeit


class Translator:
    """ Create a Translator class that models a dynamic Latin-to-English
    translation service. Contains methods to initialize the dictionary
    and translate.
    """
    # List of all made movies
    DEFAULT_FILEPATH = "latin.txt"

    def __init__(self, filepath: str = DEFAULT_FILEPATH):
        """  Initialize instance of Translator, default value provided. """
        self.filepath = filepath
        self.dictionary = {}
        self.benchmark_times = []

    @staticmethod
    def check_filepath(filepath):
        """  Check validity of given filepath. """
        try:
            file_test = open(filepath, "r")
            file_test.close()
            return True
        except FileNotFoundError:
            return False

    def get_filepath(self):
        print(self.filepath)
        print(f"\n", end="")
        return

    def set_filepath(self):
        ans = input("New filepath:")
        if Translator.check_filepath(ans):
            self.filepath = ans
            print(f"{ans} added as new filepath!")
            print(f"\n", end="")
            return
        else:
            self.filepath = self.DEFAULT_FILEPATH  # Default value if fails
            print(f"{ans} doesn't exist; setting to default.")
            print(f"\n", end="")
            return

    def load(self):
        """  Read the stored filepath and extract dictionary. """
        if Translator.check_filepath(self.filepath):
            with open(self.filepath, "r") as file_object:
                file_reader = file_object.read().splitlines()
                for i in file_reader:
                    temp_list = i.split(", ")
                    self.dictionary[temp_list[0]] = temp_list[1]
                print("Load successful!")
        else:
            print("Load failed.")
        print(f"\n", end="")
        return

    def check_dictionary(self):
        """  Check if dictionary translation is loaded. Helper function.
        """
        if self.dictionary:
            return True
        else:
            print("Translations are not loaded; see Load command.")
            return False

    def get_dictionary(self):
        """  Print the entire dictionary. """
        if self.check_dictionary():
            entry = 1
            for k, v in self.dictionary.items():
                print(f"{entry}. {k}: {v}")
                entry += 1
        print(f"\n", end="")
        return

    def get_dict_entry(self, key):
        """  Fetch a specific entry in the dictionary. """
        try:
            return self.dictionary[key]
        except KeyError:
            return "<N/A>"

    def time_get_dict_entry(self, word):
        """  Fetch a specific entry in the dictionary under time. """
        start_time = timeit.default_timer()
        return_value = self.get_dict_entry(word)
        end_time = timeit.default_timer()
        self.benchmark_times.append(end_time - start_time)
        return return_value

    def get_benchmark_times(self):
        for i, v in enumerate(self.benchmark_times):
            print(f"Attempt {i}: {v}")
        print(f"Average: "
              f"{sum(self.benchmark_times) / len(self.benchmark_times)}")

    def translate(self):
        """  Ask user for words to translate. """
        if self.check_dictionary():
            self.benchmark_times = []
            print("Wiping previous benchmark times from memory!")
            ans = input("Enter a latin phrase (space-separated):")
            split_list = ans.split(" ")
            response_list = [self.time_get_dict_entry(word) for word in
                             split_list]
            print(f"Translation: {' '.join(response_list)}")
            print(f"\n", end="")
            # Print benchmarked times
            print("Attempt times:")
            self.get_benchmark_times()
        print(f"\n", end="")
        return


def helper_menu():
    """  Display a command selection menu for user interaction. """
    print("COMMAND MENU")
    print("1 - Manually set filepath (default value available)")
    print("2 - Check current filepath")
    print("3 - Load translation from filepath")
    print("4 - Print all translations")
    print("5 - Translate phrase")
    print("0 - Exit")
    print("")  # Add another newline for spacing
    return


def main():
    return


if __name__ == "__main__":
    main()
