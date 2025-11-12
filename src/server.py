import asyncio


async def _new_connection(reader, writer):
    # new connection
    ...


async def start_server(host: str, port: int):
    server_obj = await asyncio.start_server(_new_connection, host, port)

    async with server_obj:
        await server_obj.serve_forever()
