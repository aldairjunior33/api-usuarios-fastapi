# Projeto API FastAPI + SQLAlchemy

Este projeto é uma API simples construída com FastAPI e SQLAlchemy, usando SQLite como banco de dados local. A documentação aqui descreve o que cada arquivo faz e a ordem lógica de construção do projeto.

## Estrutura do projeto

- `database.py` - configura a conexão com o banco de dados e cria os objetos de engine e sessão.
- `models.py` - define o modelo ORM `Usuario` e a base declarativa usada pelo SQLAlchemy.
- `main.py` - define a aplicação FastAPI, cria as tabelas e implementa as rotas de criação e listagem de usuários.
- `usuarios.db` - arquivo do banco de dados SQLite gerado pelo SQLAlchemy.
- `venv/` - ambiente virtual Python do projeto.

## Dependências

As dependências principais são:

- `fastapi`
- `uvicorn`
- `sqlalchemy`

### Instalação básica

1. Ative o ambiente virtual:
   - Windows PowerShell: `venv\Scripts\Activate.ps1`
   - Windows CMD: `venv\\Scripts\\activate.bat`

2. Instale as dependências (se ainda não estiverem instaladas):
   ```powershell
   pip install fastapi uvicorn sqlalchemy
   ```

## Arquivos e responsabilidades

### `database.py`

Este arquivo é responsável por configurar o banco de dados e a sessão do SQLAlchemy.

- `DATABASE_URL` define o caminho para o banco SQLite: `sqlite:///./usuarios.db`.
- `engine` é o objeto que representa a conexão com o banco de dados.
- `SessionLocal` é a fábrica que cria novas sessões de banco.
- `Base` é a classe base declarativa usada para definir modelos ORM.

### `models.py`

Este arquivo define o modelo da tabela do banco de dados.

- Importa `Base` de `database.py`.
- Define a classe `Usuario`, que representa a tabela `usuarios`.
- A classe `Usuario` possui os campos:
  - `id` (Integer, chave primária)
  - `nome` (String)
  - `email` (String)

### `main.py`

Este arquivo monta a API FastAPI e usa os modelos e o banco configurados nos outros arquivos.

- Importa `FastAPI` do `fastapi`.
- Importa `Session` do `sqlalchemy.orm` apenas para tipagem.
- Importa `engine` e `SessionLocal` de `database.py`.
- Importa `models` para registrar os modelos ORM e acessar `models.Usuario`.

Fluxo principal em `main.py`:

1. `models.Base.metadata.create_all(bind=engine)`
   - Cria as tabelas no banco de dados SQLite caso ainda não existam.

2. `app = FastAPI()`
   - Cria a aplicação FastAPI.

3. Define rota `GET /`:
   - Retorna um JSON com mensagem de funcionamento.

4. Define rota `POST /usuarios`:
   - Recebe `nome` e `email`.
   - Cria uma sessão com `SessionLocal()`.
   - Cria um novo objeto `models.Usuario`.
   - Adiciona o usuário ao banco, dá `commit` e retorna o ID.
   - Fecha a sessão.

5. Define rota `GET /usuarios`:
   - Cria uma sessão com `SessionLocal()`.
   - Consulta todos os usuários com `db.query(models.Usuario).all()`.
   - Fecha a sessão.
   - Retorna a lista de usuários.

## Ordem lógica de construção

1. **Configurar o banco de dados** (`database.py`):
   - Definir onde o banco ficará e criar `engine`, `SessionLocal` e `Base`.

2. **Definir os modelos** (`models.py`):
   - Criar a classe `Usuario` estendendo `Base`.
   - Definir os campos da tabela.

3. **Construir a aplicação FastAPI** (`main.py`):
   - Importar `engine`, `SessionLocal` e os modelos.
   - Criar as tabelas no banco.
   - Criar a instância `FastAPI()`.
   - Implementar rotas para criar e listar usuários.

## Como executar

No terminal, execute:

```powershell
uvicorn main:app --reload
```

Depois acesse:

- `http://127.0.0.1:8000/` — verifica se a API está funcionando
- `http://127.0.0.1:8000/usuarios` — lista todos os usuários
- `http://127.0.0.1:8000/docs` — documentação automática do FastAPI

## Notas finais

- `database.py` é a fundação que conecta seu app ao banco de dados.
- `models.py` descreve a estrutura dos dados que serão armazenados.
- `main.py` cria a API e usa as partes anteriores para fazer as operações.
- A ordem correta de construção é: primeiro banco, depois modelo, depois rotas.
