import time
from sys import getsizeof

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

    
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

# print(n1)

# print(id(n1.next))
# print(id(n2.data))

class SingleLinkedList():
    
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)    
        
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node

        self.size += 1

    def traverse(self):
        current = self.tail

        while current:
            value = current.data
            current = current.next
            yield value
    
    def traverse_list(self):
        current = self.tail

        arr = []

        while current:
            value = current.data
            current = current.next
            arr.append(value)

        return arr

    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                # print(f'Item to delete {current}')
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                return

            previous = current
            current = current.next

    def search(self, data):
        for node in self.traverse():
            if node == data:
                return True
        return False
        

    def clear(self):
        self.tail = None
        self.head = None


        
list = SingleLinkedList()
for i in range(4):
    list.append(i)

# print(f'Items before deletion')
# for item in list.traverse():
#     print(item)

# list.delete(3)

# print(f'Items after deletion')
# for item in list.traverse():
#     print(item)

list.delete(3)