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
    
    def get(self, index):
        # Edge cases: index < 0, index > length of LL
        if index < 0 or index >= self.length:
            return None 
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(10)
my_linked_list.append(27)

print("Normal LL: ", end="")
my_linked_list.print_list()

print("Get index = 2: ", end="")
print(my_linked_list.get(2))

print("Get index = 100 (more than LL length): ", end="")
print(my_linked_list.get(100))

print("Get index = -2 (more than LL length): ", end="")
print(my_linked_list.get(-2))
