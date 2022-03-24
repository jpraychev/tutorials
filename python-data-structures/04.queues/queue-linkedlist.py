import time
import matplotlib.pyplot as pyplot

class Node():
    
    def __init__(self, data, previous, next):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return str(self.data)

class Queue():

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, data):

        node = Node(data, None, None)
        if self.first == None:
            self.first = node 
            self.last = node
        else:
            node.previous = self.last
            self.last.next = node
            self.last = node

        self.size += 1

    def dequeue(self):
        # check if queue is empty
        current = self.first
        if self.size == 1:
            # we have one item in the queue, return it immediately
            self.first = None
            self.last = None
            self.size -= 1
            print(f'You have dequeued the last element. Be careful!')
        elif self.size > 1:
            self.first = self.first.next
            self.first.previous = None
            self.size -=1
        else:
            print(f'Queue is already empty. Consider putting elements first!')
            exit()
        return current

q = Queue()

time_enqueue = []
time_dequeue = []

test_cases = [10, 100, 1000, 10000, 100000, 1000000, 10000000]


for x in test_cases:

    start = time.time()
    for j in range(x):
        q.enqueue(j)
    end = time.time()
    time_enqueue.append(end-start)

    start = time.time()
    q.dequeue()
    end = time.time()
    time_dequeue.append(end-start)


print(time_enqueue)
print(time_dequeue)

pyplot.plot(test_cases, time_enqueue)
pyplot.xlabel('Inserted items')
pyplot.ylabel('Enqueue time, s')
pyplot.xscale("log")
pyplot.title("Enqueue time of linked lists")
pyplot.grid()
pyplot.show()


pyplot.plot(test_cases, time_dequeue)
pyplot.xlabel('Inserted items')
pyplot.ylabel('Dequeue time, s')
pyplot.xscale("log")
pyplot.title("Dequeue time of linked lists")
pyplot.grid()
pyplot.show()

    

