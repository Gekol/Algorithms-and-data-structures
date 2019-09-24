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