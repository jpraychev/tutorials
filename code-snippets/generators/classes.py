
import sys
import random
import itertools

class RandomNumbers(object):

    def __init__(self, arr):
        self.arr = arr

    def __iter__(self):
        for num in self.arr:
            yield num

# arr = []

# for _ in range(10):
    # arr.append(random.randint(1,100))
arr = [random.randint(1,100) for _ in range(10)]

print(arr)
def gen_func1(arr):

    for x in arr:
        yield x

# def gen_func(num):

#     for n in num:
#         yield n

def gen_func(n):

    m = 0
    while m < n:
        yield random.randint(1,100)
        m += 1

iter_obj = gen_func(10)
# a,b = itertools.tee(iter_obj, 2)

# print(a)
# print(b)

# print(list(a))
# print(list(b))

def get_average(gen):

    total = sum(gen)

    print(f'Random numbers -> {list(gen)}')
    print(f'Total -> {total}')
    
    for num in gen:
        yield round(100 * num / total,2)

test1 = gen_func1(arr)
# print(test1)s

test2 = get_average(test1)

# print(test2.__next__())

obj = RandomNumbers(arr)

# obj = gen_func1(arr)
a = iter(obj)
b = iter(obj)

print(a)
print(b)


print(f'Average -> {list(get_average(obj))}')