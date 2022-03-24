# Generators send method
import asyncio

def spam():
    item = yield
    print(f'Received: {item}')
    return 'A return from generator'

def run():
    s = spam()
    s.__next__()
    s.send(None)
    s.__next__()


async def foo(val):
    print('This is async function')
    print(val)
    return 'Return from async func'