from pydantic import BaseModel


class Favorite(BaseModel):
    address_code: int
    address_number: int
    user_id: int
    label: str
