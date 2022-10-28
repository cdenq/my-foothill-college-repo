""" An object-oriented program that implements the Pascal class, which
mimics Pascal's Triangle using recursion.

This is the code solution.

Christopher Denq
CS 3C, 2022
Lab 4
"""


class Pascal:
    """ Create a Pascal class to implement Pascal's Triangle.
    """
    def __init__(self, depth=None):
        """  Initialize instance of Pascal.
        """
        if depth is not None:
            self.add_lines(depth)
        else:
            self.data = []
        self.line_count = len(self.data)
        return

    def add_lines(self, depth=5):
        """ Overwrite previous Pascal with new lines of desired depth.
        """
        if depth < 0 or not isinstance(depth, int):
            print("Invalid depth. Please choose non-negative integer.")
        else:
            self.data = self.build_lines(depth)
            self.update_line_count()
        return

    def build_lines(self, depth=5):
        """  Recursively generate lines for Pascal; helper function.
        """
        if depth == 0:  # if given 0-depth triangle
            return []
        elif depth == 1:  # base case for n-depth triangle above 0
            return [[1]]
        else:  # recursion for n-depth triangle above 0
            curr_row = [1]  # first 1
            body = self.build_lines(depth - 1)
            last_row = body[-1]
            for i in range(len(last_row) - 1):
                curr_row.append(last_row[i] + last_row[i + 1])
            curr_row += [1]  # last 1
            body.append(curr_row)
        return body

    def get_lines(self):
        """  Print out all the lines in Pascal.
        """
        if not self.data:
            print(f"Row -: []")
        else:
            for i, row in enumerate(self.data):
                print(f"Row {i}: [", end="")
                for j in range(len(row)):
                    if j == 0:
                        print(f"{row[j]}", end="")
                    else:
                        print(f" {row[j]}", end="")
                print("]\n", end="")
        return

    def update_line_count(self):
        """  Update the line_count of Pascal object; helper function.
        """
        self.line_count = len(self.data)
        return

    def get_line_count(self):
        """  Return current number of lines in Pascal.
        """
        # print(self.line_count)
        return self.line_count

    # Below are functions for iterative solution / controlling lines
    # one at a time.

    def test_lines(self):
        """  Initialize Pascal body with testing values.
        """
        self.data = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
        self.update_line_count()
        return

    def create_line(self):
        """  Create skeleton of the next, new line; helper function.
        """
        element_count = self.get_line_count() + 1
        new_line = []
        for i in range(element_count):
            if i == 0 or i == element_count-1:
                new_line.append(1)
            else:
                new_line.append(None)
        return new_line, element_count

    def populate_line(self, line_tuple):
        """  Populate a given line; helper function.
        """
        element_count = line_tuple[1]
        new_line = line_tuple[0]
        for i in range(len(new_line)):
            if i == 0 or i == len(new_line)-1:
                continue
            else:
                v1 = self.data[element_count-2][i-1]
                v2 = self.data[element_count-2][i]
                new_line[i] = v1 + v2
        return new_line

    def push_line(self):
        """  Add a new line to bottom of Pascal.
        """
        if self.get_line_count() == 0:
            self.data.append([1])
        elif self.get_line_count() == 1:
            self.data.append([1, 1])
        else:
            self.data.append(self.populate_line(self.create_line()))
        self.update_line_count()
        return

    def pop_line(self):
        """  Remove bottom line in Pascal.
        """
        if not self.data:
            print("Pascal is empty! Cannot pop anymore.")
        elif self.get_line_count() <= 1:
            self.data = []
        else:
            self.data.pop()
        self.update_line_count()
        return

    def reset_lines(self):
        """  Remove all lines in Pascal, leaving null list.
        """
        while self.get_line_count() != 0:
            self.pop_line()
        self.update_line_count()
        return


def main():
    return


if __name__ == "__main__":
    main()
