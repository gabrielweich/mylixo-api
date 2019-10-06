from pydantic import BaseModel


class Address(BaseModel):
    street: str
    address_code: int
