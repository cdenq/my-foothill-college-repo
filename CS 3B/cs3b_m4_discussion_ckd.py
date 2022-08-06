"""
Module to return various exoplanets information as a linked list.
- Christopher Denq
"""


class Node:
    """ Node class to store data and pointers for LinkedList. """
    def __init__(self, id_no, orbital_radius, orbital_period, discovery_date,
                 mass):
        self.id = id_no
        self.orbital_radius = orbital_radius
        self.orbital_period = orbital_period
        self.discovery_date = discovery_date
        self.mass = mass
        self.next = None
        return

    def display(self):
        return [self.id, self.orbital_radius, self.orbital_period,
                self.discovery_date, self.mass]


class LinkedList:
    """ LinkedList class to manage Nodes. """
    def __init__(self):
        self.head = None
        return

    def push(self, id_no=None, orbital_radius=None, orbital_period=None,
             discovery_date=None, mass=None, index=0):
        """ Insert a new node AFTER index position or at the start if no
        value is given, pushing the existing Nodes after down the list.
        """
        if index == 0:  # push to front
            pushed = Node(id_no, orbital_radius, orbital_period,
                          discovery_date, mass)
            pushed.next = self.head
            self.head = pushed
            return
        elif (index > self.get_count() - 1) or (index < 0) or \
                (not isinstance(index, int)):  # check if valid
            raise IndexError(f"{index} is invalid.")
        else:  # push to the specified, non-front location
            pushed = Node(id_no, orbital_radius, orbital_period,
                          discovery_date, mass)
            curr = self.head
            for i in range(index):  # index right before our indicated
                curr = curr.next
            pushed.next = curr.next
            curr.next = pushed
            return

    def pop(self, index=0):
        """ Remove node at index position. """
        if index == 0:  # pop from front
            popped = self.head
            self.head = popped.next
            return popped
        elif (index > self.get_count() - 1) or (index < 0) or \
                (not isinstance(index, int)):  # check if valid
            raise IndexError(f"{index} is invalid.")
        else:  # pop specified, non-front location
            curr = self.head
            for i in range(index-1):  # index right before our indicated
                curr = curr.next
            popped = curr.next
            if curr.next is not None:
                curr.next = popped.next
            return popped

    def get_count(self):
        """ Return the number of Nodes in that are linked together. """
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def print(self):
        """ Print out all the nodes with index labels. """
        curr = self.head
        index = 0
        while curr is not None:
            print(f"   Node {index}:")
            print(f"       {curr.display()}")
            index += 1
            curr = curr.next
        return


def main():
    exoplanets = LinkedList()
    print("No un-duplicated tasks left in assignment; will do own tasks to "
          "test the strength of my custom LinkedList.")
    print("TASK #1 - Push/Pop from front")
    print("Adding planets to front")
    exoplanets.push("KOI-55 b", 0.006, 0.2, 2011, 0.44)
    exoplanets.print()
    print("Now adding the remaining planets to get a bigger list.")
    exoplanets.push("Kepler-22 b", 0.849, 289.9, 2011, 36)
    exoplanets.push("Kepler-36 b", 0.1152, 13.9, 2012, 3.83)
    exoplanets.push("GJ 436 b", 0.0291, 2.6, 2004, 22.1)
    print("Now popping first planet.")
    exoplanets.pop()
    exoplanets.print()
    print("TASK #2 - Push/Pop from ANY index")
    exoplanets2 = LinkedList()
    print("Starting linked list.")
    exoplanets2.push("Earth Clone D", 1, 1, 2022, 1)
    exoplanets2.push("Earth Clone C", 1, 1, 2022, 1)
    exoplanets2.push("Earth Clone B", 1, 1, 2022, 1)
    exoplanets2.push("Earth Clone A", 1, 1, 2022, 1)
    exoplanets2.print()
    print("Now inserting AFTER given index of 2 (will be in node 3).")
    exoplanets2.push("INSERTED EARTH", 1, 1, 2022, 1, 2)
    exoplanets2.print()
    print("Now deleting node 2.")
    exoplanets2.pop(2)
    exoplanets2.print()
    return


if __name__ == "__main__":
    main()

r"""
--- sample run of unit_test() ---
No un-duplicated tasks left in assignment; will do own tasks to test the strength of my custom LinkedList.
TASK #1 - Push/Pop from front
Adding planets to front
   Node 0:
       ['KOI-55 b', 0.006, 0.2, 2011, 0.44]
Now adding the remaining planets to get a bigger list.
Now popping first planet.
   Node 0:
       ['Kepler-36 b', 0.1152, 13.9, 2012, 3.83]
   Node 1:
       ['Kepler-22 b', 0.849, 289.9, 2011, 36]
   Node 2:
       ['KOI-55 b', 0.006, 0.2, 2011, 0.44]
TASK #2 - Push/Pop from ANY index
Starting linked list.
   Node 0:
       ['Earth Clone A', 1, 1, 2022, 1]
   Node 1:
       ['Earth Clone B', 1, 1, 2022, 1]
   Node 2:
       ['Earth Clone C', 1, 1, 2022, 1]
   Node 3:
       ['Earth Clone D', 1, 1, 2022, 1]
Now inserting AFTER given index of 2 (will be in node 3).
   Node 0:
       ['Earth Clone A', 1, 1, 2022, 1]
   Node 1:
       ['Earth Clone B', 1, 1, 2022, 1]
   Node 2:
       ['Earth Clone C', 1, 1, 2022, 1]
   Node 3:
       ['INSERTED EARTH', 1, 1, 2022, 1]
   Node 4:
       ['Earth Clone D', 1, 1, 2022, 1]
Now deleting node 2.
   Node 0:
       ['Earth Clone A', 1, 1, 2022, 1]
   Node 1:
       ['Earth Clone B', 1, 1, 2022, 1]
   Node 2:
       ['INSERTED EARTH', 1, 1, 2022, 1]
   Node 3:
       ['Earth Clone D', 1, 1, 2022, 1]
"""