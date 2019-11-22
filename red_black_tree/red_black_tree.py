class Node:
    def __init__(self, value=None, color="r", prev=None):
        self.value = value
        self.color = color
        self.prev = prev
        if value != None:
            self.left = Node(None, "b", self)
            self.right = Node(None, "b", self)
        else:
            self.left = None
            self.right = None

    def __str__(self):
        return str(self.value)

class RedBlackTree:
    def __init__(self):
        self.root = None

    def right_turn(self, root):
        """Right turn of a tree with the specified root"""
        grand = root.prev
        new_root = root.left

        root.left = new_root.right
        root.left.prev = root

        new_root.right = root
        new_root.right.prev = new_root
        root = new_root
        root.prev = grand
        return root

    def left_turn(self, root):
        """Left turn of a tree with the specified root"""
        grand = root.prev
        new_root = root.right

        root.right = new_root.left
        root.right.prev = root

        new_root.left = root
        new_root.left.prev = new_root

        root = new_root
        root.prev = grand
        return root

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            new_node.color = "b"
            self.root = new_node
        else:
            current = self.root
            while True:
                if current.value <= value:
                    if current.right.value == None:
                        current.right = new_node
                        new_node.prev = current
                        break
                    current = current.right
                else:
                    if current.left.value == None:
                        current.left = new_node
                        new_node.prev = current
                        break
                    current = current.left

        current = new_node
        while current and  current.prev and current.prev.color == "r":
            parent = current.prev
            if not parent:
                break
            grandparent = parent.prev
            if not grandparent:
                break
            if parent == grandparent.left:
                uncle = grandparent.right
            else:
                uncle = grandparent.left
            if uncle.color == "r":
                parent.color = uncle.color = "b"
                grandparent.color = "r"
                current = grandparent
            elif parent == grandparent.left:
                if current == parent.right:
                    res = self.left_turn(parent)
                    grandparent.left = res
                great_grandparent = grandparent.prev
                if great_grandparent == None:
                    self.root = self.right_turn(grandparent)
                    res.left.color = res.right.color = "r"
                elif grandparent == great_grandparent.left:
                    res = self.right_turn(grandparent)
                    great_grandparent.left = res
                    res.color = "b"
                    res.left.color = res.right.color = "r"
                else:
                    res = self.right_turn(grandparent)
                    great_grandparent.right = res
                    res.color = "b"
                    res.left.color = res.right.color = "r"
                current = great_grandparent
            else:
                if current == parent.left:
                    res = self.right_turn(parent)
                    grandparent.right = res
                great_grandparent = grandparent.prev
                if great_grandparent == None:
                    self.root = self.left_turn(grandparent)
                    self.root.left.color = self.root.right.color = "r"
                elif grandparent == great_grandparent.left:
                    res = self.left_turn(grandparent)
                    great_grandparent.left = res
                    res.color = "b"
                    res.left.color = res.right.color = "r"
                else:
                    res = self.left_turn(grandparent)
                    great_grandparent.right = res
                    res.color = "b"
                    res.left.color = res.right.color = "r"
                current = great_grandparent
        self.root.color = "b"

    def next_value(self, current):
        """Find the smallest value bigger than given one"""
        if current == None:
            return None

        if current.right:
            current = current.right
            while current.left.value:
                current = current.left
            return current
        return Node(None, color="b", prev=current)

    def find(self, value):
        current = self.root
        while current.value != value:
            if current.value < value:
                current = current.right
                if current.value == None:
                    return "There is no such an element!!!"
            else:
                current = current.left
                if current.value == None:
                    return "There is no such an element!!!"
        return current

    def remove(self, value):
        """First we need to find the node with the specified value. After that we will use remove_value function to remove it."""
        if self.root == None:
            return "Tree is empty!!!"
        current = self.find(value)
        if type(current) == str:
            return current
        self.remove_value(current)
        return value

    def remove_value(self, current):
        """We need to reduce our task to leave two possibilities: we will remove either leaf or a node which has only one child(child must not be NULL Node).
           After that we are going to put the left son of the """
        if current == self.root and current.left.value == current.right.value == None:
            self.root = None
            return

        if current.left.value and current.right.value:
            next_value = self.next_value(current)
            current.value = next_value.value
            v = next_value
        else:
            v = current

        if v.left.value:
            u = v.left
        else:
            u = v.right
        self.remove_rotate(v, u)

    def replace_element(self, v, u):
        """Replace v with u."""
        if v == self.root:
            self.root = u
            u.prev = None
            return
        elif v == v.prev.left:
            v.prev.left = u
            brother = v.prev.right
        else:
            v.prev.right = u
            brother = v.prev.left
        u.prev = v.prev
        return brother

    def remove_rotate(self, v, u):
        if v.color == "r" or u.color == "r":
            self.replace_element(v, u)
            u.color = "b"
        else:
            brother = self.replace_element(v, u)
            parent = u.prev
            left_nephew = brother.left
            right_nephew = brother.right
            if brother.color == "b":
                if not left_nephew and not right_nephew:
                    if u == u.prev.left:
                        u.prev.left = Node(None)
                    else:
                        u.prev.right = Node(None)
                elif brother == parent.left:
                    if left_nephew.color == right_nephew.color == "b":
                        brother.color = "r"
                        while parent != self.root and parent.color != "r":
                            parent = parent.prev
                        parent.color = "b"
                    elif left_nephew.color == "r":
                        brother.color = parent.color
                        parent.color = left_nephew.color = "b"
                        if parent == self.root:
                            self.root = self.right_turn(parent)
                        else:
                            grandparent = parent.prev
                            grandparent.left = self.right_turn(parent)
                    else:
                        right_nephew.color = "b"
                        brother.color = "r"
                        brother = self.left_turn(brother)
                        parent.left = brother
                        brother.left.color = "b"
                        if parent == self.root:
                            self.root = self.right_turn(parent)
                        else:
                            grandparent = parent.prev
                            grandparent.left = self.right_turn(parent)
                else:
                    if left_nephew.color == right_nephew.color == "b":
                        brother.color = "r"
                        while parent != self.root and parent.color != "r":
                            parent = parent.prev
                        parent.color = "b"
                    elif right_nephew.color == "r":
                        brother.color = parent.color
                        parent.color = right_nephew.color = "b"
                        if parent == self.root:
                            self.root = self.left_turn(parent)
                        else:
                            grandparent = parent.prev
                            grandparent.right = self.left_turn(parent)
                    elif left_nephew.color == "r":
                        left_nephew.color = "b"
                        brother.color = "r"
                        brother = self.right_turn(brother)
                        parent.right = brother
                        brother.right.color = "b"
                        if parent == self.root:
                            self.root = self.left_turn(parent)
                        else:
                            grandparent = parent.prev
                            grandparent.right = self.left_turn(parent)
            else:
                brother.color = "b"
                parent.color = "r"
                if brother == parent.left:
                    if parent == self.root:
                        self.root = self.right_turn(parent)
                    else:
                        grandparent = parent.prev
                        if parent == grandparent.left:
                            grandparent.left = self.right_turn(parent)
                        else:
                            grandparent.right = self.right_turn(parent)
                else:
                    if parent == self.root:
                        self.root = self.left_turn(parent)
                    else:
                        grandparent = parent.prev
                        if parent == grandparent.left:
                            grandparent.left = self.left_turn(parent)
                        else:
                            grandparent.right = self.left_turn(parent)

    def __str__(self):
        if self.root == None:
            return "Empty tree!!!"
        res = ""
        nodes = [(self.root, 1)]
        i = 1
        current_level = ["0"][:] * i
        while nodes:
            current = nodes.pop(0)
            if current[1] > i * 2 - 1:
                res += " ".join(current_level) + "\n"
                i *= 2
                current_level = ["0"][:] * i
            if current[0].value != None:
                current_level[current[1] - i] = str(current[0].value) + " " + current[0].color
                nodes.append((current[0].left, current[1] * 2))
                nodes.append((current[0].right, current[1] * 2 + 1))
        res += " ".join(current_level) + "\n"
        return res

def main():
    tree = RedBlackTree()
    while True:
        command = input("Enter the command(insert/remove/show/exit): ")
        if command == "insert":
            value = int(input("Enter new value: "))
            tree.insert(value)
        elif command == "remove":
            value = int(input("Enter value: "))
            tree.remove(value)
        elif command == "show":
            print(tree)
        elif command == "exit":
            break
        else:
            print("Wrong command!!!")

if __name__ == '__main__':
    main()