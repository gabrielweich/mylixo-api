from pydantic import BaseModel


class Favorite(BaseModel):
    address_code: int
    user_id: int
    label: str
