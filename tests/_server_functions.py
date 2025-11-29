import asyncio


async def none(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    pass


async def echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    while True:
        data = await reader.readline()
        if not data:
            break  # connection is closed!
        writer.write(data)
        await writer.drain()
    writer.close()
    await writer.wait_closed()
