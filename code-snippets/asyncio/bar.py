'''
Low level asyncio stuff
'''

import asyncio

def coro():
    while True:
        val = yield
        print(f'Got {val}')
    # return 'monty'
    # return 100


f = coro()

print(type(coro))
print(type(f))

next(f)
f.send(42)
f.send(50)