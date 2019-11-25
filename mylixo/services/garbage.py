from .base import BaseService
from ..models.collect import Collect

BASE_URL = "https://coletaseletiva.procempa.com.br/coletaseletiva/rest/coleta/pesquisa;"


class GarbageService(BaseService):
    def __init__(self):
        super().__init__(BASE_URL)

    async def collection_times(self, address_code, number):
        """ Encontra o horário de coleta de um determinado endereço e número

        Retorna:
            Dia e horário de coleta para aquele endereço
        """
        res = await self.get(f"codLogradouro={address_code};numero={number}")

        if res and "erro" not in res:
            return Collect(time=res[0]["coleta"])
        return None
