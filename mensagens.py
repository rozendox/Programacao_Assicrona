import asyncio


async def outrafuncao():
    await asyncio.sleep(1)
    print("mensagem 1")


async def outrafuncao2():
    await asyncio.sleep(2)
    print("mensagem 2 ")


async def funcao():
    task = asyncio.create_task(outrafuncao())
    task1 = asyncio.create_task(outrafuncao2())

    await task
    await task1


asyncio.run(funcao())
