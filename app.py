from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import os

app = FastAPI(
    title="Garmrus.IA - Sistema de Automação e Comprovantes",
    version="2.0.0",
    description="Backend oficial integrado para gestão de clientes e automação bancária."
)

DB_NAME = "garmrus.db"

def inicializar_banco():
    if os.path.exists("schema.sql"):
        with open("schema.sql", "r", encoding="utf-8") as f:
            script_sql = f.read()
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.executescript(script_sql)
        conn.commit()
        conn.close()

# Inicializa as tabelas ao iniciar o app
inicializar_banco()

class ClienteRequest(BaseModel):
    nome_cliente: str
    banco: str

@app.get("/")
def home():
    return {
        "status": "online",
        "sistema": "Garmrus.IA",
        "mensagem": "Cérebro principal ativo e operacional, chefia! 🚀"
    }

@app.post("/cadastrar-cliente")
def cadastrar_cliente(dados: ClienteRequest):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO clientes (nome, banco) VALUES (?, ?)",
            (dados.nome_cliente, dados.banco)
        )
        conn.commit()
        conn.close()
        return {"status": "sucesso", "mensagem": f"Cliente {dados.nome_cliente} registado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
