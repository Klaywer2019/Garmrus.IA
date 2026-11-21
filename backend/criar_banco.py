import sqlite3
#criar e conecta a base de dados
conexao = sqlite3.connect('database.db')
cursor = conexao.cursor()

#criar a tabela de clientes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
""")

conexao.commit()
conexao.close()
print("Banco de dados e tabela criados com sucesso!")