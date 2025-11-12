import asyncio


async def new_connection(reader, writer):
    print("new_connection!")


class Server:
    def __init__(self, host: str, port: int):
        self.server_obj = None
        self.address = (host, port)

    async def start(self):
        self.server_obj = await asyncio.start_server(new_connection, *self.address)

        async with self.server_obj:
            await self.server_obj.serve_forever()


if __name__ == "__main__":
    server = Server("localhost", 9000)
    asyncio.run(server.start())
