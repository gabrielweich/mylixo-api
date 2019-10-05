from .base import BaseService
from config import GARBAGE_URL


class GarbageService(BaseService):
    def __init__(self):
        super().__init__(GARBAGE_URL)

    async def collection_times(self, address_code, number):
        return await self.get(f"codLogradouro={address_code};numero={number}")
