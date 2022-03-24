import aiohttp
import asyncio
from images import images as imgs
import time
import random

numbers = [5,2]

start_time = time.time()

async def generate_random_data():
    random_sleep = random.randint(1,5)
    print(f'Data will be ready after {random_sleep}')
    await asyncio.sleep(random_sleep)
    return random_sleep

async def say_after_after(data):
    random_data = await generate_random_data()
    return f'We have processed data {data + random_data}'

async def say_after(delay):
    await asyncio.sleep(delay)
    print(f'Finished after {delay}')
    result_from_other = await say_after_after(delay)
    print(result_from_other)

async def main():
    print(f"started at {time.strftime('%X')}")
    tasks = []
    for num in numbers:
        tasks.append(say_after(num))
    await asyncio.gather(*tasks)
    # print(results)

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())