import asyncio
import time

# 获取协程的返回值


# 使用asyncio
from functools import partial


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    return "bobby"


def callback(url, future):
    print(url)
    print("send email to bobby")


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # get_future = asyncio.ensure_future(get_html("http://www.imooc.com"))
    task = loop.create_task(get_html("http://www.imooc.com"))
    task.add_done_callback(partial(callback, "http://www.imooc.com"))
    loop.run_until_complete(task)
    print(task.result())
    print(time.time() - start_time)
