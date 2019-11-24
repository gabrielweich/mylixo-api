from pydantic import BaseModel, validator
from typing import Union
from uuid import UUID


class Favorite(BaseModel):
    address_code: int
    address_number: int
    address_street: str = None
    user_id: int
    label: str


class FavoriteEntity(Favorite):
    favorite_id: Union[UUID, int, str]

    @validator("favorite_id")
    def valid_uuid(cls, value):
        return str(value)
