# async和await语法

import asyncio
import random


async def mygen(alist):
    while len(alist) > 0:
        c = random.randint(0, len(alist) - 1)
        print(alist.pop(c))
        await asyncio.sleep(1)


strlist = ['a', 'b', 'c']
intlist = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [mygen(strlist), mygen(intlist)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()