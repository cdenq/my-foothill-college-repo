""" An object-oriented program that implements the Huffman Algorithm
using the greedy search paradigm.

This is the code solution and test driver.

Christopher Denq
CS 3C, 2022
Lab 9
"""


class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def __str__(self):
        return self.left, self.right


class GreedyHuffman:
    def __int__(self, data=None):
        self.data = None
        self.freq = None
        self.root = None
        self.codes = None

    def get_data(self):
        if self.data is None:
            print("No freq determined.")
        else:
            print(self.data)
        return

    def set_data(self, text):
        self.data = text
        return

    def get_freq(self):
        if self.freq is None:
            print("No freq determined.")
        else:
            for i in self.freq:
                print(f"{i[0]}: {i[1]}")
        return

    def determine_freq(self):
        new_freq_dict = {}
        for char in self.data:
            if char in new_freq_dict.keys():
                new_freq_dict[char] += 1
            else:
                new_freq_dict[char] = 1
        sorted_freq_dict = sorted(new_freq_dict.items(), key=lambda x: x[1],
                                  reverse=True)
        self.freq = sorted_freq_dict
        return

    def determine_huffman_code(self, node, bin_string=''):
        if type(node) is str:
            return {node: bin_string}
        (l, r) = node.children()
        d = dict()
        d.update(self.determine_huffman_code(l, bin_string + '0'))
        d.update(self.determine_huffman_code(r, bin_string + '1'))
        return d

    def make_tree(self):
        temp_nodes = self.freq
        while len(temp_nodes) > 1:
            (key1, c1) = temp_nodes[-1]
            (key2, c2) = temp_nodes[-2]
            temp_nodes = temp_nodes[:-2]
            node = NodeTree(key1, key2)
            temp_nodes.append((node, c1 + c2))
            temp_nodes = sorted(temp_nodes, key=lambda x: x[1], reverse=True)
        self.root = temp_nodes[0][0]
        return

    def set_codes(self):
        self.codes = self.determine_huffman_code(self.root)
        return

    def get_codes(self):
        for i in range(len(self.freq)):
            print(f"('{self.freq[i][0]}', {self.freq[i][1]}, "
                  f"'{self.codes[self.freq[i][0]]}')")
        return


def main():
    # Welcome
    print("Welcome to Chris's Huffman Code using Greedy Algorithm!")

    # Setup object
    test = GreedyHuffman()
    text = "this is an example for huffman encoding"
    test.set_data(text)
    test.determine_freq()

    # Run assignment functions
    test.make_tree()
    test.set_codes()
    print("Symbol, Frequency, Huffman Code:")
    test.get_codes()

    # Exit
    print("Thanks for using Chris's Huffman Code.")
    print("Bye!")
    return


if __name__ == "__main__":
    main()

r"""
-------Sample Run-------
Welcome to Chris's Huffman Code using Greedy Algorithm!
Symbol, Frequency, Huffman Code:
(' ', 6, '111')
('n', 4, '001')
('i', 3, '1011')
('a', 3, '1010')
('e', 3, '1101')
('f', 3, '1100')
('h', 2, '1000')
('s', 2, '0101')
('m', 2, '0100')
('o', 2, '0111')
('t', 1, '10010')
('x', 1, '100111')
('p', 1, '100110')
('l', 1, '00001')
('r', 1, '00000')
('u', 1, '00011')
('c', 1, '00010')
('d', 1, '01101')
('g', 1, '01100')
Thanks for using Chris's Huffman Code.
Bye!
"""
