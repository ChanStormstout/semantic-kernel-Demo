import asyncio

async def foo():
    print("Start foo")
    await asyncio.sleep(1)  # 模拟 I/O-bound 操作
    print("End foo")

async def bar():
    print("Start bar")
    await asyncio.sleep(2)  # 模拟 I/O-bound 操作
    print("End bar")

async def main():
    # 使用 asyncio.gather 并发运行多个协程
    await asyncio.gather(foo(), bar())

# 运行主协程
asyncio.run(main())
