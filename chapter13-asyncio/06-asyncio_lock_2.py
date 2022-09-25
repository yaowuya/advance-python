import asyncio
from asyncio import Lock

import aiohttp

cache = {}
lock = Lock()


async def get_stuff(url):
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET', url)
        cache[url] = stuff
        return stuff


async def parse_stuff():
    stuff = await get_stuff('')


async def use_stuff():
    stuff = await get_stuff('')


tasks = [parse_stuff(), use_stuff()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
