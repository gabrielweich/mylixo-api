from ..models.favorite import Favorite


class FavoriteController:
    def __init__(self, favorite_repository):
        self.favorite_repository = favorite_repository

    async def create(self, favorite: Favorite):
        """ Cria um endereço favorito vinculado a um usuário"""
        return await self.favorite_repository.create(favorite)

    async def update(self, favorite: Favorite):
        """ Atualiza um endereço favorito vinculado a um usuário"""
        return await self.favorite_repository.update(favorite)

    async def delete(self, user_id, favorite_id):
        """ Deleta um endereço favorito vinculado a um usuário"""
        return await self.favorite_repository.delete(user_id, favorite_id)

    async def get_by_user(self, user_id):
        """ Busca os endereços favoritos vinculados a um usuário"""
        return await self.favorite_repository.get_by_user(user_id)
