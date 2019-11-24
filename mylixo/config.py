import os


class Base:
    opencage_key = "22d0a7c38c6c46408479b5892a0fabdb"


class Dev(Base):
    database = {
        "dsn": "postgres://sleyokyr:MIq481oqVQMD8JQL0bdt2vPAlCu6Swz7@tuffi.db.elephantsql.com:5432/sleyokyr"
    }


class Prod(Base):
    database = {}


config = Prod() if os.getenv("ENV", "development") == "production" else Dev()
