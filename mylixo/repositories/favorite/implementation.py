from .abstract import AbstractFavoriteRepo


class FavoriteRepository(AbstractFavoriteRepo):
    def __init__(self, database):
        self.database = database

    async def create(self, favorite):
        async with self.database.client.aquire() as con:
            await con.execute(
                f"""
                    INSERT INTO favorites (user_id, address_code, label)
                    VALUES ({favorite.user_id}, {favorite.address_code}, '{favorite.label}');
                """
            )
        return favorite

    async def update(self, favorite):
        pass

    async def delete(self, user_id, address_code):
        pass

    async def get_by_user(self, user_id):
        async with self.database.client.aquire() as con:
            rows = await con.execute(
                f"""
                    SELECT * FROM favorites
                    WHERE user_id = {user_id};
                """
            )

            return rows

        
