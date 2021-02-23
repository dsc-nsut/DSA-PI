class Node(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def func(root):
    pass


def return_tree():
    """
    Returns the root of a tree as shown below:
            0
           /  \
          1    2
         / \  / \
        3  4  5  6
    :return: Reference to root Node
    """
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    return root

