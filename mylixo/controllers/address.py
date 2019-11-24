class AddressController:
    def __init__(self, address_service, geocode_service, garbage_service):
        self.address_service = address_service
        self.geocode_service = geocode_service
        self.garbage_service = garbage_service

    async def find_by_street(self, street: str):
        return await self.address_service.search_addresses(street)

    async def find_by_coordinates(self, latitude: float, longitude: float):
        data = self.geocode_service.reverse_geocoding(latitude, longitude)
        if data is not None:
            return await self.address_service.search_addresses(data["street"])
        return None

    async def garbage_time(self, address_code: str, number: int):
        return await self.garbage_service.collection_times(address_code, number)
