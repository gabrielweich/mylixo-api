from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from typing import List
from .models.address import Address
from .models.collect import Collect
from .application import Application
from .config import config

origins = ["*"]

api = FastAPI(
    title="MyLixo", description="Public API to provide POA city garbage collection time"
)


api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


application: Application = Application(config)


@api.on_event("startup")
async def startup_event():
    await application.start()


@api.on_event("shutdown")
async def shutdown_event():
    await application.finish()


# Busca os endereços a partir de uma rua
@api.get("/api/addresses", response_model=List[Address])
async def addresses(street: str):
    controller = application.address_controller
    return await controller.find_by_street(street)


# Busca o horário de coleta a partir de um endereço
@api.get("/api/garbage-collection", response_model=Collect)
async def garbage_collection(address_code: str, number: int):
    controller = application.address_controller
    return await controller.garbage_time(address_code, number)


# Busca o endereço a partir das coordenadas
@api.get("/api/garbage-collection/coordinates", response_model=List[Address])
async def garbage_by_coordinates(latitude: float, longitude: float):
    controller = application.address_controller
    return await controller.find_by_coordinates(latitude, longitude)

