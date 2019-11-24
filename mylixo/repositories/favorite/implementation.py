from .abstract import AbstractFavoriteRepo


class FavoriteRepository(AbstractFavoriteRepo):
    def __init__(self, database):
        self.database = database

    async def create(self, favorite):
        pass

    async def update(self, favorite):
        pass

    async def delete(self, user_id, address_code):
        pass

    async def get_by_user(self, user_id):
        pass
