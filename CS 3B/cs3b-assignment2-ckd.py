""" This module allows instance creation from Monkey class, which
is an object with attributes such as type and temperature, as well as,
built-in functions to access and mutate those attributes. Monkey idea is
sourced from Emily Macway (as per assignment instructions), but edits to
code were made by Christopher Denq.
"""


class Monkey:
    """ Create a Monkey class with animal type, ID tag, and min and max
    temperature attributes.
    """
    def __init__(self,
                 id_tag: str = '000',
                 animal_type: str = 'Monkey',
                 min_temp: int = 45,
                 max_temp: int = 85):
        """  Initialize instance of Monkey, default values provided. """
        self._id_tag = id_tag
        self._animal_type = animal_type
        self._min_temp = min_temp
        self._max_temp = max_temp

    def get_animal_type(self):
        """  Return instance's animal_type. """
        return self._animal_type

    def get_id_tag(self):
        """  Return instance's id_tag. """
        return self._id_tag

    def set_id_tag(self, an_id_tag: str):
        """  Set instance's id_tag to given string. """
        self._id_tag = an_id_tag
        return

    def get_min_temp(self):
        """  Return instance's min_temp. """
        return self._min_temp

    def get_max_temp(self):
        """  Return instance's max_temp. """
        return self._max_temp


class Dodo:
    """ Create a Dodo class with animal type, ID tag, and min and max
    temperature attributes.
    """

    def __init__(self,
                 id_tag: str = '000',
                 animal_type: str = 'Dodo',
                 min_temp: int = 61.5,
                 max_temp: int = 84.6):
        """  Initialize instance of Dodo object with default values. """
        self._id_tag = id_tag
        self._animal_type = animal_type
        self._min_temp = min_temp
        self._max_temp = max_temp

    def get_animal_type(self):
        """  Return instance's animal_type. """
        return self._animal_type

    def get_id_tag(self):
        """  Return instance's id_tag. """
        return self._id_tag

    def set_id_tag(self, an_id_tag: str):
        """  Set instance's id_tag to given string. """
        self._id_tag = an_id_tag
        return

    def get_min_temp(self):
        """  Return instance's min_temp. """
        return self._min_temp

    def get_max_temp(self):
        """  Return instance's max_temp. """
        return self._max_temp


def main():
    #  Loading objects into list.
    steve_the_dodo = Dodo('001')
    jim_the_monkey = Monkey('002')
    darwin_the_dodo = Dodo('003')
    francis_the_monkey = Monkey('004')
    petting_zoo = [steve_the_dodo,
                   jim_the_monkey,
                   darwin_the_dodo,
                   francis_the_monkey]

    #  Searching by valid and then invalid ID.
    search_ids = ['003', '999']
    for animal_id in search_ids:
        print(f"Welcome to our petting zoo! We will search for animal"
              f" {animal_id} now.")
        is_found = False
        for animal in petting_zoo:
            if animal.get_id_tag() == animal_id:
                print(f"Found!")
                print(f"Animal {animal.get_id_tag()} is a "
                      f"{animal.get_animal_type()}, which lives in a place that"
                      f" goes from {animal.get_min_temp()} to "
                      f"{animal.get_max_temp()}.")
                is_found = True
                break
        if not is_found:
            print(f"Sorry, we couldn't find {animal_id}.")
        print("Thanks for coming to our petting zoo; goodbye!")
        print("--------------")
    return


if __name__ == "__main__":
    main()

r"""
--- sample run of unit_test() ---
Welcome to our petting zoo! We will search for animal 003 now.
Found!
Animal 003 is a Dodo, which lives in a place that goes from 61.5 to 84.6.
Thanks for coming to our petting zoo; goodbye!
--------------
Welcome to our petting zoo! We will search for animal 999 now.
Sorry, we couldn't find 999.
Thanks for coming to our petting zoo; goodbye!
--------------
"""