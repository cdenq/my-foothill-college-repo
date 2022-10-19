""" An object-oriented program that implements the Stack class, which
uses the Node class.

This is the code solution.

Christopher Denq
CS 3C, 2022
Lab 3
"""


from christopherdenqnode import *


class Stack:
    """ Create a Stack class that implements the Stack ADT.
    """
    def __init__(self, data=None):
        """  Initialize instance of Stack. If there is one argument
         provided, then it will be automatically pushed onto the stack.
        """
        self.head = None
        if data is not None:
            self.push(data)

    def push(self, value):
        """ Create a Node object and add that to top of Stack.
        """
        temp = Node(value)
        temp.set_next_node(self.head)
        self.head = temp
        return

    def pop(self):
        """ Remove Node object from top of Stack, if able.
        """
        if self.is_empty():
            print(f"{self} is empty; could not pop!")
            return False
        else:
            self.head = self.head.get_next_node()
            return True

    def peek(self):
        """ Print the value of the data in the header Node.
        """
        if self.is_empty():
            print(f"{self} is empty; could not peek!")
        else:
            return self.head.get_data()
        return

    def is_empty(self):
        """ Check if Stack object is empty.
        """
        if self.head is None:
            return True
        else:
            return False

    def print_stack(self):
        """ Print out values of the Node objects in the stack.
        """
        if self.is_empty():
            print(f"{self} is empty; could not print!")
        else:
            current = self.head
            return_list = []
            while current is not None:
                return_list.append(current.get_data())
                current = current.get_next_node()
            print(return_list)
        return

    @classmethod
    def create_stack(cls, value=None):
        """ Instantiate a Stack object.
        """
        if value is None:
            return Stack()
        else:
            return Stack(value)

    def delete_stack(self):
        """ Empty all Node objects from the Stack.
        """
        if self.is_empty():
            print(f"{self} is already empty; could not delete any Nodes!")
        else:
            while self.head is not None:
                self.pop()
        return

def main():
    return


if __name__ == "__main__":
    main()
