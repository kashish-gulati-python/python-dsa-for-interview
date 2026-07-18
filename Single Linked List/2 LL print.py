# creates a node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# creates LL
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.value} -> ", end="")
            temp = temp.next
        print("None")

my_linked_list = LinkedList(2)

my_linked_list.print_list() # Output: 2 -> None