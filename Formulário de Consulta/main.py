#from cgitb import text
#from email.utils import collapse_rfc2231_value
#from os import listxattr
import email
from this import d
from tkinter import *
from tkinter.tix import Tree
#from tkinter import font
#from tkinter import _XYScrollCommand
#from turtle import back, width
#from click import command
# https://pypi.org/project/tkcalendar/
# pip install tkcalendar
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from tkinter import messagebox

# Importando views
from view import *


#################### Cores ######################
cor0 = "#f0f3f5"    # Preta
cor1 = "#feffff"    # Branca
cor2 = "#4fa882"    # Verde
cor3 = "#38576b"    # Valor
cor4 = "#403d3d"    # Letra
cor5 = "#e06636"    # - profit
cor6 = "#038cfc"    # Azul
cor7 = "#ef5350"    # Vermelha
cor8 = "#263238"    # + verde
cor9 = "#e9edf5"    # sky blue

################# criando janela ###############
janela = Tk()                                   # Janela
janela.title("")                                # Título
janela.geometry('1043x453')                     # Dimensão
janela.configure(background=cor9)               # Cor de fundo
janela.resizable(width=FALSE, height=FALSE)     # Re-dimensionamento 

### Dividindo janela ###
frame_e_cima = Frame(janela, width=360, height=50, bg=cor2, relief='flat')
frame_e_cima.grid(row=0, column=0)

frame_e_baixo = Frame(janela, width=360, height=403, bg=cor1, relief='flat')
frame_e_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_dir = Frame(janela, width=588, height=403, bg=cor1, relief='flat')
frame_dir.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

### Label Esquerda Cima ###
app_nome = Label(frame_e_cima, text='Formulário de Consulta', anchor=NW, font=('Ivy 13 bold'), bg=cor2, fg=cor1, relief='flat' )
app_nome.place(x=10, y=20)

# Variável tree global
global tree

# função Inserir
def inserir():
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    dia = e_cal.get()
    estado = e_estado.get()
    assunto = e_assunto.get()
    
    lista = [nome, email, tel, dia, estado, assunto]
    
    if nome == '':
        messagebox.showerror('Erro', 'O nome não pode ser vazio!')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')


        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_assunto.delete(0, 'end')

    for widget in frame_dir.winfo_children():
        widget.destroy()

    mostrar()


# Função atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_assunto.delete(0, 'end')

        e_nome.insert(0, tree_lista[1])
        e_email.insert(0, tree_lista[2])
        e_tel.insert(0, tree_lista[3])
        e_cal.insert(0, tree_lista[4])
        e_estado.insert(0, tree_lista[5])
        e_assunto.insert(0, tree_lista[6])

        def update():
            nome = e_nome.get()
            email = e_email.get()
            tel = e_tel.get()
            dia = e_cal.get()
            estado = e_estado.get()
            assunto = e_assunto.get()
            
            lista = [nome, email, tel, dia, estado, assunto, valor_id]
            
            if nome == '':
                messagebox.showerror('Erro', 'O nome não pode ser vazio!')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')


                e_nome.delete(0, 'end')
                e_email.delete(0, 'end')
                e_tel.delete(0, 'end')
                e_cal.delete(0, 'end')
                e_estado.delete(0, 'end')
                e_assunto.delete(0, 'end')

            for widget in frame_dir.winfo_children():
                widget.destroy()

            mostrar()

        b_confirmar = Button(frame_e_baixo, command=update, text='Confirmar', width=9, font=('Ivy 7 bold'), bg=cor2, fg=cor1, relief='raised')
        b_confirmar.place(x=110, y=370)

        

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela!')


# Função deletar 
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('Sucesso', 'Os dados foram deletados da Tabela com sucesso!')

        for widget in frame_dir.winfo_children():
            widget.destroy()

        mostrar()    

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela!')


### Label Esquerda Baixo ###
# Nome #
l_nome = Label(frame_e_baixo, text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat' )
l_nome.place(x=10, y=10)
e_nome = Entry(frame_e_baixo, width=40, justify='left', relief='solid' )
e_nome.place(x=15, y=40)
# Email#
l_email = Label(frame_e_baixo, text='Email: ', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat' )
l_email.place(x=10, y=70)
e_email = Entry(frame_e_baixo, width=40, justify='left', relief='solid' )
e_email.place(x=15, y=100)
# Fone #
l_tel = Label(frame_e_baixo, text='Fone: ', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat' )
l_tel.place(x=10, y=130)
e_tel = Entry(frame_e_baixo, width=40, justify='left', relief='solid' )
e_tel.place(x=15, y=160)

# Data e Estado da consulta #
l_cal = Label(frame_e_baixo, text='Data da consulta: ', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat' )
l_cal.place(x=15, y=190)
e_cal = DateEntry(frame_e_baixo, width=12, justify='left', relief='solid' )
e_cal.place(x=15, y=220)

l_estado = Label(frame_e_baixo, text='Estado da consulta: ', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat' )
l_estado.place(x=160, y=190)
e_estado = Entry(frame_e_baixo, width=22, justify='left', relief='solid' )
e_estado.place(x=160, y=220)


# Sobre #
l_assunto = Label(frame_e_baixo, text='Informações extra: ', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat' )
l_assunto.place(x=15, y=260)
e_assunto = Entry(frame_e_baixo, width=40, justify='left', relief='solid' )
e_assunto.place(x=15, y=290)

# Botões #
b_inserir = Button(frame_e_baixo, command=inserir, text='Inserir', width=9, font=('Ivy 9 bold'), bg=cor6, fg=cor1, relief='raised')
b_inserir.place(x=15, y=340)

b_att = Button(frame_e_baixo, command=atualizar, text='Atualizar', width=9, font=('Ivy 9 bold'), bg=cor2, fg=cor1, relief='raised')
b_att.place(x=125, y=340)

b_del = Button(frame_e_baixo, command=deletar, text='Deletar', width=9, font=('Ivy 9 bold'), bg=cor7, fg=cor1, relief='raised')
b_del.place(x=235, y=340)



######################### Frame Direita ############################
# Lista informações
def mostrar():

    global tree
    
    lista = mostrar_info()

    # Lista para cabeçalho #
    tabela_c = ['ID', 'Nome', 'Email', 'Telefone', 'Data', 'Estado', 'Sobre']

    df_list = lista

    tree = ttk.Treeview(frame_dir, selectmode='extended', columns=tabela_c, show='headings')

    # Scrollbar vertical #
    vsb = ttk.Scrollbar(frame_dir, orient='vertical', command=tree.yview)
    # Scrollbar horizontal
    hsb = ttk.Scrollbar(frame_dir, orient='horizontal', command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, stick='nsew')
    vsb.grid(column=1, row=0, stick='ns')
    hsb.grid(column=0, row=1, stick='ew')
    frame_dir.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "cente", "center"]
    h = [30, 170, 140, 100, 120, 50, 100]
    n = 0

    for col in tabela_c:
        tree.heading(col, text=col.title(), anchor=CENTER)
        #
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in lista:
        tree.insert('', 'end', values=item)

# Chamando função mostrar
mostrar()

janela.mainloop()                               # Chamando inicialização da janela 



