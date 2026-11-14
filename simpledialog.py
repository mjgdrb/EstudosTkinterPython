import tkinter
from tkinter import simpledialog

nome = simpledialog.askstring(title="Titulo do simpledialog askstring", prompt="Escreva o seu nome")


if nome:
    print(nome)


idade = simpledialog.askinteger(title="Titulo do simpledialog askinteger", prompt="Escreva a sua idade")


if idade >= 0:
    print(idade)

