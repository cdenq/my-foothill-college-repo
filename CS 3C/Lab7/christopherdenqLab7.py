""" An object-oriented program that implements the Binary Search Tree.

This is the code solution.

Christopher Denq
CS 3C, 2022
Lab 7
"""


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.height = 0

    def length(self):
        """ Return length.
        """
        return self.size

    def height(self):
        """ Return height.
        """
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        """ Insert element.
        """
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            self.height += 1
        self.size += 1

    def _put(self, key, val, current_node):
        """ put() helper function.
        """
        if key < current_node.key:
            if current_node.hasLeftChild():
                self._put(key, val, current_node.leftChild)
            else:
                current_node.leftChild = TreeNode(key, val,
                                                 parent=current_node)
                self.height += 1
                self.update_balance(current_node.leftChild)
        else:
            if current_node.hasRightChild():
                self._put(key, val, current_node.rightChild)
            else:
                current_node.rightChild = TreeNode(key, val,
                                                  parent=current_node)
                self.height += 1
                self.update_balance(current_node.rightChild)

    def update_balance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.update_balance(node.parent)

    def rotateLeft(self, rot_root):
        new_root = rot_root.rightChild
        rot_root.rightChild = new_root.leftChild
        if new_root.leftChild is not None:
            new_root.leftChild.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.isRoot():
            self.root = new_root
        else:
            if rot_root.isLeftChild():
                rot_root.parent.leftChild = new_root
            else:
                rot_root.parent.rightChild = new_root
                new_root.leftChild = rot_root
        rot_root.parent = new_root
        rot_root.balanceFactor = rot_root.balanceFactor + 1 \
                                - min(new_root.balanceFactor, 0)
        new_root.balanceFactor = new_root.balanceFactor + 1 \
                                + max(rot_root.balanceFactor, 0)

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)


    def __setitem__(self, k, v):
            self.put(k, v)

    def get(self, key):
        """ Check if key in tree.
        """
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        """ get() helper function.
        """
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.leftChild)
        else:
            return self._get(key, current_node.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        """ Delete key from tree.
        """
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
            self.height -= 1
        else:
            raise KeyError('Key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def find_max(self):
        """ Return the max value in the tree.
        """
        current = self
        while current.hasRightChild():
            current = current.RightChild
        return current

    def remove(self,current_node):
        if current_node.isLeaf(): #leaf
            if current_node == current_node.parent.leftChild:
                current_node.parent.leftChild = None
            else:
                current_node.parent.rightChild = None
        elif current_node.hasBothChildren():  # interior
            succ = current_node.findSuccessor()
            succ.spliceOut()
            current_node.key = succ.key
            current_node.payload = succ.payload
        elif current_node.hasChildren():  # this node has one child
            if current_node.hasLeftChild():
                if current_node.isLeftChild():
                    current_node.leftChild.parent = current_node.parent
                    current_node.parent.leftChild = current_node.leftChild
                elif current_node.isRightChild():
                    current_node.leftChild.parent = current_node.parent
                    current_node.parent.rightChild = current_node.leftChild
                else:
                    current_node.replaceNodeData(current_node.leftChild.key,
                                                 current_node.leftChild.payload,
                                                 current_node.leftChild.leftChild,
                                                 current_node.leftChild.rightChild)
        else:
            if current_node.isLeftChild():
                current_node.rightChild.parent = current_node.parent
                current_node.parent.leftChild = current_node.rightChild
            elif current_node.isRightChild():
                current_node.rightChild.parent = current_node.parent
                current_node.parent.rightChild = current_node.rightChild
            else:
                current_node.replaceNodeData(current_node.rightChild.key,
                                 current_node.rightChild.payload,
                                 current_node.rightChild.leftChild,
                                 current_node.rightChild.rightChild)


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and \
               self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and \
               self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent


def main():
    return


if __name__ == "__main__":
    main()

