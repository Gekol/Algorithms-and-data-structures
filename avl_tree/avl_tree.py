class Node:
    def __init__(self, value):
        self.value = value
        self.balance = 0
        self.height = 0
        self.prev = None
        if value != None:
            self.left = Node(None)
            self.right = Node(None)
        else:
            self.left = None
            self.right = None
            self.height -= 1

    def __str__(self):
        return str(self.value)

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, new_node, current=None):
        if self.root == None:
            self.root = new_node
        else:
            if current == None:
                current = self.root
            if current.value <= new_node.value:
                if current.right.value == None:
                    current.right = new_node
                    new_node.prev = current
                else:
                    self.insert(new_node, current.right)
            else:
                if current.left.value == None:
                    current.left = new_node
                    new_node.prev = current
                else:
                    self.insert(new_node, current.left)
            current.height = max(current.left.height, current.right.height) + 1
            self.balance_tree(current)
            current.balance = current.left.height - current.right.height

    def set_height(self, root):
        """Set the height needed for the whole tree with the given root"""
        if root.left.value == root.right.value == None:
            root.height = 0
        elif root.left.value == None:
            root.height = self.set_height(root.right) + 1
        elif root.right.value == None:
            root.height = self.set_height(root.left) + 1
        else:
            root.height = max(self.set_height(root.left), self.set_height(root.right)) + 1
        return root.height

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
        self.set_height(root)
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
        self.set_height(root)
        return root

    def balance_tree(self, root):
        """Balance tree"""
        lt = root.left
        rt = root.right
        llt = lt.left
        rlt = lt.right
        lrt = rt.left
        rrt = rt.right
        grand = root.prev
        if root != self.root:
            if root == grand.left:
                left_child = True
            else:
                left_child = False
        if lt.height - rt.height == 2:
            if llt.height >= rlt.height:
                print("Simple right turn")
                if root == self.root:
                    self.root = self.right_turn(root)
                else:
                    res = self.right_turn(root)
                    grand.left = res
                    res.prev = grand
                print(self)
            else:
                print("Complex right turn")
                if root == self.root:
                    self.root.left = self.left_turn(self.root.left)
                    self.root.left.prev = self.root
                    self.root = self.right_turn(self.root)
                else:
                    root.left = self.left_turn(root.left)
                    root.left.prev = root
                    res = self.right_turn(root)
                    res.prev = grand
                    if left_child:
                        grand.left = res
                    else:
                        grand.right = res
                print(self)
        elif lt.height - rt.height == -2:
            if rrt.height >= lrt.height:
                print("Simple left turn")
                if root == self.root:
                    self.root = self.left_turn(self.root)
                else:
                    res = self.left_turn(root)
                    grand.right = res
                    res.prev = grand
                print(self)
            else:
                print("Complex left turn")
                if root == self.root:
                    self.root.right = self.right_turn(root.right)
                    self.root.right.prev = self.root
                    self.root = self.left_turn(self.root)
                else:
                    root.right = self.right_turn(root.right)
                    root.right.prev = root
                    res = self.left_turn(root)
                    res.prev = grand
                    if left_child:
                        grand.left = res
                    else:
                        grand.right = res
                print(self)
        else:
            return False
        return True

    def next_value(self, current):
        """Find the smallest value bigger than given one"""
        if current == None:
            return None

        if current.right:
            current = current.right
            while current.left.value != None:
                current = current.left
            return current
        else:
            while current.prev and current != current.prev.left:
                current = current.prev
            if current.prev == None:
                return None
            return current

    def prev_value(self, current):
        """Find the biggest value smaller than the given one"""
        if current == None:
            return None

        if current.left:
            current = current.left
            while current.right.value != None:
                current = current.right
            return current
        else:
            while current.prev and current != current.prev.right:
                current = current.prev
            if current.prev == None:
                return None
            return current

    def remove(self, value):
        """Delete node with the first occurence of the specified value"""
        current = self.root
        if current == None:
            return "Tree is empty!!!"
        while current.value != None and current.value != value:
            if current.value < value:
                current = current.right
            else:
                current = current.left
        if current.value == None:
            return "There is no such an element!!!"
        if current.left.value != None and current.right.value != None:
            next_val = self.next_value(current)
            if next_val:
                current.value = next_val.value
                if next_val.prev == current:
                    current.right = next_val.right
                    if next_val.right:
                        next_val.right.prev = current
                else:
                    next_val.prev.left = next_val.right
                    if next_val.right != None:
                        next_val.right.prev = next_val.prev
                next_val.prev = current.prev
            else:
                prev_val = self.prev_value(current)
                current.value = prev_val.value
                if prev_val.prev == current:
                    current.left = prev_val.left
                    if prev_val.left:
                        prev_val.left.prev = current
                else:
                    prev_val.prev.right = prev_val.left
                    if prev_val.left != None:
                        prev_val.left.prev = prev_val.prev
                prev_val.prev = current.prev
        else:
            if current == current.prev.left:
                if current.left.value != None:
                    current.prev.left = current.left
                else:
                    current.prev.left = current.right
            else:
                if current.left.value != None:
                    current.prev.right = current.left
                else:
                    current.prev.right = current.right
        self.set_height(self.root)
        while current != None:
            self.balance_tree(current)
            current = current.prev
        return value

    def index_remove(self, index):
        """Remove element by index"""
        if self.root == None:
            return "Tree is empty!!!"
        nodes = [(self.root, 1)]
        i = 1
        found = False
        while nodes:
            current = nodes.pop(0)
            if current[1] == index:
                found = True
                break
            if current[0].right.value and current[0].left.value:
                nodes.append((current[0].left, i + 1))
                nodes.append((current[0].right, i + 2))
                i += 2
            elif current[0].right.value:
                nodes.append((current[0].right, i + 1))
                i += 1
            elif current[0].left.value:
                nodes.append((current[0].left, i + 1))
                i += 1

        if found == False:
            return "There is no element with such index!!!"
        current = current[0]
        value = current.value
        if current.left.value != None and current.right.value != None:
            next_val = self.next_value(current)
            if next_val:
                current.value = next_val.value
                if next_val.prev == current:
                    current.right = next_val.right
                    if next_val.right:
                        next_val.right.prev = current
                else:
                    next_val.prev.left = next_val.right
                    if next_val.right != None:
                        next_val.right.prev = next_val.prev
                next_val.prev = current.prev
            else:
                prev_val = self.prev_value(current)
                current.value = prev_val.value
                if prev_val.prev == current:
                    current.left = prev_val.left
                    if prev_val.left:
                        prev_val.left.prev = current
                else:
                    prev_val.prev.right = prev_val.left
                    if prev_val.left != None:
                        prev_val.left.prev = prev_val.prev
                prev_val.prev = current.prev
        else:
            if current == current.prev.left:
                if current.left.value != None:
                    current.prev.left = current.left
                else:
                    current.prev.left = current.right
            else:
                if current.left.value != None:
                    current.prev.right = current.left
                else:
                    current.prev.right = current.right
        self.set_height(self.root)
        while current != None:
            self.balance_tree(current)
            current = current.prev
        return value

    def prefix_traverse(self, current):
        """Traverse tree in a prefix order"""
        res = ""
        if current.value != None:
            left = self.prefix_traverse(current.left)
            right = self.prefix_traverse(current.right)
            res = str(current.value)
            if left != "":
                res += " " + left
            if right != "":
                res += " " + right
        return res

    def postfix_traverse(self, current):
        """Traverse tree in a postfix order"""
        res = ""
        if current.value != None:
            left = self.postfix_traverse(current.left)
            right = self.postfix_traverse(current.right)
            res =  ""
            if left != "":
                res += left + " "
            if right != "":
                res += right + " "
            res += str(current.value)
        return res

    def infix_traverse(self, current):
        """Traverse tree in an infix order"""
        res = ""
        if current.value != None:
            left = self.infix_traverse(current.left)
            right = self.infix_traverse(current.right)
            if left != "":
                res += left + " "
            res += str(current.value)
            if right != "":
                res += " " + right
        return res

    def __str__(self):
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
                current_level[current[1]-i] = str(current[0].value)
                nodes.append((current[0].left, current[1] * 2))
                nodes.append((current[0].right, current[1] * 2 + 1))
        res += " ".join(current_level) + "\n"
        return res

def main():
    avl_tree = AVLTree()
    while True:
        command = input(("Enter the command(insert/remove/prefix_traverse/postfix_traverse/infix_traverse/show/exit): "))
        if command == "insert":
            new_value = int(input("Enter the new value: "))
            new_node = Node(new_value)
            avl_tree.insert(new_node)
        elif command == "remove":
            delete_by = input("Do you want to remove by value or index(value/index)? ")
            if delete_by == "value":
                value = int(input("Enter the value: "))
                print(avl_tree.remove(value))
            elif delete_by == "index":
                index = int(input("Enter the index: "))
                print(avl_tree.index_remove(index))
        elif command == "prefix_traverse":
            print(avl_tree.prefix_traverse(avl_tree.root))
        elif command == "postfix_traverse":
            print(avl_tree.postfix_traverse(avl_tree.root))
        elif command == "infix_traverse":
            print(avl_tree.infix_traverse(avl_tree.root))
        elif command == "show":
            print(avl_tree)
        elif command == "exit":
            break
        else:
            print("Wrong command!!!")

if __name__ == '__main__':
    main()