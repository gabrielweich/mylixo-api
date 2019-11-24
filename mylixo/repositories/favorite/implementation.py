from .abstract import AbstractFavoriteRepo
from ...models.favorite import FavoriteEntity


class FavoriteRepository(AbstractFavoriteRepo):
    def __init__(self, database):
        self.database = database

    async def create(self, favorite):

        async with self.database.client.acquire() as con:
            data = await con.fetchrow(
                f"""
                    INSERT INTO favorites (
                        user_id,
                        address_code,
                        address_number,
                        address_street,
                        label
                    )
                    VALUES ($1, $2, $3, $4, $5)
                    RETURNING *;
                """,
                favorite.user_id,
                favorite.address_code,
                favorite.address_number,
                favorite.address_street,
                favorite.label,
            )
            print(data)
            return FavoriteEntity(**data)

    async def update(self, favorite):
        pass

    async def delete(self, user_id, address_code):
        pass

    async def get_by_user(self, user_id):
        async with self.database.client.acquire() as con:
            rows = await con.fetch(
                f"""
                    SELECT * FROM favorites
                    WHERE user_id = {user_id};
                """
            )
            return [FavoriteEntity(**r) for r in rows]

