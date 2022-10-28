# Instruções:
 

### Crie o ambiente virtual
```
python -m venv venv
```
### Ative o venv
```bash
# linux: 

source venv/bin/activate

```

### Instale as dependências 
```
pip install -r requirements.txt
```
### Abra o arquivo .env.example e crie um arquivo .env baseado nele
```
# mkdir .env
```
### Crie e teste a conexão de um database Postgres

### Execute as migrações
```
./manage.py migrate
```