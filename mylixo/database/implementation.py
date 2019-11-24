from .abstract import AbstractDatabase


class Database(AbstractDatabase):
    async def connect(self):
        pass

    async def disconnect(self):
        pass
