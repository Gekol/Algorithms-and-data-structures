class Node:
    def __init__(self, value):
        self.values = value
        self.children = []
        self.prev = None

    def __str__(self):
        res = ""
        for i in self.values:
            res += str(i) + " "
        return res

class BTree:
    """The size of the tree is 4"""
    def __init__(self, dimension):
        self.root = None
        self.dimension = dimension

    def search(self, value):
        current = self.root
        while current:
            try:
                if current.values[0] == value or current.values[len(current.values) - 1] == value:
                    return current
                if current.values[0] > value:
                    current = current.children[0]
                elif current.values[len(current.values) - 1] < value:
                    current = current.children[len(current.children) - 1]
                else:
                    for i in range(len(current.values) - 1):
                        if current.values[i] == value:
                            return current
                        elif current.values[i] < value < current.values[i + 1]:
                            current = current.children[i + 1]
                            break
            except:
                return "Not found!!!"
        return "Not found!!!"

    def insert(self, value):
        if not self.root:
            self.root = Node([value])
            return
        current = self.root
        while current.children != []:
            if value < current.values[0]:
                current = current.children[0]
            elif current.values[len(current.values) - 1] < value:
                current = current.children[len(current.children) - 1]
            else:
                for i in range(len(current.values) - 1):
                    if current.values[i] < value < current.values[i + 1]:
                        current = current.children[i]
        self.node_insert(value, current)

    def node_insert(self, value, node):
        if value >= node.values[len(node.values) - 1]:
            node.values.append(value)
        else:
            for i in range(len(node.values)):
                if value <= node.values[i]:
                    node.values.insert(i, value)
                    break
        if len(node.values) > 2 * self.dimension - 1:
            minimum = node.values[0]
            left_child = Node(node.values[:(2 * self.dimension - 1) // 2])
            left_child.prev = node.prev
            median = node.values[(2 * self.dimension - 1) // 2]
            node.values = node.values[(2 * self.dimension - 1) // 2 + 1:]
            left_child.children = node.children[:len(node.children) // 2][:]
            for i in left_child.children:
                i.prev = left_child
            node.children = node.children[len(node.children) // 2:]
            if node.prev == None:
                self.root = Node([median])
                self.root.children = [left_child, node]
                left_child.prev = node.prev = self.root
            else:
                added = False
                for i in range(len(node.prev.children)):
                    if node.prev.children[i].values[0] > minimum:
                        node.prev.children.insert(i, left_child)
                        added = True
                        break
                if not added:
                    node.prev.children.append(left_child)
                self.node_insert(median, node.prev)

    def delete(self, value):
        if self.root.values == [value] and self.root.children == []:
            self.root = None
            return
        node = self.search(value)
        value_index = node.values.index(value)
        if len(node.children) == 0:
            if len(node.values) >= self.dimension:
                node.values.remove(value)
            else:
                parent = node.prev
                index = parent.children.index(node)
                try:
                    brother = parent.children[index + 1]
                except:
                    brother = parent.children[index - 1]
                try:
                    y = parent.values[index]
                except:
                    y = parent.values[index - 1]
                if len(brother.values) >= self.dimension:
                    m = brother.values[0]
                    node.values[value_index] = y
                    try:
                        parent.values[index] = m
                    except:
                        parent.values[index - 1] = m
                    brother.values.pop(0)
                else:
                    if node.values[len(node.values) - 1] < brother.values[0]:
                        new_node = Node(node.values + [y] + brother.values)
                    else:
                        new_node = Node(brother.values + [y] + node.values)
                    parent.values.remove(y)
                    if not parent.values and parent == self.root:
                        self.root = new_node
                        return
                    node_index = parent.children.index(node)
                    parent.children[node_index] = new_node
                    parent.children.remove(brother)
                    new_node.prev = parent
        else:
            left_child = node.children[value_index]
            right_child = node.children[value_index + 1]
            if len(left_child.values) >= self.dimension:
                new_value = left_child.values[len(left_child.values) - 1]
                self.delete(new_value)
                node.values[value_index] = new_value
            elif len(right_child.values) >= self.dimension:
                new_value = right_child.values[0]
                self.delete(new_value)
                node.values[value_index] = new_value
            else:
                new_node = Node(left_child.values + right_child.values)
                node.children.remove(right_child)
                node.children[node.children.index(left_child)] = new_node
                node.values.remove(value)
        return value

    def __str__(self):
        if not self.root:
            return ""
        res = ""
        nodes = [self.root]
        level_elements_count = 1
        # current_level = ["0"][:] * level_elements_count
        while nodes:
            new_level = 0
            for i in range(level_elements_count):
                current = nodes.pop(0)
                res += str(current) + ", "
                for i in current.children:
                    nodes.append(i)
                    new_level += 1
            res += "\n"
            level_elements_count = new_level
        return res

def main():
    dimension = int(input("Enter the dimesions count: "))
    btree = BTree(dimension)
    print(btree)
    btree.insert(10)
    btree.insert(20)
    btree.insert(30)
    btree.insert(40)
    btree.insert(50)
    btree.insert(60)
    btree.insert(15)
    btree.insert(16)
    btree.insert(17)
    btree.insert(18)
    print(btree)
    btree.delete(30)
    print(btree)
    btree.delete(20)
    print(btree)
    btree.delete(16)
    print(btree)
    btree.delete(40)
    print(btree)
    btree.delete(50)
    print(btree)
    btree.delete(18)
    print(btree)
    while True:
        command = input("Enter the command(insert/delete/search/show/exit): ")
        if command == "insert":
            value = int(input("Enter the new value: "))
            btree.insert(value)
        elif command == "search":
            value = int(input("Enter the value: "))
            print(btree.search(value))
        elif command == "delete":
            value = int(input("Enter the value: "))
            print(btree.delete(value))
        elif command == "show":
            print(btree)
        elif command == "exit":
            break
        else:
            print("Wrong command!!!")

if __name__ == '__main__':
    main()