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
        """Insert a new leaf"""
        new_node = Node(new_item)
        if self.root == None:
            self.root = new_node
            return
        current_element = self.root
        while True:
            if current_element.value > new_item:
                if current_element.left == None:
                    current_element.left = new_node
                    new_node.prev = current_element
                    return
                current_element = current_element.left
            else:
                if current_element.right == None:
                    current_element.right = new_node
                    new_node.prev = current_element
                    return
                current_element = current_element.right

    def straight_value_search(self, value, current_node=None):
        """Returns the values of the nodes we need to visit to get to the Node with specified value using straight search"""
        if current_node == None:
            current_node = self.root
        way = [current_node.value]
        if current_node.value == value:
            return way
        else:
            if current_node.left != None:
                left_search = self.straight_value_search(value, current_node.left)
                if left_search and left_search[len(left_search) - 1] == value:
                    way.extend(left_search)
                    return way
            if current_node.right != None:
                right_search = self.straight_value_search(value, current_node.right)
                if right_search and right_search[len(right_search) - 1] == value:
                    way.extend(right_search)
                    return way

    def reversed_value_search(self, value, current_node=None):
        """Returns the values of the nodes we need to visit to get to the Node with specified value using reversed search"""
        if current_node == None:
            current_node = self.root
        way = [current_node.value]
        if current_node.left != None:
            left_search = self.reversed_value_search(value, current_node.left)
            if left_search and left_search[len(left_search) - 1] == value:
                way.extend(left_search)
                return way
        if current_node.right != None:
            right_search = self.straight_value_search(value, current_node.right)
            if right_search and right_search[len(right_search) - 1] == value:
                way.extend(right_search)
                return way
        if current_node.value == value:
            return way

    def straight_index_search(self, index):
        """Returns the values of the nodes we need to visit to get to the Node with specified index using straight search"""
        nodes = [(self.root, 1, [self.root.value])]
        i = 2
        while nodes:
            current = nodes.pop(0)
            if current[1] == index:
                return current[2]
            if current[0].left:
                nodes.append((current[0].left, i, current[2] + [current[0].left.value]))
                i += 1
            if current[0].right:
                nodes.append((current[0].right, i, current[2] + [current[0].right.value]))
                i += 1
        return "There is no element with such index!!!"

    def reversed_index_search(self, index):
        """Returns the values of the nodes we need to visit to get to the Node with specified index using reversed search"""
        nodes = [(self.root, 1, [self.root.value])]
        j = 0
        i = 2
        while j < len(nodes):
            current = nodes[j]
            if current[1] == index:
                return current[2]
            if current[0].left:
                nodes.append((current[0].left, i, current[2] + [current[0].left.value]))
                i += 1
            if current[0].right:
                nodes.append((current[0].right, i, current[2] + [current[0].right.value]))
                i += 1
            j += 1
        while nodes:
            current = nodes.pop()
            if current[1] == index:
                return current[2]
        return "There is no element with such index!!!"

    def next_value(self, current):
        if current == None:
            return None

        if current.right:
            current = current.right
            while current.left:
                current = current.left
            return current
        else:
            while current.prev and current != current.prev.left:
                current = current.prev
            if current.prev == None:
                return None
            return current

    def prev_value(self, current):
        if current == None:
            return None

        if current.left:
            current = current.left
            while current.right:
                current = current.right
            return current
        else:
            while current.prev and current != current.prev.right:
                current = current.prev
            if current.prev == None:
                return None
            return current

    def index_remove(self, index):
        """Remove node with specified index."""
        if self.root == None:
            return "Tree is empty"
        nodes = [(self.root, 1)]
        i = 1
        found = False
        while nodes:
            current = nodes.pop(0)
            if current[1] == index:
                found = True
                break
            if current[0].right and current[0].left:
                nodes.append((current[0].left, i + 1))
                nodes.append((current[0].right, i + 2))
                i += 2
            elif current[0].right:
                nodes.append((current[0].right, i + 1))
                i += 1
            elif current[0].left:
                nodes.append((current[0].left, i + 1))
                i += 1

        if found == False:
            return "There is no element with such index!!!"
        current = current[0]
        res = current.value
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
            if current.left == current.right == None:
                if current == current.prev.right:
                    current.prev.right = None
                else:
                    current.prev.left = None
            else:
                prev_val = self.prev_value(current)
                current.value = prev_val.value
                if prev_val.prev == current:
                    current.left = prev_val.left
                    if prev_val.left:
                        prev_val.left.prev = current
                else:
                    prev_val.prev.left = prev_val.left
                    if prev_val.right != None:
                        prev_val.right = prev_val.prev
                prev_val.prev = current.prev
        return res


    def remove(self, value):
        """Delete Node with the specified value"""
        current = self.root
        if current == None:
            return "Tree is empty!!!"
        while current and current.value != value:
            if current.value > value:
                current = current.left
            else:
                current = current.right

        if current == None:
            return "No such an element!!!"

        res = current.value
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
            if current.left == current.right == None:
                if current == current.prev.right:
                    current.prev.right = None
                else:
                    current.prev.left = None
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
            if current[0] != None:
                current_level[current[1]-i] = str(current[0].value)
                nodes.append((current[0].left, current[1] * 2))
                nodes.append((current[0].right, current[1] * 2 + 1))
        res += " ".join(current_level) + "\n"
        return res

def main():
    tree = BinaryTree()
    while True:
        command = input("Enter command(insert/search/remove/show/exit): ")
        if command == "insert":
            # index_insert = input("Do you want to insert by index?(y/n) ")
            # if index_insert == "y":
            #     index = int(input("Enter the index: "))
            #     value = int(input("Enter the value: "))
            #     tree.index_insert(value, index)
            # elif index_insert == "n":
            value = int(input("Enter the value: "))
            tree.insert(value)
            # else:
            #     print("Wrong command!!!")
        elif command == "search":
            search_type = input("Enter search method(straight/reversed): ")
            if search_type == "straight":
                search_by = input("Enter search by which we are going to search(value/index): ")
                if search_by == "value":
                    value = int(input("Enter the value: "))
                    print(tree.straight_value_search(value))
                elif search_by == "index":
                    index = int(input("Enter the index: "))
                    print(tree.straight_index_search(index))
                else:
                    print("Wrong command!!!")
            elif search_type == "reversed":
                search_by = input("Enter search by which we are going to search(value/index): ")
                if search_by == "value":
                    value = int(input("Enter the value: "))
                    print(tree.reversed_value_search(value))
                elif search_by == "index":
                    index = int(input("Enter the index: "))
                    print(tree.reversed_index_search(value))
                else:
                    print("Wrong command!!!")
            else:
                print("Wrong command!!!")
        elif command == "remove":
            delete_by = input("Do you want to remove by value or index(value/index)? ")
            if delete_by == "value":
                value = int(input("Enter the value: "))
                print(tree.remove(value))
            elif delete_by == "index":
                index = int(input("Enter the index: "))
                print(tree.index_remove(index))
        elif command == "show":
            print(tree)
        elif command == "exit":
            break
        else:
            print("Wrong command!!!")

if __name__ == '__main__':
    main()