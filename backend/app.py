from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3 
import os
import asyncio
from backend.automacao.kamino_bot import executar_robo_kamino

app = FastAPI(
    title =  "Garmrus.IA - Sistema de Automação de Comprovantes",
    version = "2.0.0",
    description = "Backend oficial integrada para gestão de clientes e automação bancári."
)

DB_NAME = "garmrus.db"

def inicializar_banco():
    if os.path.exists ("schema.sql"):
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
        "mensagem": "Arquivo principal ativo e operacional!"
    }

@app.post("/cadastrar-cliente")
def cadastrar_cliente(dados: ClienteRequest):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO clientes (nome, banco) VALUES (?,?)",
            (dados.nome_cliente, dados.banco)
        )
        conn.commit()
        conn.close()
        return {
            "status": "sucesso", "mensagem": f"Cliente {dados.nome_cliente} registrado com sucesso!"
        }
    except Exception as e:
        raise HTTPException (status_code = 500, detail = str(e))

@app.post("/executar-automacao/{nome_cliente}")
async def disparar_automacao(nome_cliente: str):
    try:
        # Dispara o robo de forma leve para nao travar a API
        asyncio.create_task(executar_robo_kamino(nome_cliente))
        return{
            "status": "sucesso",
            "mensagem": f"Automação iniciada em segundo plano para o cliente: {nome_cliente}!"
        }
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))