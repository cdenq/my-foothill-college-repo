""" Dodo module that allows instance creation from Dodo class, which
is an object with attributes such as type and temperature, as well as,
built-in functions to access and mutate those attributes. - Chris Denq
"""


class Dodo:

    def __init__(self,
                 animal_type='dodo',
                 id_tag='12345',
                 min_temp=61.5,
                 max_temp=84.6):
        """  Initialize instance of Dodo object with default values. """
        self._animal_type = animal_type
        self._id_tag = id_tag
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
    return


def unit_test():
    steve_the_dodo = Dodo()
    print(steve_the_dodo.get_animal_type())
    print(steve_the_dodo.get_min_temp())
    print(steve_the_dodo.get_max_temp())
    print(steve_the_dodo.get_id_tag())
    steve_the_dodo.set_id_tag('54321')
    print(steve_the_dodo.get_id_tag())


if __name__ == "__main__":
    # unit_test()
    main()

r"""
--- sample run of unit_test() ---
dodo
61.5
84.6
12345
54321
"""