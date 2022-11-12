""" An object-oriented program that implements the coded HTML parser.

This is the test driver.

Christopher Denq
CS 3C, 2022
Lab 6
"""


from christopherdenqLab6 import *


def main():
    print("Welcome to Chris's HTML Parser!")
    # Setup program object
    test = ListCollector()

    # Automatically parse the HTML
    test.parse_lists()

    # Print results
    test.get_lists()

    print("Thank you for using Chris's Translator!")
    print("Bye!")
    return


if __name__ == "__main__":
    main()


r"""
----sample run----
Welcome to Chris's HTML Parser!
[['An item', 'Another', 'And another one'], ['Item one', 'Item two', 'Item three', 'Item four']]
Thank you for using Chris's Translator!
Bye!
"""