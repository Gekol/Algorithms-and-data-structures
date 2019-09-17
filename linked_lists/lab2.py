class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head

    def append(self, elem):
        self.tail.next = elem
        self.tail = self.tail.next

    def add_to_start(self, new_head):
        """Add new start element"""
        new_head.next = self.head
        self.head = new_head

    def clear(self):
        """Clear the list"""
        self.head = None

    def insert(self, new_elem, n):
        """Insert new element after the n-th element where n >= 0"""
        if n == 0:
            self.add_to_start(new_elem)
            return
        current_elem = self.head
        i = 1
        while current_elem.next != None and i != n:
            current_elem = current_elem.next
            i += 1

        new_elem.next = current_elem.next
        current_elem.next = new_elem

    def delete(self, n):
        if n == 1:
            self.head = self.head.next
            return
        current_elem = self.head
        i = 1
        while current_elem.next != None and i != n - 1:
            current_elem = current_elem.next
            i += 1

        current_elem.next = current_elem.next.next

    def delete_n(self, n):
        prev_elem = self.head
        current_elem = self.head.next
        i = 2
        while current_elem != None:
            if i % n == 0:
                prev_elem.next = current_elem.next
                current_elem = current_elem.next
                i = 1
            else:
                prev_elem = current_elem
                current_elem = current_elem.next
                i += 1

    def change_position(self, value, n):
        if self.head.value == value:
            current_elem = self.head
            self.head = self.head.next
            current_elem.next = self.head.next
            self.head.next = current_elem
            prev_elem = self.head
            n -= 1
        else:
            prev_elem = current_elem = self.head
            while current_elem.next != None and current_elem.value != value:
                prev_elem = current_elem
                current_elem = current_elem.next

        for i in range(n):
            if current_elem.next != None and i != n:
                next_elem = current_elem.next
                prev_elem.next = next_elem
                current_elem.next = next_elem.next
                next_elem.next = current_elem
                prev_elem = next_elem
            else:
                break

    def union(self, linked_list):
        new_list = self.copy()
        last_elem = new_list.head
        while last_elem.next != None:
            last_elem = last_elem.next
        last_elem.next = linked_list.copy().head
        return new_list

    def copy(self):
        new_list = LinkedList(Node(self.head.value))
        current_elem = self.head.next
        while current_elem != None:
            new_list.append(Node(current_elem.value))
            current_elem = current_elem.next
        return new_list

    def intersection(self, linked_list):
        current_elem = self.head
        set1 = {current_elem.value}
        while current_elem != None:
            set1.add(current_elem.value)
            current_elem = current_elem.next

        current_elem = linked_list.head
        set2 = {current_elem.value}
        while current_elem != None:
            set2.add(current_elem.value)
            current_elem = current_elem.next

        result_set = set1.intersection(set2)
        i = 0
        for elem in result_set:
            if i == 0:
                result_list = LinkedList(Node(elem))
            else:
                result_list.append(Node(elem))
            i += 1
        return result_list

    def sort(self, how):
        values = []
        current_elem = self.head
        while current_elem != None:
            values.append(current_elem.value)
            current_elem = current_elem.next
        if how == 1:
            values.sort()
        elif how == -1:
            values.sort(reverse=True)
        else:
            print("Incorrect sort key!!!")
            return
        sorted_list = LinkedList(Node(values[0]))
        for i in range(1, len(values)):
            sorted_list.append(Node(values[i]))
        return sorted_list

    def __str__(self):
        current_elem = self.head
        result = ""
        while current_elem != None:
            result += str(current_elem) + " "
            current_elem = current_elem.next
        return result

# linked_list = LinkedList(Node(1))
# linked_list.add_to_start(Node(0))
# linked_list.append(Node(2))
# print(linked_list)
# linked_list.delete(2)
# print(linked_list)
# linked_list.delete(1)
# print(linked_list)
# linked_list.add_to_start(Node(1))
# linked_list.insert(Node(3), 0)
# print(linked_list)
# linked_list.change_position(3, 2)
# print(linked_list)
# linked_list.insert(Node(4), 3)
# print(linked_list)
# linked_list.change_position(3, 2)
# print(linked_list)
# linked_list.change_position(2, 2)
# print(linked_list)
# linked_list = linked_list.sort(1)
# print(linked_list)
# linked_list = linked_list.sort(-1)
# copied_list = linked_list.copy()
# print(copied_list)
# print(linked_list)
# linked_list.delete_n(2)
# print(linked_list)
# copied_list = linked_list.union(copied_list)
# print(copied_list)
# l = LinkedList(Node(1))
# l.add_to_start(Node(2))
# l.add_to_start(Node(3))
# print(l)
# l.clear()
# print(l)
# linked_list = linked_list.intersection(copied_list)
# print(linked_list)

class CircleList:
    def __init__(self, head):
        self.length = 1
        self.head = head
        self.tail = head
        self.tail.next = self.head

    def append(self, new_node):
        """Add new element to the list"""
        if self.length == 1:
            self.head.next = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def __str__(self):
        current = self.head
        result = ""
        for i in range(self.length):
            result += str(current.value) + " "
            current = current.next
        return result

def main():
    n = int(input("Number of tickets: "))
    k = int(input("Number of students: "))

    students = CircleList(Node("Petrov"))
    students.append(Node("Ivanov"))
    students.append(Node("Sidorov"))
    students.append(Node("Makeev"))
    students.append(Node("Polev"))
    students.append(Node("Maksimov"))
    students.append(Node("Letuchyi"))
    students.append(Node("Tolmachov"))
    students.append(Node("Sokolovskyi"))
    students.append(Node("Domaschenko"))
    students.append(Node("Zinchenko"))

    tickets = CircleList(Node(1))
    tickets.append(Node(2))
    tickets.append(Node(3))
    tickets.append(Node(4))
    tickets.append(Node(5))
    tickets.append(Node(6))
    tickets.append(Node(7))
    tickets.append(Node(8))
    tickets.append(Node(9))
    tickets.append(Node(10))
    tickets.append(Node(11))

    students_count = 0
    current_student = students.head
    current_ticket = tickets.head
    while students_count != students.length:
        if students_count == 0:
            k -= 1
            n -= 1
        for i in range(k):
            current_student = current_student.next
        for i in range(n):
            current_ticket = current_ticket.next
        if students_count == 0:
            k += 1
            n += 1
        students_count += 1
        print(current_student.value, current_ticket.value)

if __name__ == '__main__':
    main()