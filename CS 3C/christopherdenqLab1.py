""" An object-oriented program that maintains a list of favorite movies.
Program provides menu that will allow client to: list movies, add movie,
delete movie.

This is the code solution.

Christopher Denq
CS 3C, 2022
Lab 1
"""


class Movie:
    """ Create a Movie class that models a movie list application. Class
    will allow for getting from, adding to, and deleting from its data.
    """
    # List of all made movies
    __movie_list = []

    # "New Default Values"
    DEFAULT_NAME = "Default Movie"
    DEFAULT_YEAR = 2000

    def __init__(self, name: str = DEFAULT_NAME, year: int = DEFAULT_YEAR):
        """  Initialize instance of Movie, default values provided. """
        self.name = name
        self.year = year

    @staticmethod
    def strOK(value):
        """  Validate str parameters (<= 50 chars, whitespace included).
        """
        if not (len(value) <= 50):
            print(f"{value} is over 50 characters.")
            return False
        elif not (value.isprintable()):
            print(f"{value} is non-printable.")
            return False
            # Note: Since the value being passed into strOK is obtained with a
            # Python input function, I don't think it's possible to have a non-
            # printable character here
        else:
            return True

    # Added this extra helper to further condense code
    @staticmethod
    def intOK(value):
        """  Change value to integer type, if able. """
        try:
            return int(value)
        except ValueError:
            print(f"{value} is not an integer nor can it be changed into one.")
            return False

    @staticmethod
    def yearOK(value):
        """  Validate year parameters (1000 <= year <= 2023). """
        # Convert value into integer, if able
        value = Movie.intOK(value)

        # Perform year checks
        if not value:
            return False
        elif 1000 <= value <= 2023:
            return True
        else:
            print(f"{value} is not between 1000 and 2023.")
            return False

    # Added this extra helper to further condense code
    def listEmpty(self):
        """  Check if the current movie list is empty. """
        if self.__movie_list:
            return True
        else:
            print("Movie list is currently empty.")
            return False

    def getName(self):
        return self.name

    def setName(self):
        ans = input("Name:")
        if Movie.strOK(ans):
            self.name = ans
            return True
        else:
            self.name = self.DEFAULT_NAME  # Default value if fails
            return False

    def getYear(self):
        return self.year

    def setYear(self):
        ans = input("Year:")
        if Movie.yearOK(ans):
            self.year = ans
            return True
        else:
            self.year = self.DEFAULT_YEAR  # Default value if fails
            return False

    def getStr(self):
        """  Convert the current movie information into string. """
        return f"{self.getName()} ({self.getYear()})"

    def add(self):
        """  Prompt changes to movie name and title and then adds to
        list.
        """
        # Prompt name and year changes
        if self.setName() and self.setYear():
            # And if both are successful, go ahead and make change to list
            self.__movie_list.append(self.getStr())
            print(f"{self.getStr()} was added.")
        # Otherwise, if there is any failure at any point, make no change
        else:
            print("Nothing was added.")
        print("")  # Add another newline for spacing
        return

    def delete(self):
        """  Delete a movie from the movie list. """
        # Check if movie list has at least 1 entry before proceeding
        if self.listEmpty():
            # Ask for movie list number and then convert if possible
            ans = input("Number:")
            ans = Movie.intOK(ans)

            # If given input value not an integer (aka returns False, aka 0) OR
            # given input value is below the first item on list OR is higher
            # than first item on the list
            if ans <= 0 or ans > len(self.__movie_list):
                print(f"{ans} is not a valid number (too low, too high, or "
                      f"just not an integer); nothing is deleted.")
            # Else, given input value is on the list
            else:
                print(f"{self.__movie_list[ans - 1]} was deleted.")
                self.__movie_list.pop(ans - 1)
        print("")  # Add another newline for spacing
        return

    def list(self):
        """  Return current movie list. """
        # Check if movie list has at least 1 entry before printing
        if self.listEmpty():
            for i in range(len(self.__movie_list)):
                print(f"{i + 1}. {self.__movie_list[i]}")
        print("")  # Add another newline for spacing
        return


def helperMenu():
    """  Display a command selection menu for user interaction. """
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print("")  # Add another newline for spacing
    return


def main():
    return


if __name__ == "__main__":
    main()
