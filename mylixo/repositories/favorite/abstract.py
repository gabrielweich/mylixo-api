from abc import ABC, abstractmethod
from typing import List
from ...models.favorite import Favorite


class AbstractFavoriteRepo(ABC):
    def __init__(self, database):
        self.database = database
        super().__init__()

    @abstractmethod
    async def create(self, favorite: Favorite) -> Favorite:
        """ Persiste um objeto do tipo Favorito

        Retorna:
            Objeto to tipo Favorito que foi persistido
        """

    @abstractmethod
    async def get_by_user(self, user_id: int) -> List[Favorite]:
        """ Busca os favoritos de um determinado usuário

        Retorna:
            Lista de favoritos do usuário
        """

    @abstractmethod
    async def update(self, favorite) -> Favorite:
        """ Atualiza as informações de um favorito

        Retorna:
            O objeto do tipo Favorito atualizado
        """

    @abstractmethod
    async def delete(self, user_id: int, favorite_id: str) -> Favorite:
        """ Deleta um favorito de um determinado usuário

        Retorna:
            O objeto do tipo Favorito que foi deletado
        """
