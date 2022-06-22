# BackEnd
# Banco de dados
import sqlite3 as lite

con = lite.connect("lista.db")

'''
with con:
    cursor = con.cursor()
    cursor.execute("CREATE TABLE tarefa(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")
'''
def inserir(i):
    with con:
        cursor = con.cursor()
        query = "INSERT INTO tarefa[nome] VALUES(?)"
        cursor.execute(query, i)
  

def selecionar():
    lista_tarefa = []
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM tarefa")
        row = cursor.fetchall()
        for r in row:
            lista_tarefa.append(r)
    return lista_tarefa


def deletar(i):
    with con:
        cursor = con.cursor()
        query = "DELETE FROM tarefa WHERE id=?"
        cursor.execute(query, i)


def atualizar(i):
    with con:
        cursor = con.cursor()
        query = "UPDATE tarefa SET id='?' "
        cursor.execute(query, i)


print(selecionar())





