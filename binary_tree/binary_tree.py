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

    # def index_insert(self, new_item, index):
    #     """Insert new item at the place of node with specified index"""
    #     new_node = Node(new_item)
    #     if self.root == None:
    #         self.root = new_node
    #         return
    #     if index == 1:
    #         self.root.prev = new_node
    #         if self.root.value < new_item:
    #             new_node.left = self.root
    #         else:
    #             new_node.right = self.root
    #         self.root = new_node
    #         return
    #     nodes = [(None, self.root, 1)]
    #     while nodes:
    #         current = nodes.pop(0)
    #         if current[2] == index:
    #             break
    #         if current[1] != None:
    #             nodes.append((current[1], current[1].left, current[2] + 1))
    #             nodes.append((current[1], current[1].right, current[2] + 2))
    #     prev_node = current[0]
    #     current = current[1]
    #     if new_item < prev_node.value:
    #         prev_node.left = new_node
    #     else:
    #         prev_node.right = new_node
    #
    #     if current != None:
    #         if new_item <= current.value:
    #             new_node.right = current
    #         else:
    #             new_node.left = current
    #         current.prev = new_node
    #     new_node.prev = prev_node

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

    def index_remove(self, index):
        """Remove node with specified index."""
        current = self.root
        if current == None:
            return "Tree is empty!!!"
        elif index == 1:
            if current.right:
                nodes_to_add = current.right.left
                left_subtree = current.left
                new_root = current.right
                current.right = None
                new_root.prev = None
                new_root.left = left_subtree
                if left_subtree:
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

        nodes = [(self.root, 1)]
        i = 2
        found = False
        if not nodes:
            return "Tree is empty!!!"
        while nodes:
            current = nodes.pop(0)
            if current[1] == index:
                found = True
                break
            if current[0].left != None:
                nodes.append((current[0].left, i))
                i += 1
            if current[0].right != None:
                nodes.append((current[0].right, i))
                i += 1

        if not found:
            return "There is no element with such index!!!"

        current = current[0]

        if current.right:
            nodes_to_add = current.right.left
            left_subtree = current.left
            new_node = current.right
            current.right = None
            new_node.prev = current.prev
            new_node.left = left_subtree
            if left_subtree:
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
                if left_subtree:
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
            if left_subtree:
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