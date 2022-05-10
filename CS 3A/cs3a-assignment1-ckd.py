""" Input and Output module that allows the user to input their name
and the function will use their name in a hello statement.
"""


def main():
    """ Inquires user's name and returns it in print statement. """
    print("Welcome to Christopher's first OOP program!")
    user_name = input("Please input your name.")
    print("Hi, ", user_name, "!", sep="")


if __name__ == "__main__":
    main()

r"""
--- sample run ---
Welcome to Christopher's first OOP program!
Please input your name.John Smith
Hi, John Smith!
"""