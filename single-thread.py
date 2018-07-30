import time
import requests
total = 100


def request():
    url = 'http://127.0.0.1:5000'
    r = requests.get(url, timeout=10)


if __name__ == '__main__':
    time0 = time.time()
    for i in range(0, total):
        request()
    time1 = time.time()
    print("爬取{0}个网页 ，总花费时间:{1:.2f}s".format(
        total, time1-time0), end="")
