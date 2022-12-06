""" An object-oriented program that tests the BST code.

This is the test driver.

Time complexity of max function = O(n)
Space complexity of max function = O(1)

Christopher Denq
CS 3C, 2022
Lab 7
"""


from christopherdenqLab7 import *


def main():
    print("Welcome to Chris's BST Tester!")
    # Setup program object
    test = BinaryTree()

    # Insert values
    to_insert = [15, 43, 87, 7, 13, 19, 17, 5, 34, 3, 4]
    for i in to_insert:
        test.insert(i)
    test.preorder(test.root)

    print("Thank you for using Chris's BST Tester!")
    print("Bye!")
    return


if __name__ == "__main__":
    main()


r"""
----sample run----

"""