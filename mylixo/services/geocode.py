from opencage.geocoder import OpenCageGeocode


class GeocodeService:
    def __init__(self, key):
        self.geocoder = OpenCageGeocode(key)

    def reverse_geocoding(self, latitude, longitude):
        """ Encontra a rua correspondente a uma determinada latitude/longitude

        Retorna:
            Objeto contendo a rua encontrada
        """
        res = self.geocoder.reverse_geocode(latitude, longitude, language="pt")
        if res:
            data = res[0]
            return {"street": data["components"]["road"], "address": data["formatted"]}
        return None
