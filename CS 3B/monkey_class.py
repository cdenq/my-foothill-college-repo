"""
Emily Macway
Zoo Animal Class assignment
CS 3B, Summer 2022
June 28, 2022
"""


class Monkey:
    """ Create a Monkey class with animal type, ID tag, and
    min and max temperature attributes"""
    def __init__(self):
        """initialize attributes """
        self.animalType = "Monkey"
        self.idTag = None
        self.minTemperature = 45  # chimp min temp in degrees F, from AZA
        self.maxTemperature = 85  # chimp max temp in degrees F, from AZA

    def getAnimalType(self):
        """ getter for Animal Type """
        return self.animalType

    def getIdTag(self):
        """ getter for ID Tag """
        return self.idTag

    def setIdTag(self, anIdTag):
        """ setter for ID Tag"""
        self.idTag = anIdTag

    def getMinTemperature(self):
        """getter for Minimum Temperature"""
        return self.minTemperature

    def getMaxTemperature(self):
        """getter for Macimum Temperature"""
        return self.maxTemperature


def main():
    """ Unit test for instance of Monkey class"""
    my_monkey = Monkey()  # instantiate
    type = my_monkey.getAnimalType()  # set type variable to "Monkey"
    my_monkey.setIdTag("12345")  # set ID Tag
    tag = my_monkey.getIdTag()  # set tag variable to "12345"
    min_temp = my_monkey.getMinTemperature() # set min temp to 45
    max_temp = my_monkey.getMaxTemperature() # set max temp to 85

    print(f"There is a {type} with ID number {tag}. "
          f"\nThe minimum temperature should be {min_temp} and "
          f"the maximum temperature should be {max_temp}.")

    my_monkey.setIdTag(tag[:3]+"00")  # revise ID Tag with setter
    revised_tag = my_monkey.getIdTag()
    print(f"Actually, the ID number should be {revised_tag}")


if __name__ == "__main__":
    main()

""" 
----------- Sample Run -------------
There is a Monkey with ID number 12345. 
The minimum temperature should be 45 and the maximum temperature should be 85.
Actually, the ID number should be 12300

Process finished with exit code 0


------------------------------------

This is the desired output! :)

"""