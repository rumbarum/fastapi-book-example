import asyncio


async def q():
    print("시트웰: 답이 하나도 안 맞잖아?")
    await asyncio.sleep(3)


async def a():
    print("로저스: 하지만 빨랐죠.")


async def main():
    await asyncio.gather(q(), a())
