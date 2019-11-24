# MyLixo

Public API to provide POA city garbage collection time.

#### Instructions to execute (using venv) - Unix:

```bash
git clone https://github.com/gabrielweich/mylixo-api.git 
cd mylixo-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn mylixo.main:api --reload
```
