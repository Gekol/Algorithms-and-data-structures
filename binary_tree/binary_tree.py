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

    def __str__(self):
        res = ""
        nodes = [self.root]
        i = 1
        j = 0
        while nodes:
            current = nodes.pop(0)
            if current == None:
                res += "0 "
            else:
                res += str(current) + " "
                nodes.append(current.left)
                nodes.append(current.right)
            j += 1
            if j == i:
                res += "\n"
                j = 0
                i *= 2
        return res

    def remove(self, value):
        """Delete Node with the specified value"""
        current = self.root
        if current == None:
            return "Tree is empty!!!"
        elif current.value == value:
            if current.right:
                nodes_to_add = current.right.left
                left_subtree = current.left
                new_root = current.right
                current.right = None
                new_root.prev = None
                new_root.left = left_subtree
                left_subtree.prev = new_root
                self.root = new_root
                self.insert(nodes_to_add)
                return current.value
            else:
                new_root = current.left
                current.left = None
                new_root.prev = None
                self.root = new_root
                return current.value
        while current and current.value != value:
            if current.value > value:
                current = current.left
            else:
                current = current.right

        if current == None:
            return "No such an element!!!"

        if current.right:
            nodes_to_add = current.right.left
            left_subtree = current.left
            new_node = current.right
            current.right = None
            new_node.prev = current.prev
            new_node.left = left_subtree
            left_subtree.prev = new_node
            if current == current.prev.left:
                current.prev.left = new_node
            else:
                current.prev.right = new_node
            self.insert(nodes_to_add)
            return current.value
        elif current.left:
            current.left.prev = current.prev
            if current == current.prev.left:
                current.prev.left = current.left
            else:
                current.prev.right = current.left
            return current
        else:
            if current == current.prev.left:
                current.prev.left = None
            else:
                current.prev.right = None
            return current


def main():
    tree = BinaryTree()
    while True:
        command = input("Enter command(insert/search/remove/exit): ")
        if command == "insert":
            value = int(input())
            tree.insert(Node(value))
        elif command == "remove":
            value = int(input())
            print(tree.remove(value))
        elif command == "search":
            search_type = input("Enter search method(straight/reversed): ")
            if search_type == "straight":
                search_by = input("Enter search by which we are going to search(value/index): ")
                if search_by == "value":
                    value = int(input("Enter the value: "))
                    print(tree.straight_value_search(value))
                elif search_by == "index":
                    index = int(input("Enter the index: "))
                    print(tree.straight_index_search(value))
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
        elif command == "exit":
            break
        else:
            print("Wrong command!!!")

if __name__ == '__main__':
    main()