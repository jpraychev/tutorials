class Node():
    
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class Stack():

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):

        node = Node(data)
        
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        
        self.size += 1

    def pop(self):

        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None

    def xprint(self):
        
        current = self.top
        
        while current:
            value = current.data
            current = current.next
            yield value
        
    def peek(self):

        if self.top:
            return self.top.data
        else:
            return None

    def is_empty(self):

        if self.top:
            return False
        return True

stack = Stack()

stack.push(1)
print(stack.is_empty())