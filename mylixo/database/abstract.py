from abc import ABC, abstractmethod


class AbstractDatabase(ABC):
    def __init__(self, configuration):
        self.configuration = configuration
        super().__init__()

    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def disconnect(self):
        pass

    