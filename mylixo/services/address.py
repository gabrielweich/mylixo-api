from .base import BaseService
from ..config import ADDRESS_URL
from ..models.address import Address
from typing import List


class AddressService(BaseService):
    def __init__(self):
        super().__init__(ADDRESS_URL)

    async def search_addresses(self, street) -> List[Address]:
        res = await self.get(street)
        return list(map(
            lambda r: Address(
                address_code=r["codigoLogradouro"], street=r["nomeLogradouro"]
            ),
            res,
        ))
