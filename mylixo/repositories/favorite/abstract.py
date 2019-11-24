from abc import ABC, abstractmethod
from typing import List
from ...models.favorite import Favorite


class AbstractFavoriteRepo(ABC):
    def __init__(self, database):
        self.database = database
        super().__init__()

    @abstractmethod
    async def create(self, favorite: Favorite) -> Favorite:
        pass

    @abstractmethod
    async def get_by_user(self, user_id: int) -> List[Favorite]:
        pass

    @abstractmethod
    async def update(self, favorite) -> Favorite:
        pass

    @abstractmethod
    async def delete(self, user_id: int, favorite_id: str) -> Favorite:
        pass
