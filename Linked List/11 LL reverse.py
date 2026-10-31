class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length): # while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(10)
my_linked_list.append(27)
my_linked_list.append(22)

print("Normal LL: ", end="")
my_linked_list.print_list()

my_linked_list.reverse()

print("Reversed LL: ", end="")
my_linked_list.print_list()