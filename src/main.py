import asyncio

from server import Server


if __name__ == "__main__":
    server = Server("localhost", 9000)
    asyncio.run(server.start())
