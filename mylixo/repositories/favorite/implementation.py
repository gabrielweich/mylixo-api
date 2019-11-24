from .abstract import AbstractFavoriteRepo
from ...models.favorite import Favorite, FavoriteEntity
from bson.objectid import ObjectId


class FavoriteRepository(AbstractFavoriteRepo):
    def __init__(self, database):
        self.database = database

    async def create(self, favorite: Favorite):
        collection = self.database.db.favorites
        res = await collection.insert_one(favorite.dict())
        inserted = await collection.find_one({"_id": res.inserted_id})
        return FavoriteEntity(**inserted, favorite_id=str(inserted["_id"]))

    async def update(self, favorite):
        collection = self.database.db.favorites
        await collection.find_one_and_update(
            {"_id": ObjectId(favorite.favorite_id), "user_id": favorite.user_id},
            {
                "$set": {
                    "label": favorite.label,
                    "address_code": favorite.address_code,
                    "address_street": favorite.address_street,
                    "address_number": favorite.address_number,
                }
            },
        )

        doc = await collection.find_one(
            {"_id": ObjectId(favorite.favorite_id), "user_id": favorite.user_id}
        )
        return FavoriteEntity(**doc, favorite_id=str(doc["_id"]))

    async def delete(self, user_id, favorite_id):
        collection = self.database.db.favorites
        doc = await collection.find_one_and_delete(
            {"_id": ObjectId(favorite_id), "user_id": user_id}
        )
        return FavoriteEntity(**doc, favorite_id=str(doc["_id"]))

    async def get_by_user(self, user_id):
        collection = self.database.db.favorites
        cursor = collection.find({"user_id": user_id})
        res = []
        for doc in await cursor.to_list(length=100):
            res.append(FavoriteEntity(**doc, favorite_id=str(doc["_id"])))
        return res
