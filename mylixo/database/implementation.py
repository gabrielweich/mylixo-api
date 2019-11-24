import asyncpg
from .abstract import AbstractDatabase


class Database(AbstractDatabase):
    def __init__(self, configuration):
        super().__init__(configuration)
        self.client = None

    async def connect(self):
        self.client = await asyncpg.create_pool(self.configuration["dsn"], max_size=2, min_size=1)

    async def disconnect(self):
        if self.client is not None:
            await self.client.close()
