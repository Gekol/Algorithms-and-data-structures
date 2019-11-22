class Node():
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.left = None
        self.right = None
        self.prev = None

    def __str__(self):
        return str(self.value) + " " + str(self.key)

class Treap:
    def __init__(self):
        self.root = None

    def add(self, value, key):
        if self.root == None:
            self.root = Node(value, key)
        else:
            pass

    def split(self, value):
        current = self.root
        left_subtree_root = None
        right_subtree_root = None
        current_right = None
        current_left = None

        while current != None:
            if current.value >= value:
                if not right_subtree_root:
                    right_subtree_root = current
                    current_right = right_subtree_root
                else:
                    current_right.left = current
                    current.prev = current_right
                    current_right = current_right.left
                current = current.left
            else:
                if not left_subtree_root:
                    left_subtree_root = current
                    current_left = left_subtree_root
                else:
                    current_left.right = current
                    current.prev = current_left
                    current_left = current_left.right
                current = current.right
        if current_right != None:
            current_right.left = None
        if current_left != None:
            current_left.right = None
        return left_subtree_root, right_subtree_root

    def merge(self, left, right):
        if left == None:
            return right
        elif right == None:
            return left
        elif left.key > right.key:
            res = self.merge(left.right, right)
            left.right = res
            res.prev = left
            return left
        else:
            res = self.merge(left, right.left)
            right.left = res
            res.prev = right
            return right

    def insert(self, value, key):
        new_node = Node(value, key)
        if self.root == None:
            self.root = new_node
            return
        left, right = self.split(value)
        left = self.merge(left, new_node)
        self.root = self.merge(left, right)

    def delete(self, value):
        if self.root == None:
            return "Tree is empty!!!"
        current = self.root
        while current and current.value != value:
            if current.value > value:
                current = current.left
            else:
                current = current.right
        if not current:
            return "There is no element with such a value!!!"
        parent = current.prev
        res = self.merge(current.left, current.right)
        if not parent:
            self.root = res
        elif current == parent.left:
            parent.left = res
        else:
            parent.right = res
        if res:
            res.prev = parent
        return value

    def __str__(self):
        res = ""
        nodes = [(self.root, 1)]
        i = 1
        current_level = ["0"][:] * i
        while nodes:
            current = nodes.pop(0)
            if current[1] > i * 2 - 1:
                res += ", ".join(current_level) + "\n"
                i *= 2
                current_level = ["0"][:] * i
            if current[0] != None:
                current_level[current[1]-i] = str(current[0].value) + " " + str(current[0].key)
                nodes.append((current[0].left, current[1] * 2))
                nodes.append((current[0].right, current[1] * 2 + 1))
        res += " ".join(current_level) + "\n"
        return res

def main():
    treap = Treap()
    while True:
        command = input("Enter command(insert/delete/show/exit): ")
        if command == "insert":
            value = int(input(("Enter the new value: ")))
            key = int(input(("Enter the new key: ")))
            treap.insert(value, key)
        elif command == "delete":
            value = int(input(("Enter the value: ")))
            print(treap.delete(value))
        elif command == "show":
            print(treap)
        elif command == "exit":
            break
        else:
            print("Wrong command!!!")

if __name__ == '__main__':
    main()