from .hash_func import get_hash
from .merge_sort import sort_func

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
            if self.keys[i] == elem["key"] and self.names[i] == elem["name"]:
                self.array[self.codes[i] + self.probes[i]] += elem["count"]
                return

        hash_code = get_hash(elem["key"])
        i = 0
        while self.array[hash_code + i] != 0:
            i += 1
        self.keys.append(elem["key"])
        self.names.append(elem["name"])
        self.codes.append(hash_code)
        self.probes.append(i)
        self.array[hash_code + i] = elem["count"]

    def delete(self, elem):
        """Delete element from table according to the hash-code and the name"""
        for i in range(len(self.keys)):
            if self.keys[i] == elem["key"] and self.names[i] == elem["name"]:
                res = (self.codes[i], [self.keys[i], self.names[i], self.array[self.codes[i] + self.probes[i]]])
                self.array[self.codes[i] + self.probes[i]] = 0
                self.keys.pop(i)
                self.names.pop(i)
                self.codes.pop(i)
                self.probes.pop(i)
                return res
        return "There is no such element!!!"

    def search(self, key):
        """Get all the elements with the key got as a parameter."""
        result = ""
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                result += str([self.keys[i], self.names[i], self.array[self.codes[i] + self.probes[i]]]) + " "
        if result == "":
            result = "There is no elements with such cypher!"
        return result

    def show(self, sort_by=""):
        """Show elements of the table using merge sort"""
        array_to_show = []
        for i in range(len(self.codes)):
            array_to_show.append([self.codes[i], self.keys[i], self.names[i], self.array[self.codes[i] + self.probes[i]]])
        sort_func(array_to_show, sort_by)