import httpx


class BaseService:
    def __init__(self, url):
        self.url = url

    async def get(self, endpoint):
        async with httpx.AsyncClient() as client:
            res = await client.get(self.url + endpoint)
            return res.json()
