from linked_lists.lab2 import Node, LinkedList

class Heap:
    def __init__(self):
        self.heap = [0]

    def heapify(self, index):
        """Makes sure that the heap keeps its property."""
        while index > 1:
            if self.heap[index] > self.heap[index // 2]:
                self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
                index //= 2
            else:
                break
        while index * 2 < len(self):
            left_elem = self.heap[index * 2]
            right_elem = 0
            if index * 2 + 1 < len(self.heap):
                right_elem = self.heap[index * 2 + 1]
            if self.heap[index] >= left_elem and self.heap[index] >= right_elem:
                break
            if left_elem > right_elem and left_elem > self.heap[index]:
                self.heap[index], self.heap[index * 2] = self.heap[index * 2], self.heap[index]
            elif right_elem >= left_elem and right_elem > self.heap[index]:
                self.heap[index], self.heap[index * 2 + 1] = self.heap[index * 2 + 1], self.heap[index]
            index *= 2

    def add(self, new_elem):
        """Add a new item at the end of the heap list and make sure the list has the property of a heap."""
        self.heap.append(new_elem)
        self.heapify(len(self.heap) - 1)

    def change_value(self, index, new_value):
        """Changes value of the element with the specified index"""
        self.heap[index] = new_value
        self.heapify(index)

    def delete(self, index=1):
        """Deletes element with the given index or extracts maximum"""
        if len(self) == 1:
            return "Empty heap!!!"
        self.heap[index], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[index]
        res = self.heap.pop()
        self.heapify(index)
        return res

    def heap_sort(self):
        """Shows sorted heap"""
        sorted_array = LinkedList(None)
        heap_to_use = Heap()
        heap_to_use.heap = self.heap[:]
        while len(heap_to_use) != 1:
            sorted_array.add_to_start(Node(heap_to_use.delete()))
        return sorted_array

    def __len__(self):
        """The length of the heap"""
        return len(self.heap)

    def __str__(self):
        return " ".join(list(map(str, self.heap[1:])))

def main():
    heap = Heap()
    while True:
        command = input(("Enter the command(add/change/delete/extract_max/heap_sort/show/exit): "))
        if command == "add":
            new_value = int(input("Enter the new value: "))
            heap.add(new_value)
        elif command == "change":
            index = int(input("Enter the index: "))
            new_value = int(input("Enter the new value: "))
            heap.change_value(index, new_value)
        elif command == "delete":
            index = int(input("Enter the index: "))
            heap.delete(index)
        elif command == "extract_max":
            heap.delete()
        elif command == "heap_sort":
            print(heap.heap_sort())
        elif command == "show":
            print(heap)
        elif command == "exit":
            break
        else:
            print("Wrong command!!!")

if __name__ == '__main__':
    main()