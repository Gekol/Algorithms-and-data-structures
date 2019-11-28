class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def __str__(self):
        return str(self.value)

class Graph:
    def __init__(self):
        self.root = None

    def add(self, pair):
        if not self.root:
            self.root = Node(pair[0], [Node(pair[1])])
            return
        node = self.breadth_first_search(pair[0])
        new_node = Node(pair[1])
        node.children = node.children + [new_node]

    def breadth_first_search(self, value):
        nodes = [self.root]
        while nodes:
            current = nodes.pop(0)
            if current.value == value:
                return current
            nodes.extend(current.children)
        return "Not found!!!"

    def breath_first_show(self):
        nodes = [self.root]
        res = ""
        while nodes:
            current = nodes.pop(0)
            res += str(current) + " "
            nodes.extend(current.children)
        return res

    def depth_first_show(self, current, res=""):
        res += str(current) + " "
        for child in current.children:
            res = self.depth_first_show(child, res)
        return res

graph = Graph()
while True:
    command = input("Enter the command(insert/bfs/dfs/exit): ")
    if command == "insert":
        pair = input("Enter the pair(parent child): ")
        pair = list(map(int, pair.split()))
        graph.add(pair)
    elif command == "bfs":
        print(graph.breath_first_show())
    elif command == "dfs":
        print(graph.depth_first_show(graph.root))
    elif command == "exit":
        break
    else:
        print("Wrong command!!!")