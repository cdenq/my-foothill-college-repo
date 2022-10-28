""" An object-oriented program that tests out a Pascal implementation.

This is the test driver.

Christopher Denq
CS 3C, 2022
Lab 4
"""


from christopherdenqLab4 import *


FULLNAME = "ChristopherDenq"


def main():
    print("Welcome to Chris's Pascal Program!")
    print("Automatically running through 0 - 6 depth triangles...")
    for i in range(7):
        print(f"Depth {i}:")
        test = Pascal(i)
        test.get_lines()
        print(f"-------------------")
    print(f"Now printing {len(FULLNAME)} depth triangle...")
    print(f"-------------------")
    print(f"Depth {len(FULLNAME)}:")
    test = Pascal(len(FULLNAME))
    test.get_lines()
    print("Thanks for using Chris's Pascal Program!")
    return


if __name__ == "__main__":
    main()

r"""
----sample run----
Welcome to Chris's Pascal Program!
Automatically running through 0 - 6 depth triangles...
Depth 0:
Row -: []
-------------------
Depth 1:
Row 0: [1]
-------------------
Depth 2:
Row 0: [1]
Row 1: [1 1]
-------------------
Depth 3:
Row 0: [1]
Row 1: [1 1]
Row 2: [1 2 1]
-------------------
Depth 4:
Row 0: [1]
Row 1: [1 1]
Row 2: [1 2 1]
Row 3: [1 3 3 1]
-------------------
Depth 5:
Row 0: [1]
Row 1: [1 1]
Row 2: [1 2 1]
Row 3: [1 3 3 1]
Row 4: [1 4 6 4 1]
-------------------
Depth 6:
Row 0: [1]
Row 1: [1 1]
Row 2: [1 2 1]
Row 3: [1 3 3 1]
Row 4: [1 4 6 4 1]
Row 5: [1 5 10 10 5 1]
-------------------
Now printing 15 depth triangle...
-------------------
Depth 15:
Row 0: [1]
Row 1: [1 1]
Row 2: [1 2 1]
Row 3: [1 3 3 1]
Row 4: [1 4 6 4 1]
Row 5: [1 5 10 10 5 1]
Row 6: [1 6 15 20 15 6 1]
Row 7: [1 7 21 35 35 21 7 1]
Row 8: [1 8 28 56 70 56 28 8 1]
Row 9: [1 9 36 84 126 126 84 36 9 1]
Row 10: [1 10 45 120 210 252 210 120 45 10 1]
Row 11: [1 11 55 165 330 462 462 330 165 55 11 1]
Row 12: [1 12 66 220 495 792 924 792 495 220 66 12 1]
Row 13: [1 13 78 286 715 1287 1716 1716 1287 715 286 78 13 1]
Row 14: [1 14 91 364 1001 2002 3003 3432 3003 2002 1001 364 91 14 1]
Thanks for using Chris's Pascal Program!
"""