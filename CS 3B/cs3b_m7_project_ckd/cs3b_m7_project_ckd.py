"""
Chris Denq

"""
import csv

# Default / auto global filepaths for the "auto filepath" option.
raw_filepath = 'original_message.txt'
encoded_filepath = 'encoded.txt'
decoded_filepath = 'decoded.txt'


class Caesar:
    """ Represent the Caesar cipher, which can perform encoding/decoding
    functionality on itself.
    """

    def __init__(self, formatted):
        self.formatted = formatted

    @staticmethod
    def encode_helper(character, key, first_ascii):
        """ Helper method that encodes a letter into the key-shifted
        result.
        """
        converted = chr(
            (ord(character) + key - ord(first_ascii))
            % 26 + ord(first_ascii)
        )
        return converted

    @staticmethod
    def decode_helper(character, key, first_ascii):
        """ Helper method that decodes a letter into the key-shifted
        result.
        """
        converted = chr(
            (ord(character) - ord(first_ascii) + 26 - key)
            % 26 + ord(first_ascii)
        )
        return converted

    def caesar_encode(self, key):
        """ Encode a plain text character or list of plain text
        characters and return a cipher character or list of cipher
        characters.
        """
        output = []
        for line in self.formatted:
            temp_list = []
            for letter in line:
                # Checking the letter type
                if ord("A") <= ord(letter) <= ord("Z"):  # if is uppercase
                    to_append = Caesar.encode_helper(letter, key, "A")
                elif ord("a") <= ord(letter) <= ord("z"):  # if is lowercase
                    to_append = Caesar.encode_helper(letter, key, "a")
                else:  # else it's not a letter, so do nothing
                    to_append = letter
                temp_list.append(to_append)
            output.append(temp_list)
        self.formatted = output
        return

    def caesar_decode(self, key):
        """ Decode a cipher character or list of cipher characters and
        return a plain text character or list of plain text characters.
        """
        output = []
        for line in self.formatted:
            temp_list = []
            for letter in line:
                # Checking the letter type
                if ord("A") <= ord(letter) <= ord("Z"):  # if is uppercase
                    to_append = Caesar.decode_helper(letter, key, "A")
                elif ord("a") <= ord(letter) <= ord("z"):  # if is lowercase
                    to_append = Caesar.decode_helper(letter, key, "a")
                else:  # else it's not a letter, so do nothing
                    to_append = letter
                temp_list.append(to_append)
            output.append(temp_list)
        self.formatted = output
        return


