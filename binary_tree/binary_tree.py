class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, new_item):
        if self.root == None:
            self.root = new_item
            return
        current_element = self.root
        while True:
            if current_element.value > new_item.value:
                if current_element.left == None:
                    current_element.left = new_item
                    new_item.prev = current_element
                    return
                current_element = current_element.left
            else:
                if current_element.right == None:
                    current_element.right = new_item
                    new_item.prev = current_element
                    return
                current_element = current_element.right

    def straight_search(self, value, current_element=None):
        if current_element == None:
            current_element = self.root
        if current_element.value == value:
            return "Found!!!"
        if current_element.left:
            self.straight_search(value, current_element.left)
        if current_element.right:
            self.straight_search(value, current_element.right)

    def reversed_search(self, value, current_element=None):
        if current_element == None:
            current_element = self.root
        if current_element.left:
            self.straight_search(value, current_element.left)
        if current_element.right:
            self.straight_search(value, current_element.right)
        if current_element.value == value:
            return "Found!!!"

    def remove(self, value):
        if self.root == None:
            print("Tree is empty!!!")
        current_elem = self.root
        if current_elem.value == value:
            if current_elem.right == None:
                self.root = current_elem.left
                self.root.prev = None
                return
            else:
                left_subtree = self.root.left
                self.root = current_elem.right
                self.root.prev = None
                tree_to_add = self.root.left
                self.root.left = left_subtree
                self.insert(tree_to_add)
                return
        while current_elem != None and current_elem.value != value:
            if value > current_elem.value:
                current_elem = current_elem.right
            else:
                current_elem = current_elem.left

        if current_elem.left == current_elem.right == None:
            if current_elem == current_elem.prev.left:
                current_elem.prev.left = None
            else:
                current_elem.prev.right = None
        elif current_elem.left == None:
            if current_elem == current_elem.prev.left:
                current_elem.prev.right = current_elem.right
            else:
                current_elem.prev.right = current_elem.right
        elif current_elem.right == None:
            if current_elem == current_elem.prev.right:
                current_elem.prev.left = current_elem.left
            else:
                current_elem.prev.left = current_elem.left
        else:
            if current_elem == current_elem.prev.right:
                current_elem.prev.right = current_elem.right
                tree_to_add = current_elem.left
                self.insert(tree_to_add)
            else:
                current_elem.prev.left = current_elem.left
                tree_to_add = current_elem.right
                self.insert(tree_to_add)

    def breadth_search(self, element):
        elements = [self.root]
        while elements:
            current_elem = elements.pop(0)
            if current_elem.value == element:
                return "Found!!!"
            elements.append(current_elem.left)
            elements.append(current_elem.right)

    def straight_traverse(self, current_element=None):
        if current_element == None:
            current_element = self.root
        print(current_element.value)
        if current_element.left:
            self.straight_traverse(current_element.left)
        if current_element.right:
            self.straight_traverse(current_element.right)

    def reversed_traverse(self, current_element):
        if current_element == None:
            current_element = self.root
        print(current_element.value)
        if current_element.left:
            self.straight_traverse(current_element.left)
        if current_element.right:
            self.straight_traverse(current_element.right)

    def __str__(self):
        res = ""
        nodes = [self.root]
        while nodes:
            current = nodes.pop(0)
            if current == None:
                res += "0 "
            else:
                res += str(current) + " "
                nodes.append(current.left)
                nodes.append(current.right)

        return res

def main():
    tree = BinaryTree()
    tree.insert(Node(5))
    tree.insert(Node(4))
    tree.insert(Node(6))
    tree.insert(Node(3))
    tree.insert(Node(7))
    tree.insert(Node(5))
    print(tree)
    tree.remove(4)
    print(tree)
    tree.remove(7)
    print(tree)

if __name__ == '__main__':
    main()