from .base import BaseService
from ..models.address import Address
from typing import List


BASE_URL = "https://cdlrest.procempa.com.br/cdlrest/rest/endereco;q="


class AddressService(BaseService):
    def __init__(self):
        super().__init__(BASE_URL)

    async def search_addresses(self, street) -> List[Address]:
        res = await self.get(street)
        return list(
            map(
                lambda r: Address(
                    address_code=r["codigoLogradouro"], street=r["nomeLogradouro"]
                ),
                res,
            )
        )
