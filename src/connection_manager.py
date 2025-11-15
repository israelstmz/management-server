class ConnectionManager:
    def __init__(self, connections_function):
        self.connections_function = connections_function

    async def new(self, reader, writer):
        await self.connections_function(reader, writer)
