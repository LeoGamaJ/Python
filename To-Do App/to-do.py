from ast import Lambda
from tkinter import *
from tkinter import ttk
from dbb import *

# FrontEnd

# Tabela de Cores

cor0 = "#000000"    # preta
cor1 = "#59656F"
cor2 = "#feffff"    # branca
cor3 = "#0074eb"    # azul
cor4 = "#f04141"    # vermelha
cor5 = "#59b356"    # verde
cor6 = "#cdd1cd"    # cinza

### Janela principal

janela = Tk()
janela.resizable(width=FALSE, height=FALSE)
janela.geometry("500x225")
janela.title("To-do App")
janela.configure(background=cor1)

### Dividindo janela principal

frame_esq = Frame(janela, width=300, height=200, bg=cor2, relief="flat")
frame_esq.grid(row=0, column=0, sticky=NSEW)

frame_dir = Frame(janela, width=200, height=250, bg=cor2, relief="flat")
frame_dir.grid(row=0, column=1, sticky=NSEW)

### Dividindo frame a esquerda

frame_esq_cima = Frame(frame_esq, width=300, height=50, bg=cor2, relief="flat")
frame_esq_cima.grid(row=0, column=0, sticky=NSEW)

frame_esq_baixo = Frame(frame_esq, width=300, height=150, bg=cor2, relief="flat")
frame_esq_baixo.grid(row=1, column=0, sticky=NSEW)

def main(a):
    # novo
    if a == "novo":
        label = Label(frame_esq_baixo, text="Insira nova tarefa", width=42, height=5, pady=15,   anchor=W)
        label.grid(row=0, column=0, sticky=NSEW, anchor=CENTER)
        
        entry = Entry(frame_esq_baixo, width=15)
        entry.grid(row=0, column=0, sticky=NSEW)

    # atualizar
    if a == "atualizar":
        print("atualizar")


### Botões

b_novo = Button(frame_esq_cima, text="Novo", width=10, height=1, bg=cor3, fg="white", font="5", anchor="center", relief=RAISED, command = lambda: main("novo"))
b_novo.grid(row=0, column=0, sticky=NSEW, padx=1)

b_remover = Button(frame_esq_cima, text="Remover", width=10, height=1, bg=cor4, fg="white", font="5", anchor="center", relief=RAISED)
b_remover.grid(row=0, column=1, sticky=NSEW, padx=1)

b_atualizar = Button(frame_esq_cima, text="Atualizar", width=10, height=1, bg=cor5, fg="white", font="5", anchor="center", relief=RAISED, command = lambda: main("atualizar"))
b_atualizar.grid(row=0, column=2, sticky=NSEW, padx=1)


### Adicionado listbox e label à direita

label = Label(frame_dir, text="Tarefas", width=37, height=1, pady=7, padx=10, relief="flat", anchor=W, font=("Courier 20 bold"), fg=cor0, bg=cor2)
label.grid(row=0, column=0, sticky=NSEW, padx=1)

listbox = Listbox(frame_dir, font=("Courier 12 bold"), width=1)
listbox.grid(row=1, column=0, sticky=NSEW, pady=5)

### Add tarefeas na Listbox

def mostrar():
    tarefas = selecionar()
    for item in tarefas:
        listbox.insert(END, item[1])


print(mostrar())
'''
for i in tarefas:
    listbox.insert(END, i)
'''






janela.mainloop()