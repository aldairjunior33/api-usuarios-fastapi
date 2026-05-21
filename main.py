from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "API funcionando 🚀"}

@app.post("/usuarios")
def criar_usuario(nome: str, email: str):
    db: Session = SessionLocal()

    novo_usuario = models.Usuario(nome=nome, email=email)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    db.close()

    return {"msg": "Usuário criado", "id": novo_usuario.id}

@app.get("/usuarios")
def listar_usuarios():
    db: Session = SessionLocal()
    usuarios = db.query(models.Usuario).all()
    db.close()

    return usuarios