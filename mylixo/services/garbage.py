from .base import BaseService
from ..config import GARBAGE_URL
from ..models.collect import Collect

class GarbageService(BaseService):
    def __init__(self):
        super().__init__(GARBAGE_URL)

    async def collection_times(self, address_code, number):
        res = await self.get(f"codLogradouro={address_code};numero={number}")
        if (res):
            return Collect(time=res[0]['coleta'])
