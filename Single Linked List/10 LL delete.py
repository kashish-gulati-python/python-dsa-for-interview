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

    def pop(self):
        if self.length == 0: 
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None 
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def delete(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next # temp = self.get(index)
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value

        # TC -> O(N)
        # SC -> O(1)


my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(10)
my_linked_list.append(27)
my_linked_list.append(22)

print("Normal LL: ", end="")
my_linked_list.print_list()

my_linked_list.delete(3)
my_linked_list.delete(-1)
my_linked_list.delete(199)

print("Updated LL: ", end="")
my_linked_list.print_list()
