import asyncio
import aiohttp  # pip install aiohttp aiodns


async def get( session: aiohttp.ClientSession, number: str, **kwargs):
    url = f"https://pokeapi.co/api/v2/pokemon/{number}"
    print(f"Requesting {url}")
    resp = await session.request('GET', url=url, **kwargs)
    # Note that this may raise an exception for non-2xx responses
    # You can either handle that here, or pass the exception through
    data = await resp.json()
    return data
    # print(f"Received data for {url}")
    # print(data['name'])

async def main(colors, **kwargs):
    # Asynchronous context manager.  Prefer this rather
    # than using a different session for each GET request
    async with aiohttp.ClientSession() as session:
        tasks = []
        for c in colors:
            tasks.append(get(session=session, number=c, **kwargs))
        # asyncio.gather() will wait on the entire task set to be
        # completed.  If you want to process results greedily as they come in,
        # loop over asyncio.as_completed()
        htmls = await asyncio.gather(*tasks, return_exceptions=True)
        print(htmls[0]['name'])


if __name__ == '__main__':
    colors = [1]  # ...
    # Either take colors from stdin or make some default here

    import time
    start = time.time()
    # On Windows seems to be a problem with EventLoopPolicy, use this snippet to work around it:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) 
    asyncio.run(main(colors))  # Python 3.7+
    print(f'Finished in {time.time()-start}')