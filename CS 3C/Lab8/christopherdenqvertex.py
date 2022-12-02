""" An object-oriented program that implements the vertex class used
in graphs.

This is the code solution.

Christopher Denq
CS 3C, 2022
Lab 8
"""
import sys


class Vertex:
    def __init__(self, name=None):
        self.id = name
        self.adjacent = {}
        self.dist = sys.maxsize
        self.visited = False
        self.previous = None

    def get_vertex_id(self):
        return self.id

    def get_weight(self, name):
        return self.adjacent[name]

    def get_distance(self):
        return self._dist

    def set_distance(self, value):
        self.dist = value
        return

    def get_connections(self):
        return self.adjacent.keys()

    def set_previous(self, value):
        self.previous = value
        return

    def add_neighbor(self, name, weight=None):
        """ Adds a neighbor to adjacency mapping of current node.
        """
        self.adjacent[name] = weight
        return

    def to_string(self):
        return str(self.id) + " -> " + str([x.id for x in self.adjacent])


def main():
    return


if __name__ == "__main__":
    main()

