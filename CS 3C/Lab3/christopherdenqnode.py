""" An object-oriented program that implements the Node class, which is
used in the Linked List class.

This is the code solution.

Christopher Denq
CS 3C, 2022
Lab 3
"""


class Node:
    """ Create a Node class that holds data about an item in a linked
    list .
    """
    def __init__(self, data: str = ""):
        """  Initialize instance of Node, default values provided. """
        self.data = data
        self.next_node = None

    def check_data(self):
        if self.data == "":
            return False
        else:
            return True

    def check_next_node(self):
        if self.next_node is None:
            return False
        else:
            return True

    def get_data(self):
        return self.data

    def set_data(self, value):
        self.data = value
        return

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, value):
        self.next_node = value
        return True


def main():
    return


if __name__ == "__main__":
    main()
