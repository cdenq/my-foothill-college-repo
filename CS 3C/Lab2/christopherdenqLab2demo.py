""" An object-oriented program that can extract a translation guide from
a text file. The translation guide is a dictionary, and we can test the
time complexity of dictionary functions.

This is the test driver.

Benchmarking:

Time complexity: O(1), constant.

Christopher Denq
CS 3C, 2022
Lab 2
"""


from christopherdenqLab2 import *


def main():
    # Setup program object
    latin = Translator()

    # Run interactive section
    print("Welcome to Chris's Latin-English Translator!")
    print("")  # Add another newline for spacing
    while True:
        helper_menu()
        ans = input("Command:")
        if ans == "1":
            latin.set_filepath()
        elif ans == "2":
            latin.get_filepath()
        elif ans == "3":
            latin.load()
        elif ans == "4":
            latin.get_dictionary()
        elif ans == "5":
            latin.translate()
        elif ans == "0":
            break
        else:
            print(f"{ans} is not a valid command. Please try again.")
            print("")  # Add another newline for spacing
    print("Thank you for using Chris's Translator!")
    print("Bye!")
    return


if __name__ == "__main__":
    main()


r"""
----sample run----
Welcome to Chris's Latin-English Translator!

COMMAND MENU
1 - Manually set filepath (default value available)
2 - Check current filepath
3 - Load translation from filepath
4 - Print all translations
5 - Translate phrase
0 - Exit

Command:4
Translations are not loaded; see Load command.

COMMAND MENU
1 - Manually set filepath (default value available)
2 - Check current filepath
3 - Load translation from filepath
4 - Print all translations
5 - Translate phrase
0 - Exit

Command:5
Translations are not loaded; see Load command.

COMMAND MENU
1 - Manually set filepath (default value available)
2 - Check current filepath
3 - Load translation from filepath
4 - Print all translations
5 - Translate phrase
0 - Exit

Command:2
latin.txt

COMMAND MENU
1 - Manually set filepath (default value available)
2 - Check current filepath
3 - Load translation from filepath
4 - Print all translations
5 - Translate phrase
0 - Exit

Command:1
New filepath:fakefile.txt
fakefile.txt doesn't exist; setting to default.

COMMAND MENU
1 - Manually set filepath (default value available)
2 - Check current filepath
3 - Load translation from filepath
4 - Print all translations
5 - Translate phrase
0 - Exit

Command:1
New filepath:small_latin.txt
small_latin.txt added as new filepath!

COMMAND MENU
1 - Manually set filepath (default value available)
2 - Check current filepath
3 - Load translation from filepath
4 - Print all translations
5 - Translate phrase
0 - Exit

Command:2
small_latin.txt

COMMAND MENU
1 - Manually set filepath (default value available)
2 - Check current filepath
3 - Load translation from filepath
4 - Print all translations
5 - Translate phrase
0 - Exit

Command:1
New filepath:latin.txt
latin.txt added as new filepath!

COMMAND MENU
1 - Manually set filepath (default value available)
2 - Check current filepath
3 - Load translation from filepath
4 - Print all translations
5 - Translate phrase
0 - Exit

Command:3
Load successful!

COMMAND MENU
1 - Manually set filepath (default value available)
2 - Check current filepath
3 - Load translation from filepath
4 - Print all translations
5 - Translate phrase
0 - Exit

Command:4
1. abbas: father
2. abbatis: abbot
3. abbatia: abbey
...
2971. volturius: vulture
2972. vultus: expression
2973. xiphias: sword

COMMAND MENU
1 - Manually set filepath (default value available)
2 - Check current filepath
3 - Load translation from filepath
4 - Print all translations
5 - Translate phrase
0 - Exit

Command:5
Wiping previous benchmark times from memory!
Enter a latin phrase (space-separated):post hoc ergo propter FAKELATINWORD
Translation: after this therefore because of <N/A>

Attempt times:
Attempt 0: 3.1999999947629476e-06
Attempt 1: 8.99999996306633e-07
Attempt 2: 8.000000022434506e-07
Attempt 3: 8.000000022434506e-07
Attempt 4: 4.300000000512227e-06
Average: 1.999999999213742e-06

COMMAND MENU
1 - Manually set filepath (default value available)
2 - Check current filepath
3 - Load translation from filepath
4 - Print all translations
5 - Translate phrase
0 - Exit

Command:9
9 is not a valid command. Please try again.

COMMAND MENU
1 - Manually set filepath (default value available)
2 - Check current filepath
3 - Load translation from filepath
4 - Print all translations
5 - Translate phrase
0 - Exit

Command:0
Thank you for using Chris's Translator!
Bye!
"""