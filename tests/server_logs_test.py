import asyncio
import logging

from src.logs import setup_logs_pipe
from src.server import Server

from _test_pipe import Pipe


async def test(host="localhost", port=9000):
    test_pipe = Pipe()
    setup_logs_pipe(test_pipe)
    logging.getLogger().setLevel(level=logging.DEBUG)

    server = Server(host, port)
    server_task = asyncio.create_task(server.start())  # start server in task

    await asyncio.sleep(0.1)  # waiting for the log to be registered

    assert test_pipe[-1] == "server is up!", test_pipe[-1]  # [-1] = last item

    # close the server
    await server.close()
    server_task.cancel()

    assert test_pipe[-1] == "server is closed!", test_pipe[-1]


if __name__ == "__main__":
    asyncio.run(test())
    print("test is done!")
