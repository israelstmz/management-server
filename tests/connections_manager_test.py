import asyncio

from _server_functions import echo
from _client import Connection
from src.server import Server


async def test(host="localhost", port=9000, test_message="Test Message!"):
    server = Server(host, port, echo)
    server_task = asyncio.create_task(server.start())  # start server in task

    connection = await Connection.start_connection(host, port)

    # "\n" marks the end of a message
    await connection.send(test_message+"\n")
    # without "\n" - a timeout error due to lack of response from the server, stuck in an unfinished read

    assert (error := await connection.read()) == test_message+"\n", error

    await connection.close()

    # close the server
    await server.close()
    server_task.cancel()


if __name__ == "__main__":
    asyncio.run(test())
    print("test is done!")
