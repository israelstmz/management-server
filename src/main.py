import asyncio

from server import Server


async def _new_connection(reader, writer):
    # new connection
    ...


if __name__ == "__main__":
    server = Server("localhost", 9000, _new_connection)
    asyncio.run(server.start())
