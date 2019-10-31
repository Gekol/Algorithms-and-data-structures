class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.child = None
        self.sibling = None

class Graph:
    def __init__(self):
        self.root = None

    def add(self, new_value, index):
        if self.root == None or index == 1:
            new_root = Node(new_value)
            new_root.child = self.root
            self.root = new_root
        else:
            nodes = [(self.root, 1)]
            while nodes:
                current = nodes.pop(0)
                if current[1] == index:
                    pass