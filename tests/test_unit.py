from mylixo.controllers.favorite import FavoriteController
from mylixo.repositories.favorite.implementation import AbstractFavoriteRepo
from mylixo.models.favorite import FavoriteEntity
import uuid
import pytest


class FakeRepo(AbstractFavoriteRepo):
    def __init__(self):
        self.db = {}

    async def create(self, favorite):
        created = FavoriteEntity(**favorite, favorite_id=uuid.uuid4())
        self.db[created.favorite_id] = created
        return created

    async def update(self, favorite):
        old = self.db[favorite.favorite_id]
        new = FavoriteEntity(**{**old.dict(), **favorite.dict()})
        self.db[favorite.favorite_id] = new
        return new

    async def delete(self, user_id, favorite_id):
        del self.db[favorite_id]

    async def get_by_user(self, user_id):
        return [v for k, v in self.db.items() if v.user_id == user_id]

    async def get_favorite(self, favorite_id):
        return self.db[favorite_id]


TestController = FavoriteController(FakeRepo())
fakeFavorite = {"user_id": 1, "address_code": 1, "address_number": 1, "label": "test"}


@pytest.mark.asyncio
async def test_favorite_create():
    res = await TestController.create(fakeFavorite)
    assert res.favorite_id is not None


@pytest.mark.asyncio
async def test_favorite_delete():
    created = await TestController.create(fakeFavorite)
    await TestController.delete(created.user_id, created.favorite_id)
    saved = await TestController.get_by_user(created.user_id)
    assert created.favorite_id not in [s.favorite_id for s in saved]


@pytest.mark.asyncio
async def test_favorite_update():
    created = await TestController.create(fakeFavorite)
    created.label = "gesiel"
    res = await TestController.update(created)
    assert res.label == "gesiel"
