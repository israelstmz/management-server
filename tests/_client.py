import asyncio


class Connection:
    def __init__(self):
        # for the purpose of pep 8
        self.reader: asyncio.StreamReader | None = None
        self.writer: asyncio.StreamWriter | None = None

    async def _connect(self, host, port):
        self.reader, self.writer = await asyncio.open_connection(host, port)

    async def close(self):
        self.writer.close()
        await self.writer.wait_closed()

    async def read(self):
        """
        Reads until it reaches "\n" with timeout.
        :return:
        """
        try:
            data = await asyncio.wait_for(self.reader.readline(), timeout=5.0)
            return data.decode()
        except asyncio.TimeoutError:
            return "the timeout is over!"

    async def send(self, message: str):
        self.writer.write(message.encode())
        await self.writer.drain()

    @classmethod
    async def start_connection(cls, host: str, port: int):
        """
        Here is the starting point,
        because creating a connection is asynchronous, and __init__ is not asynchronous.
        :param host:
        :param port:
        :return:
        """
        c = cls()
        await c._connect(host, port)
        return c

    @classmethod
    async def try_connect(cls, host: str, port: int):
        """
        Returns if connected successfully.
        :param host:
        :param port:
        :return:
        """
        try:
            connection = await cls.start_connection(host, port)
            await connection.close()
            return True
        except ConnectionRefusedError:
            return False
