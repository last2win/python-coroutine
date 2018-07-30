import time
import requests
from multiprocessing.dummy import Pool as ThreadPool
total = 100
thread = 4


def request():
    url = 'http://127.0.0.1:5000'
    r = requests.get(url, timeout=10)


def divide(i):
    for j in range(0, total//thread):
        request()


if __name__ == '__main__':
    time0 = time.time()
    i = [j for j in range(0, thread)]
    pool = ThreadPool(thread)
    pool.map(divide, i)
    pool.close()
    pool.join()
    time1 = time.time()
    print("爬取{0}个网页 ，总花费时间:{1:.2f}s".format(
        total, time1-time0), end="")
