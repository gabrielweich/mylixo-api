import os


class Base:
    """Configurações comuns aos dois ambientes"""
    opencage_key = "22d0a7c38c6c46408479b5892a0fabdb"


class Dev(Base):
    """Configurações do ambiente de desenvolvimento"""
    database = {}


class Prod(Base):
    """Configurações do ambiente de produção"""
    database = {}


config = Prod() if os.getenv("ENV", "development") == "production" else Dev()
