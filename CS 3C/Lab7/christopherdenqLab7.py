""" An object-oriented program that implements the Binary Search Tree.

This is the code solution.

Christopher Denq
CS 3C, 2022
Lab 7
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(self.root, data)

    def insert_node(self, curr_node, data):
        if data == curr_node.data:
            return
        if data < curr_node.data:
            if curr_node.left:
                self.insert_node(curr_node.left, data)
            else:
                curr_node.left = Node(data)
        elif data > curr_node.data:
            if curr_node.right:
                self.insert_node(curr_node.right, data)
            else:
                curr_node.right = Node(data)

    def get_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete(self, root, data):
        # base case
        if root is None:
            return None

        # data to delete is less than curr_node
        if data < root.data:
            root.left = self.delete(root.left, data)

        # data to delete is greater than curr_node
        elif data > root.data:
            root.right = self.delete(root.right, data)

        # data equal to data member, delete node
        else:
            # node is leaf node
            if root.left is None and root.right is None:
                root = None

                # node is root node
                if self.root.data == data:
                    self.root = None
                    return None

            # node has one child
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left

            # node has two children
            else:
                # get min node from right subtree
                temp = self.get_min(root.right)
                # copy the min value to current node
                root.data = temp.data
                # find and delete the min node in the right subtree
                root.right = self.delete(root.right, temp.data)

        return root

    def find(self, root, data):
        """Level order traversal search"""
        if root is None:
            return False

        # initialize queue with root as first element
        queue = [root]

        # loop through elements in queue
        while queue:
            # element at front of queue
            node = queue[0]

            # if element matches, return
            if node.data == data:
                return True

            # add children to queue
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

            # pop first element
            queue.pop(0)

        return False

    def height(self, root):
        if root is None:
            return 0
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    def size(self, root):
        if root is None:
            return 0
        else:
            return self.size(root.left) + 1 + self.size(root.right)

    def preorder(self, node):
        # root > left > right
        str_return = ''
        if node is not None:
            str_return += f'{node.data} '
            if node.left:
                str_return += self.preorder(node.left)
            if node.right:
                str_return += self.preorder(node.right)
            return str_return

    def inorder(self, node):
        # left > root > right
        str_return = ''
        if node is not None:
            if node.left:
                str_return += self.preorder(node.left)
            str_return += f'{node.data} '
            if node.right:
                str_return += self.preorder(node.right)
            return str_return

    def postorder(self, node):
        # left > right > root
        str_return = ''
        if node is not None:
            if node.left:
                str_return += self.preorder(node.left)
            if node.right:
                str_return += self.preorder(node.right)
            str_return += f'{node.data} '
            return str_return

    def get_max(self, node):
        if node is None:
            return

        # visit all nodes using dfs
        node_val = node.data
        left_val = self.get_max(node.left)
        right_val = self.get_max(node.right)
        if left_val is not None and left_val > node_val:
            node_val = left_val
        if right_val is not None and right_val > node_val:
            node_val = right_val
        return node_val


def main():
    return


if __name__ == "__main__":
    main()

