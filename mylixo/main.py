from fastapi import FastAPI
from .services.address import AddressService
from .services.garbage import GarbageService
from .services.geocode import GeocodeService
from starlette.middleware.cors import CORSMiddleware
from typing import List
from .models.address import Address
from .models.collect import Collect

origins = [
    "*",
]

app = FastAPI(
    title="MyLixo", description="Public API to provide POA city garbage collection time"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#Busca os endereços a partir de uma rua
@app.get("/api/addresses", response_model=List[Address])
async def addresses(street: str):
    return await AddressService().search_addresses(street)


#Busca o horário de coleta a partir de um endereço
@app.get("/api/garbage-collection", response_model=Collect)
async def garbage_collection(address_code: str, number: int):
    print(address_code, number)
    return await GarbageService().collection_times(address_code, number)


#Busca o endereço a partir das coordenadas
@app.get("/api/garbage-collection/coordinates", response_model=List[Address])
async def garbage_by_coordinates(latitude: float, longitude: float):
    data = GeocodeService().reverse_geocoding(latitude, longitude)
    if data is not None:
        return await AddressService().search_addresses(data['street'])