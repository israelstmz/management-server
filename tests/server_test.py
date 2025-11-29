import asyncio

from _server_functions import none
from _client import Connection
from src.server import Server


async def test(host="localhost", port=9000):
    server = Server(host, port, none)
    server_task = asyncio.create_task(server.start())  # start server in task

    # trying to establish a connection
    assert await Connection.try_connect(host, port), "server not found!"

    await server.close()
    assert not await Connection.try_connect(host, port), "server not stop!"

    # close the server task
    server_task.cancel()


if __name__ == "__main__":
    asyncio.run(test())
    print("test is done!")
