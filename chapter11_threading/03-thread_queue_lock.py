# 线程间通信

# 1. 生产者当生产10个url以后就就等待，保证detail_url_list中最多只有十个url
# 2. 当url_list为空的时候，消费者就暂停
import threading
import time
from threading import RLock

from chapter11_threading import variables


def get_detail_html(lock):
    """爬取文章详情"""
    detail_url_list = variables.detail_url_list
    while True:
        if len(variables.detail_url_list):
            lock.acquire()
            if len(detail_url_list):
                url = detail_url_list.pop()
                lock.release()
                print("get detail html started")
                time.sleep(2)
                print("get detail html end")
            else:
                lock.release()
                time.sleep(1)


def get_detail_url(lock):
    """爬取文章列表"""
    detail_url_list = variables.detail_url_list
    while True:
        print("get detail url started")
        time.sleep(4)
        for d in range(4):
            lock.acquire()
            if len(detail_url_list) >= 10:
                lock.release()
                time.sleep(1)
            else:
                detail_url_list.append("http://projectsedu.com/{id}".format(id=d))
                lock.release()
        print("get detail url end")


if __name__ == "__main__":
    lock = RLock()
    thread_detail_url = threading.Thread(target=get_detail_url, args=(lock,))
    thread_detail_url.start()
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(lock,))
        html_thread.start()
    start_time = time.time()
    # 当主线程退出的时候， 子线程kill掉
    print("last time: {}".format(time.time() - start_time))
