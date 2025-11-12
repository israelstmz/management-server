import asyncio


async def new_connection(reader, writer):
    print("new_connection!")


async def start_server(host: str, port: int):
    server_obj = await asyncio.start_server(new_connection, host, port)

    async with server_obj:
        await server_obj.serve_forever()


if __name__ == "__main__":
    asyncio.run(start_server("localhost", 9000))
