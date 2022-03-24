import time
import matplotlib.pyplot as pyplot

class Queue():

    def __init__(self):
        self.size = 0
        self.list = []

    def enqueue(self, data):
        self.list.append(data)
        self.size += 1

    def dequeue(self):
        try:
            self.size -= 1
            return self.list.pop(0)
        except Exception as error:
            print(f'{error} is not possible')     

    def xprint(self, index):
        print(self.list[index])

q = Queue()

'''
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
pyplot.title("Enqueue time of lists")
pyplot.grid()
pyplot.show()


pyplot.plot(test_cases, time_dequeue)
pyplot.xlabel('Inserted items')
pyplot.ylabel('Dequeue time, s')
pyplot.xscale("log")
pyplot.title("Dequeue time of lists")
pyplot.grid()
pyplot.show()
'''