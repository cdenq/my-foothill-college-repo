""" An object-oriented program uses tree traversal algorithms to
navigate/parse a given web page layout--which is being treated as a
binary tree.

This is the code solution.

Christopher Denq
CS 3C, 2022
Lab 6
"""


from html import parser
file_path = "lists.html"


class ListCollector(parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = self.load_list()
        self.parsed_data = []
        self.can_parse = False
        self.temp_list = []

    def get_lists(self):
        print(self.parsed_data)
        return

    def parse_lists(self):
        self.feed(self.data)
        return

    def handle_starttag(self, tag, attrs):
        if tag == "ul" or tag == "ol":
            self.can_parse = True
        return

    def handle_endtag(self, tag):
        if tag == "ul" or tag == "ol":
            self.can_parse = False
            self.parsed_data.append(self.temp_list)
            self.temp_list = []
        return

    def handle_data(self, data):
        if self.can_parse and data.strip():
            self.temp_list.append(data)

    @staticmethod
    def load_list():
        with open(file_path, "r") as htmlfile:
            output_str = ""
            body = htmlfile.read().splitlines()
            for i in body:
                output_str += i
            return output_str


def main():
    return


if __name__ == "__main__":
    main()
