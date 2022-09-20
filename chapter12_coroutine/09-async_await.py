# python为了将语义变得更加明确，就引入了async和await关键词用于定义原生的协程

import types


@types.coroutine
def downloader(url):
    yield "bobby"

# async def downloader(url):
#     return "bobby"


async def download_url(url):
    html = await downloader(url)
    return html


if __name__ == "__main__":
    coro = download_url("http://www.imooc.com")
    coro.send(None)
