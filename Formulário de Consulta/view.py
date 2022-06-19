# importando SQLite
from re import I
import sqlite3 as lite

# CRUD
# C = Create (Inserir)
# R = Read (Leitura)
# U = Update (Att)
# D = Delete (Del)

# Conexão com BD
con = lite.connect('dados.db')


# Inserir informações
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, diaa_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)


# Acessar Infomações
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario" 
        cur.execute(query)
        info = cur.fetchall()
        
        for i in info:
            lista.append(i)
    return lista


def atualizar_info(i):
    # Atualizar Info
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, diaa_em=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query, i)

def deletar_info(i):
    # Deletear Info
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)

