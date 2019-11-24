import os


class Base:
    opencage_key = "22d0a7c38c6c46408479b5892a0fabdb"


class Dev(Base):
    database = {
        "srv": "mongodb+srv://admin:gesiel@cluster0-vnjra.gcp.mongodb.net/test?retryWrites=true&w=majority"
    }


class Prod(Base):
    database = {}


config = Prod() if os.getenv("ENV", "development") == "production" else Dev()
