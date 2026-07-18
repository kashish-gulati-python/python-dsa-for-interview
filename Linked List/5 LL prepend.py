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
        print()

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
    
    def prepend(self, value):
        new_node = Node(value)
        # Edge case: empty LL
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # temp = self.head
            # self.head = new_node
            # self.head.next = temp
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

my_linked_list = LinkedList(2)
my_linked_list.append(3)

print("Normal LL: ", end="")
my_linked_list.print_list()

print("Normal LL after prepend: ", end="")
my_linked_list.prepend(4)
my_linked_list.print_list()

edge_linked_list = LinkedList(None)

print("Edge LL: ", end="")
edge_linked_list.print_list()

print("Edge LL after prepend: ", end="")
edge_linked_list.prepend(8)
edge_linked_list.print_list()
