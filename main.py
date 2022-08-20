from bin_tree import *
if __name__ == '__main__':
    root = BinTreeNode(66)
    tree = BinTree(root)
    tree.insert(root, 3)
    tree.insert(root, 10)
    tree.insert(root, 1)
    tree.insert(root, 6)
    tree.insert(root, 14)
    tree.insert(root, 4)
    tree.insert(root, 7)
    tree.insert(root, 13)
    tree.insert(root, 2)
    tree.insert(root, 13)
    tree.printTree(root)
    tree.search(root, 1)

