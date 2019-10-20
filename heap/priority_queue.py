from heap import Heap

class PriorityQueue(Heap):
    def __init__(self):
        super().__init__()

    def heapify(self, priority):
        """Makes sure that the heap keeps its property."""
        while priority > 1:
            if self.heap[priority][0] < self.heap[priority // 2][0]:
                self.heap[priority], self.heap[priority // 2] = self.heap[priority // 2], self.heap[priority]
                priority //= 2
            else:
                break
        while priority * 2 < len(self):
            left_elem = self.heap[priority * 2]
            right_elem = (float("inf"), 0)
            if priority * 2 + 1 < len(self.heap):
                right_elem = self.heap[priority * 2 + 1]
            if self.heap[priority][0] < left_elem[0] and self.heap[priority][0] < right_elem[0]:
                break
            if left_elem[0] < right_elem[0] and left_elem[0] < self.heap[priority][0]:
                self.heap[priority], self.heap[priority * 2] = self.heap[priority * 2], self.heap[priority]
            elif right_elem[0] < left_elem[0] and right_elem[0] < self.heap[priority][0]:
                self.heap[priority], self.heap[priority * 2 + 1] = self.heap[priority * 2 + 1], self.heap[priority]
            priority *= 2

    def insert(self, priority, value):
        """Insert new element with the given priority and value"""
        self.heap.append((priority, value))
        self.heapify(len(self) - 1)

    def extract_minimum(self):
        """Extract element with the highest priority"""
        if len(self) == 1:
            return "Queue is empty!!!"
        self.heap[1], self.heap[len(self) - 1] = self.heap[len(self) - 1], self.heap[1]
        res = self.heap.pop()
        self.heapify(1)
        return res[1]

    def show_minimum(self):
        """Show the element with the highest priority"""
        return self.heap[1]

    def delete(self, priority):
        """Delete element with the given priority"""
        for i in range(1, len(self.heap)):
            if self.heap[i][0] == priority:
                self.heap[i], self.heap[len(self) - 1] = self.heap[len(self) - 1], self.heap[i]
                res = self.heap.pop()
                self.heapify(i)
                return res
        return "There is no element with suh a priority!!!"

    def __len__(self):
        """The length of the queue"""
        return len(self.heap)

    def __str__(self):
        res = ""
        for elem in self.heap[1:]:
            res += "({}, {}) ".format(elem[0], elem[1])
        return res

def main():
    queue = PriorityQueue()
    while True:
        command = input(("Enter the command(insert/extract_min/show_min/delete/show/exit): "))
        if command == "insert":
            new_priority = int(input("Enter the priority: "))
            new_value = int(input("Enter the new value: "))
            queue.insert(new_priority, new_value)
        elif command == "extract_min":
            print(queue.extract_minimum())
        elif command == "show_min":
            print(queue.show_minimum())
        elif command == "delete":
            priority = int(input("Enter the priority: "))
            print(queue.delete(priority))
        elif command == "show":
            print(queue)
        elif command == "exit":
            break
        else:
            print("Wrong command!!!")
#
# def main():
#     pass
#
if __name__ == '__main__':
    main()