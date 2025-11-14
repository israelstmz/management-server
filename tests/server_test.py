import asyncio

from src.server import Server
from client import try_connect


async def test(host="localhost", port=9000):
    server = Server(host, port)
    server_task = asyncio.create_task(server.start())  # start server in task

    # test client
    assert await try_connect(host, port), "server not found!"

    await server.close()
    assert not await try_connect(host, port), "server not stop!"

    # close the server task
    server_task.cancel()


if __name__ == "__main__":
    asyncio.run(test())
    print("test is done!")
