from .abstract import AbstractDatabase
import motor.motor_asyncio


class Database(AbstractDatabase):
    def __init__(self, configuration):
        super().__init__(configuration)
        self.client = None
        self.db = None

    async def connect(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.configuration["srv"])
        self.db = self.client.mylixo

    async def disconnect(self):
        if self.client:
            await self.client.close()
            self.db = None
