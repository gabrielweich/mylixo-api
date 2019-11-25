from abc import ABC, abstractmethod


class AbstractDatabase(ABC):
    def __init__(self, configuration):
        self.configuration = configuration
        super().__init__()

    @abstractmethod
    async def connect(self):
        """ Opcional: Cria uma conexão com algum banco de dados
            O método é executado antes de iniciar o servidor.
        """

    @abstractmethod
    async def disconnect(self):
        """ Opcional: Encerra a conexão criada
            O método é executado ao encerrar o servidor.
        """
