import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.sqlite3')
cursor = conexao.cursor()


def criar_tabela(conexao, cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT
    )
    """)
    conexao.commit()


def inserir_cliente(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?, ?)", data
    )
    conexao.commit()


def atualizar_registro(conexao, cursor, id, nome, email):
    data = (nome, email, id)
    cursor.execute(
        "UPDATE clientes SET nome = ?, email = ? WHERE id = ?", data
    )
    conexao.commit()