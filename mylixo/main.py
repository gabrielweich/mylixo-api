from fastapi import FastAPI
from services.address import AddressService
from services.garbage import GarbageService

app = FastAPI()


@app.get("/addresses")
async def addresses(street: str):
    return await AddressService().search_addresses(street)


@app.get("/garbage-collection")
async def garbage_collection(address_code: str, number: int):
    print(address_code, number)
    return await GarbageService().collection_times(address_code, number)