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
        # Edge case: null LL
        if self.head is None: # if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # TC -> O(1)
    # SC -> O(1)

my_linked_list = LinkedList(2)

print("Normal LL: ", end="")
my_linked_list.print_list()
my_linked_list.append(3)
print("Normal LL after append: ", end="")
my_linked_list.print_list()

# Output: Normal LL: 2 -> None
# Normal LL after append: 2 -> 3 -> None