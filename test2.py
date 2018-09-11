# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:58:51 2018

@author: peter
"""

import time
import requests
import asyncio
total = 3
head = {"User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36"}


async def request():
    url = 'http://www.baidu.com/s?ie=UTF-8&wd=python'
    future = loop.run_in_executor(
        None, requests.get, url,head)
    response = await future
    response.encoding = response.apparent_encoding
    demo = response.text
    print(demo)


if __name__ == '__main__':
    time0 = time.time()
    tasks = [asyncio.ensure_future(request()) for i in range(0, total)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    time1 = time.time()
    print("爬取{0}个网页 ，总花费时间:{1:.2f}s".format(
        total, time1-time0), end="")
