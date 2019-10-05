from .base import BaseService
from config import ADDRESS_URL


class AddressService(BaseService):
    def __init__(self):
        super().__init__(ADDRESS_URL)

    async def search_addresses(self, street):
        return await self.get(street)
