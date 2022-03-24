import random
import sys
import dis

n = 10
 
def list_func(n):
    
    m = 0
    arr = []

    while m < n:
        arr.append(random.randint(1,100))
        m += 1
    
    return arr
    

list_test = list_func(n)


def gen_func(n):

    m = 0

    while m < n:
        yield random.randint(1,100)
        m += 1

gen_test = gen_func(n)


def get_average_from_list():
    
    out = []
    total = sum(list_func(10))

    for num in list_func(10):
        out.append(round(100*num/total,2))

    return out

get_average_from_list()

def get_average_from_gen(gen):

    total = sum(gen)

    for num in gen:
        yield round(100*num/total,2)


test = get_average_from_gen(gen_func(10))

def new_gen():

    n = 2
    print(f'We yielded {n}')
    yield n

    n += 2
    print(f'We yielded {n}')
    yield n

    n += 2
    print(f'We yielded {n}')
    yield n

gen = new_gen()

next(gen)
next(gen)
next(gen)
next(gen)