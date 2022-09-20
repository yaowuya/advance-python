import asyncio
import time

"""
事件循环+回调（驱动生成器）+epoll(IO多路复用)
asyncio是python用于解决异步io编程的一整套解决方案
tornado、gevent、twisted（scrapy， django channels）
torando(实现web服务器)， django+flask(uwsgi, gunicorn+nginx)
tornado可以直接部署， nginx+tornado
"""


# 使用asyncio
async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)  # 此处不能用time.sleep进行阻塞
    print("end get url")


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.imooc.com") for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)
