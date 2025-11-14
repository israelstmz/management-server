import asyncio


async def _new_connection(reader, writer):
    # new connection
    ...


class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.obj = None

    async def start(self):
        self.obj = await asyncio.start_server(_new_connection, self.host, self.port)

        async with self.obj:
            await self.obj.serve_forever()

    async def close(self):
        self.obj.close()
        await self.obj.wait_closed()
