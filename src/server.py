import asyncio

from src.connection_manager import ConnectionManager


class Server:
    def __init__(self, host: str, port: int, connection_function):
        self.host = host
        self.port = port

        self.obj = None
        self.connections = ConnectionManager(connection_function)

    async def start(self):
        self.obj = await asyncio.start_server(self.connections.new, self.host, self.port)

        async with self.obj:
            await self.obj.serve_forever()

    async def close(self):
        self.obj.close()
        await self.obj.wait_closed()
