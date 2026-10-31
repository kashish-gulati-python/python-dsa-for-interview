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

my_queue = Queue(2)

my_queue.print_list() # Output: 2 -> None