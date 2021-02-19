# MyLixo
API pública para fornecer o horário de coleta de lixo de Porto Alegre

----

#### Requisitos
* Python 3.6 +

#### Instruções para execução (usando venv) - Unix:

```bash
git clone https://github.com/gabrielweich/mylixo-api.git 
cd mylixo-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Executar a aplicação:
```bash
uvicorn mylixo.main:app --reload
```

Rodar os testes:
```bash
pytest
```


#### Implementação do framework
##### Hot spots:
* mylixo/database/implementation.py: Os métodos "connect" e "disconnect" ficam disponíveis para o desenvolvedor implementar alguma conexão com o banco de dados.
* mylixo/repositories/favorite/implementation.py: Os métodos de CRUD podem ser implementados se a aplicação for utilizá-los para salvar endereços de um usuário.

* mylixo/config.py: Aqui deve ser inserido as credencias para conexão com o banco de dados. A configuração a ser passada para o aquivo *database/implementation.py* é aquela contida na variável *database*. 

*Obs.: A implementação de desses pontos não é obrigatória caso não se implemente a funcionalidade de favoritos*


##### Camadas:
* Services: Realizam a comunicação com serviços externos, tais como o serviço de geolocalização e de coleta de lixo.
* Controllers: Implementam as operações e as regras de negócio esperadas para uma determinada rota.
* Repositories: Responsáveis pela comunicação com o mecanismo de persistência.


##### Inversão de controle:
*Módulos de alto nível não devem depender de módulos de baixo nível, ambos devem depender de abstrações.*

Pode ser evidenciado pela arquitetura desenvolvida. Exemplo: as classes do módulo *controller* não dependem das classes do tipo *repository*. Embora as utilizem para realizar a persistência dos dados, a inversão de controle é implementada aqui através da injeção de dependência ao passar as classes do tipo *repository* como parâmetro do construtor das classes *controller*.


