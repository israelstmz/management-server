import asyncio
import logging

from server import Server


if __name__ == "__main__":
    logging.getLogger().setLevel(level=logging.DEBUG)  # also show the lowest level logs (debug)
    server = Server("localhost", 9000)
    asyncio.run(server.start())
