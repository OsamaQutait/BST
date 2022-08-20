import sys
from bin_tree_node import *
class BinTree:

    def __init__(self, root):
        self.root =root

    def insert(self, root, newValue):
        if root is None:
            root = BinTreeNode(newValue)
        elif newValue > root.value:
            root.right = self.insert(root.right, newValue)
        elif newValue < root.value:
            root.left = self.insert(root.left, newValue)
        elif newValue == root.value:
            return root
            # print("yes")
            # sys.exit(str(newValue)+" is already exists in tree")
            # exit()
            # quit()
            # return None
            # pass
        return root

    def search(self, root, value):
        if root is None:
            print("\nthe value ("+str(value)+") not in the tree")
            return
        if root.value == value:
            print("\nthe value ("+str(value)+") in the tree")
            return
        if root.value > value:
            self.search(root.left, value)
        else:
            self.search(root.right, value)


    def printTree(self, root):
        # the output will produce sorted
        if root is None:
            return
        else:
            self.printTree(root.left)
            print(root.value, end=" -> ")
            self.printTree(root.right)
