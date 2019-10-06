from opencage.geocoder import OpenCageGeocode


class GeocodeService:
    def __init__(self):
        self.geocoder = OpenCageGeocode('22d0a7c38c6c46408479b5892a0fabdb')


    def reverse_geocoding(self, latitude, longitude):
        res = self.geocoder.reverse_geocode(latitude, longitude, language='pt')
        if res:
            data = res[0]
            return {'street': data['components']['road'], 'address': data['formatted'] }
        return None
