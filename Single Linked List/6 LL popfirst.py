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
    
    def popfirst(self):
        # Edge case 1: Empty node
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # Edge case 1: only one node (after decrementing by 1)
        if self.length == 0:
            self.tail = None
        return temp

        # TC -> O(1)
        # SC -> O(1)

my_linked_list = LinkedList(2)
my_linked_list.append(3)

print("Normal LL: ", end="")
my_linked_list.print_list()

print("Normal LL after popfirst: ", end="")
my_linked_list.popfirst()
my_linked_list.print_list()

edge1_linked_list = LinkedList(2)

print("Only 1 element LL: ", end="")
edge1_linked_list.print_list()

print("Only 1 element LL after popfirst: ", end="")
edge1_linked_list.popfirst()
edge1_linked_list.print_list()

edge2_linked_list = LinkedList(None)

print("Empty LL: ", end="")
edge2_linked_list.print_list()

print("Empty LL after popfirst: ", end="")
edge2_linked_list.popfirst()
edge2_linked_list.print_list()
