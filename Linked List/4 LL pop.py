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

    def append(self, value):
        new_node = Node(value)
        if self.head is None: # if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        # Edge case 1: If no node
        if self.length == 0: # if self.head is None: # if self.tail is None:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None: # while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # Edge case 2: If only 1 node, then self.head and self.tail is still pointing to the only existing node
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

            

my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(8)

print(f"Normal linked list: ", end="")
my_linked_list.print_list()
print(f"Popped: {my_linked_list.pop()}")
print(f"Normal linked list after pop: ", end="")
my_linked_list.print_list()

edge1_ll = LinkedList(None)
print(f"Edge 1 linked list: ", end="")
edge1_ll.print_list()
print(f"Popped: {edge1_ll.pop()}")
print(f"Edge 1 linked list after pop: ", end="")
edge1_ll.print_list()

edge2_ll = LinkedList(1)
print(f"Edge 2 linked list: ", end="")
edge2_ll.print_list()
print(f"Popped: {edge2_ll.pop()}")
print(f"Edge 2 linked list after pop: ", end="")
edge2_ll.print_list()
