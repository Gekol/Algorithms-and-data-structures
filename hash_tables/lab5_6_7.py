import json
from .hashTableChaining import HashTableChaining
from .hashTableProbing import HashTableProbing

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def append(self, elem):
        if self.head:
            self.tail.next = elem
            self.tail = self.tail.next
        else:
            self.head = self.tail = elem

    def delete(self, value):
        current_elem = self.head
        if current_elem == None:
            return "The list is empty!!!"

        if current_elem.value[1] == value:
            res = self.head
            self.head = self.head.next
            return res

        while current_elem.next != None:
            if current_elem.next.value[1] == value:
                res = current_elem.next
                current_elem.next = current_elem.next.next
                return current_elem

    def __str__(self):
        current_elem = self.head
        result = ""
        while current_elem != None:
            result += str(current_elem) + " "
            current_elem = current_elem.next
        return result

def merge(left, right, index):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][1][index] <= right[j][1][index]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result = result + left[i:] + right[j:]
    return result

def merge_sort(array, index):
    if len(array) >= 2:
        left = merge_sort(array[:len(array) // 2],index)
        right = merge_sort(array[len(array) // 2:], index)
        array = merge(left, right, index)
    return array

def get_hash(elem):
    hash_code = 0
    for i in range(len(elem)):
        ch = elem[i]
        factor = i + 1
        if "0" <= ch <= "9":
            hash_code += (ord(ch) - 48) * factor
        elif "A" <= ch <= "Z":
            hash_code += (9 + ord(ch) - 64) * factor
        elif "a" <= ch <= "z":
            hash_code += (9 + 26 + ord(ch) - 96) * factor
    return hash_code

def read_file():
    with open("data.json", "r") as f:
        data = json.load(f)
    return data

def main():
    table_to_use = input("Do you want to use chaining?(y/n): ")
    if table_to_use == "y":
        print("Reading into table with chaining...")
        table = HashTableChaining()
    elif table_to_use == "n":
        print("Reading into table with probing")
        table = HashTableProbing()
    data = read_file()
    for i in data:
        table.add(i)
    while True:
        command = input("Enter the command(add/search/remove/show/exit): ")
        if command == "add":
            cypher = input("Enter the cypher: ")
            name = input("Enter the name: ")
            number = int(input("Enter the number: "))
            comm = [cypher, name, number]
            table.add(comm)
        elif command == "search":
            cypher = input("Enter the cypher: ")
            print(table.search(cypher))
        elif command == "remove":
            cypher = input("Enter the cypher: ")
            name = input("Enter the name: ")
            print(table.delete([cypher, name]))
        elif command == "show":
            order_by = input("Enter the order key(/cypher/name/count): ")
            table.show(order_by)
        elif command == "exit":
            break
        else:
            print("Wrong command")

if __name__ == '__main__':
    main()