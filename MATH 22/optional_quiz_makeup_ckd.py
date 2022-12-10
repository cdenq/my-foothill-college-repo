""" An object-oriented program that implements the solution for the
MATH 22 Discrete Mathematics optional make-up quiz assignment.

This is the code solution and test driver.

Christopher Denq
Prof. Charles Witschorik
MATH 22, Dec 2022
"""


class Solution:
    GLOBAL_ID = "20518719"

    def __init__(self, value=GLOBAL_ID):
        self.student_id = value
        self.a = sum([int(i) for i in self.student_id[:4]])
        self.b = sum([int(i) for i in self.student_id[4:]])

    def get_id(self):
        return self.student_id

    def set_id(self, value):
        self.student_id = value
        return

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def sequence_s(self, n):
        if n < 0 or not isinstance(n, int):
            print("Invalid n.")
        elif n == 0:
            return self.a
        elif n == 1:
            return self.b
        else:
            return self.sequence_s(n - 2) + self.sequence_s(n - 1)

    def print_sequence_s(self, n):
        for i in range(n+1):
            print(f"S{i}: {self.sequence_s(i)}")
        return


def main():
    # Welcome
    print("Welcome to Chris's Recursive Playground Code")

    # Setup object
    test = Solution()
    print(f"id = {test.get_id()}")
    print(f"a = {test.get_a()}")
    print(f"b = {test.get_b()}")
    print("")

    # Run assignment question
    print("S30 is...")
    test.print_sequence_s(30)
    print("")

    # Run assignment demonstration
    done = False
    while True:
        ans = input("Which specific S(n) would you like to see?")
        try:
            valid_n = int(ans)
            print(f"S{valid_n}...")
            print(test.sequence_s(valid_n))
        except ValueError:
            print("That is an invalid n.")
        while True:
            resp = input("Would you like to try another n? (y/n)")
            if resp == "n":
                done = True
                break
            elif resp == "y":
                break
            else:
                print("Please input (y/n).")
        if done:
            break
    print("")

    # Exit
    print("Thanks for using Chris's Recursive Playground Code")
    print("Bye!")
    return


if __name__ == "__main__":
    main()

r"""
-------Sample Run-------
Welcome to Chris's Recursive Playground Code
id = 20518719
a = 8
b = 25

S30 is...
S0: 8
S1: 25
S2: 33
S3: 58
S4: 91
S5: 149
S6: 240
S7: 389
S8: 629
S9: 1018
S10: 1647
S11: 2665
S12: 4312
S13: 6977
S14: 11289
S15: 18266
S16: 29555
S17: 47821
S18: 77376
S19: 125197
S20: 202573
S21: 327770
S22: 530343
S23: 858113
S24: 1388456
S25: 2246569
S26: 3635025
S27: 5881594
S28: 9516619
S29: 15398213
S30: 24914832

Which specific S(n) would you like to see?invalid
That is an invalid n.
Would you like to try another n? (y/n)y
Which specific S(n) would you like to see?5.342
That is an invalid n.
Would you like to try another n? (y/n)y
Which specific S(n) would you like to see?7
S7...
389
Would you like to try another n? (y/n)y
Which specific S(n) would you like to see?12
S12...
4312
Would you like to try another n? (y/n)y
Which specific S(n) would you like to see?bad input y/n
That is an invalid n.
Would you like to try another n? (y/n)5
Please input (y/n).
Would you like to try another n? (y/n)t
Please input (y/n).
Would you like to try another n? (y/n)n

Thanks for using Chris's Recursive Playground Code
Bye!
"""