def process_file(input_filename, output_filename, encode_decode, key):
    """ Perform encoding/decoding on a given filepath and then outputs
    the results to the given output filepath.
    """
    # Error Handling: catching unknown files
    try:
        csv_file = open(input_filename, 'r')
    except FileNotFoundError:
        print("File not found; returning False.")
        return False

    # Format data to pass into Caesar class
    reader = csv.reader(csv_file, delimiter="\n")
    formatted = []
    for line in reader:
        temp_list = []
        for letter in range(len(line[0])):
            temp_list.append(line[0][letter])
        formatted.append(temp_list)
    csv_file.close()

    # Running cipher functions on Caesar object
    message_to_go = Caesar(formatted)
    if encode_decode == "encode":
        message_to_go.caesar_encode(key)
    else:
        message_to_go.caesar_decode(key)

    # Output data to file
    with open(output_filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for line in message_to_go.formatted:
            combined_string = ""
            for letter in line:
                combined_string += letter
            writer.writerow([combined_string])


def main():
    # Welcome
    print("Welcome to Chris's Cipher Program!")

    # User Interaction Section
    ask_again = True
    while ask_again:

        # User Input: Manually input filepaths or use auto files?
        while True:
            mode = input("Would you like to manually specify the filepaths (1)"
                         " or use the automatic options in this workbook? (2)")
            try:
                mode = int(mode)
                if mode == 1:
                    print("Manual filepath selected!")
                    break
                elif mode == 2:
                    print("Automatic filepath selected! Make sure to encode"
                          " before you decode!")
                    break
                else:
                    print(f"{mode} is not a valid integer; please try again.")
            except ValueError:
                print(f"{mode} is not valid; please try again.")

        # User Input: Cipher Key
        while True:
            key = input("What key / shift do you want? Please input integer.")
            try:
                key = int(key)
                break
            except ValueError:
                print(f"{key} is not an integer; please try again.")

        # User Input: Encode or Decode?
        while True:
            en_de = input("Would you like to encode (1) or decode (2) a "
                          "message?")
            try:
                en_de = int(en_de)
                if en_de == 1:
                    print("Encoding selected.")
                    break
                elif en_de == 2:
                    print("Decoding selected")
                    break
                else:
                    print(f"{en_de} is not a valid integer; please try again.")
            except ValueError:
                print(f"{en_de} is not valid; please try again.")

        # Program Sequence: Run Cipher Code
        if mode == 1:
            input_filepath = input("What your the exact input filepath?")
            output_filepath = input("What is the filename of the output?")
            if en_de == 1:
                process_file(input_filepath, output_filepath, 'encode', key)
                print("Done encoding! New file outputted (if valid)!")
            else:
                process_file(input_filepath, output_filepath, 'decode', key)
                print("Done decoding! New file outputted (if valid)!")

        else:  # User has specified auto-filepaths
            if en_de == 1:
                process_file(raw_filepath, encoded_filepath, 'encode', key)
                print("Done auto-encoding! New file outputted (if valid)!")
            else:
                process_file(encoded_filepath, decoded_filepath, 'decode', key)
                print("Done auto-decoding! New file outputted (if valid)!")

        # User Input: Go Again?
        while True:
            ans3 = input("Would you like to perform another action? (y/n)")
            if ans3 == "y":
                break
            elif ans3 == "n":
                ask_again = False
                break
            else:
                print(f"{ans3} is not a valid response; please try again.")

    # Goodbye
    print("Thank you for using the cipher! Goodbye!")
    return


if __name__ == "__main__":
    main()

r"""
--- sample run of unit_test() ---
Welcome to Chris's Cipher Program!
Would you like to manually specify the filepaths (1) or use the automatic options in this workbook? (2)2
Automatic filepath selected! Make sure to encode before you decode!
What key / shift do you want? Please input integer.1
Would you like to encode (1) or decode (2) a message?2
Decoding selected
File not found; returning False.
Done auto-decoding! New file outputted (if valid)!
Would you like to perform another action? (y/n)y
Would you like to manually specify the filepaths (1) or use the automatic options in this workbook? (2)2
Automatic filepath selected! Make sure to encode before you decode!
What key / shift do you want? Please input integer.1
Would you like to encode (1) or decode (2) a message?2
Decoding selected
File not found; returning False.
Done auto-decoding! New file outputted (if valid)!
Would you like to perform another action? (y/n)y
Would you like to manually specify the filepaths (1) or use the automatic options in this workbook? (2)2
Automatic filepath selected! Make sure to encode before you decode!
What key / shift do you want? Please input integer.1
Would you like to encode (1) or decode (2) a message?1
Encoding selected.
Done auto-encoding! New file outputted (if valid)!
Would you like to perform another action? (y/n)y
Would you like to manually specify the filepaths (1) or use the automatic options in this workbook? (2)2
Automatic filepath selected! Make sure to encode before you decode!
What key / shift do you want? Please input integer.1
Would you like to encode (1) or decode (2) a message?2
Decoding selected
Done auto-decoding! New file outputted (if valid)!
Would you like to perform another action? (y/n)y
Would you like to manually specify the filepaths (1) or use the automatic options in this workbook? (2)1
Manual filepath selected!
What key / shift do you want? Please input integer.1
Would you like to encode (1) or decode (2) a message?1
Encoding selected.
What your the exact input filepath?original_message.txt
What is the filename of the output?manual_test.txt
Done encoding! New file outputted (if valid)!
Would you like to perform another action? (y/n)y
Would you like to manually specify the filepaths (1) or use the automatic options in this workbook? (2)1
Manual filepath selected!
What key / shift do you want? Please input integer.1
Would you like to encode (1) or decode (2) a message?2
Decoding selected
What your the exact input filepath?manual_test.txt
What is the filename of the output?manual_test_de.txt
Done decoding! New file outputted (if valid)!
Would you like to perform another action? (y/n)n
Thank you for using the cipher! Goodbye!
"""
