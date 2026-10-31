class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_list(self):
        temp = self.first
        while temp is not None:
            print(f"{temp.value} -> ", end="")
            temp = temp.next
        print("None")

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return new_node

my_queue = Queue(2)

my_queue.enqueue(4)
my_queue.enqueue(1)
my_queue.enqueue(8)

my_queue.print_list() # Output: 2 -> 4 -> 1 -> 8 -> None