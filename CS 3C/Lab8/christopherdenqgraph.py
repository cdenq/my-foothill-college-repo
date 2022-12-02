""" An object-oriented program that implements the graph class used
in graphs.

This is the code solution.

Christopher Denq
CS 3C, 2022
Lab 8
"""
from christopherdenqvertex import *


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def get_vertex(self, name):
        if name in self.vert_list:
            return self.vert_list[name]
        else:
            return None

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertices(self) -> object:
        return self.vert_list.values()

    def get_edges(self):
        res_list = []
        for i in self.vert_list:
            for j in self.vert_list[i].adjacent.keys():
                res_list.append((i,
                                 j.id,
                                 self.vert_list[i].adjacent[j]))
        return res_list

    def add_edge(self, f, t, c=0):
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], c)
        return

    def __contains__(self, name):
        """ Check if vertex is in list.
        """
        return name in self.vert_list

    def __iter__(self):
        return iter(self.vert_list.values())


def main():
    return


if __name__ == "__main__":
    main()

