import asyncio

#@asyncio.coroutine
#print("Hello world!")
    # 异步调用asyncio.sleep(1):
    #r = yield from asyncio.sleep(1)
    #print("Hello again!")
	
async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()