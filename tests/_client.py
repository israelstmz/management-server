import asyncio


async def _close_connection(writer):
    writer.close()
    await writer.wait_closed()


async def try_connect(host: str, port: int):
    try:
        reader, writer = await asyncio.open_connection(host, port)
        await _close_connection(writer)
        return True
    except ConnectionRefusedError:
        return False
