"""
Constraints:
1. Length is not given.
2. You cannot calculate length.
3. Only one time looping over the Linked List is allowed.
"""
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

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(10)
my_linked_list.append(27)
my_linked_list.append(22)
my_linked_list.append(2)

print("LL: ", end="")
my_linked_list.print_list()

print(my_linked_list.find_middle_node().value)