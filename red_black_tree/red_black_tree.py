class Node:
    def __init__(self, value=None, color="r"):
        self.value = value
        self.color = color
        if value != None:
            self.left = Node(None, "b")
            self.right = Node(None, "b")

class RedBlackTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root == None:
            self.root = Node(value, "b")
        else:
            color = "r"
            current = self.root
