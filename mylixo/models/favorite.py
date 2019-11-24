from pydantic import BaseModel


class Favorite(BaseModel):
    address_code: int
    address_number: int
    address_street: str = None
    user_id: int
    label: str
