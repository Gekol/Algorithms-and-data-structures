from .lab5_6_7 import get_hash, merge_sort

class HashTableProbing:
    """Hash-table using probing"""
    def __init__(self):
        self.array = []
        for i in range(10000):
            self.array.append(0)
        self.keys = []
        self.names = []
        self.codes = []
        self.probes = []

    def add(self, elem):
        """Add new element or update the number of the element."""
        for i in range(len(self.keys)):
            # Check if there was the same element
            if self.keys[i] == elem[0] and self.names[i] == elem[1]:
                self.array[self.codes[i] + self.probes[i]] += elem[2]
                return

        hash_code = get_hash(elem[0])
        i = 0
        while self.array[hash_code + i] != 0:
            i += 1
        self.keys.append(elem[0])
        self.names.append(elem[1])
        self.codes.append(hash_code)
        self.probes.append(i)
        self.array[hash_code + i] = elem[2]

    def delete(self, elem):
        """Delete element from table according to the hash-code and the name"""
        for i in range(len(self.keys)):
            if self.keys[i] == elem[0] and self.names[i] == elem[1]:
                res = self.array[self.codes[i] + self.probes[i]]
                self.array[self.codes[i] + self.probes[i]] = ["", "", 0]
                self.keys.pop(i)
                self.names.pop(i)
                self.codes.pop(i)
                self.probes.pop(i)
                return res
        return "There is no such element!!!"

    def search(self, key):
        """Get all the elements with the key got as a parameter."""
        result = []
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                result.append(self.array[self.codes[i] + self.probes[i]])
        return result

    def show(self, sort_by=""):
        """Show elements of the table using merge sort"""
        array_to_show = []
        for i in range(len(self.codes)):
            array_to_show.append((self.codes[i], [self.keys[i], self.names[i], self.array[self.codes[i] + self.probes[i]]]))
        if sort_by == "":
            print("Unsorted table")
            for i in array_to_show:
                print(i)
        elif sort_by == "cypher":
            print("Sorted table by cypher")
            array_to_show = merge_sort(array_to_show, 0)
            for i in array_to_show:
                print(i)
        elif sort_by == "name":
            print("Sorted table by name")
            array_to_show = merge_sort(array_to_show, 1)
            for i in array_to_show:
                print(i)
        elif sort_by == "count":
            print("Sorted table by count")
            array_to_show = merge_sort(array_to_show, 2)
            for i in array_to_show:
                print(i)
        else:
            print("Wrong data!!!")
