from .hash_func import get_hash
from .merge_sort import sort_func
from .linked_list import LinkedList, Node

class HashTableChaining:
    """Hash-table using chaining"""
    def __init__(self):
        self.array = []
        for i in range(10000):
            self.array.append(LinkedList())
        self.codes = []

    def add(self, item):
        """Add new element or update the number of the element."""
        hash_code = get_hash(item['key'])
        current_elem = self.array[hash_code].head
        key_was = False
        element_was = False
        while current_elem != None:
            if current_elem.value[0] == item['key']:
                key_was = True
                if current_elem.value[1] == item['name']:
                    element_was = True
                    current_elem.value[2] += item['count']
                    break
            current_elem = current_elem.next
        if key_was != True:
            self.codes.append(hash_code)
        if element_was != True:
            self.array[hash_code].append(Node([item['key'], item['name'], item['count']]))
        return hash_code

    def delete(self, elem):
        """Delete element from table according to the hash-code and the name"""
        hash_code = get_hash(elem["key"])
        linked_list = self.array[hash_code]
        return linked_list.delete(elem["name"])

    def search(self, key):
        """Get all the elements with the key got as a parameter."""
        hash_code = get_hash(key)
        result = LinkedList()
        current_elem = self.array[hash_code].head
        while current_elem != None:
            if current_elem.value[0] == key:
                result.append(Node(current_elem.value))
            current_elem = current_elem.next
        return result

    def show(self, sort_by=""):
        """Show elements of the table using merge sort"""
        array_to_show = []
        for code in self.codes:
            linked_list = self.array[code]
            current_elem = linked_list.head
            while current_elem != None:
                array_to_show.append([code] + current_elem.value)
                current_elem = current_elem.next
        sort_func(array_to_show, sort_by)