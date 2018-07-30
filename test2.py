import time
import requests
import asyncio
import concurrent.futures
total = 100
thread = 4


async def request():
    with concurrent.futures.ThreadPoolExecutor(thread) as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor,
                requests.get,
                'http://127.0.0.1:5000'
            )
            for i in range(0, total)
        ]
        for response in await asyncio.gather(*futures):
            pass


if __name__ == '__main__':
    time0 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(request())
    time1 = time.time()
    print("爬取{0}个网页 ，总花费时间:{1:.2f}s".format(
        total, time1-time0), end="")
