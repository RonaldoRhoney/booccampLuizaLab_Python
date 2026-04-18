import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.sqlite3')

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")

conexao.commit()
conexao.close()