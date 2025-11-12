import asyncio

from src.server import start_server
from client import try_connect


async def test(host="localhost", port=9000):
    server_task = asyncio.create_task(start_server(host, port))  # start server in task

    # test client
    assert await try_connect(host, port), "server not found!"

    # close the server task
    server_task.cancel()


if __name__ == "__main__":
    asyncio.run(test())
    print("test is done!")
