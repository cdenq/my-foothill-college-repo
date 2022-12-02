""" An object-oriented program that tests the graph and vertex code.

This is the test driver.

Christopher Denq
CS 3C, 2022
Lab 8
"""
from christopherdenqvertex import *
from christopherdenqgraph import *


def main():
    print("Welcome to Chris's Graph Tester!")
    # Setup program object
    test = Graph()

    # Read in assignment values
    # a->b: 4; a->c: 1 ; b->a: 3; b->d: 2; c-> a: 1; c->b: 5
    test.add_edge("a", "b", 4)
    test.add_edge("a", "c", 1)
    test.add_edge("b", "a", 3)
    test.add_edge("b", "d", 2)
    test.add_edge("c", "a", 1)
    test.add_edge("c", "b", 5)
    print("Graph data:")
    print(test.get_edges())

    # Farewell
    print("Thank you for using Chris's Graph Tester!")
    print("Bye!")
    return


if __name__ == "__main__":
    main()


r"""
----sample run----
Welcome to Chris's Graph Tester!
Graph data:
[('a', 'b', 4), ('a', 'c', 1), ('b', 'a', 3), ('b', 'd', 2), ('c', 'a', 1), ('c', 'b', 5)]
Thank you for using Chris's Graph Tester!
Bye!
"""