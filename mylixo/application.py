from .controllers.address import AddressController
from .controllers.favorite import FavoriteController

from .services.address import AddressService
from .services.garbage import GarbageService
from .services.geocode import GeocodeService

from .repositories.favorite.implementation import FavoriteRepository
from .database.implementation import Database


class Application:
    favorite_controller: FavoriteController = None
    address_controller: AddressController = None

    def __init__(self, config):
        self.database: Database = Database(config.database)

        self.favorite_repository = FavoriteRepository(self.database)

        self.geocode_service = GeocodeService(config.opencage_key)
        self.address_service = AddressService()
        self.garbage_service = GarbageService()
        self._init_controllers()

    async def start(self):
        await self.database.connect()

    async def finish(self):
        await self.database.disconnect()

    def _init_controllers(self):
        Application.address_controller = AddressController(
            self.address_service, self.geocode_service, self.garbage_service
        )

        Application.favorite_controller = FavoriteController(self.favorite_repository)
