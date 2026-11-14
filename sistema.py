import tkinter as tk
from tkinter.font import Font

#incia a janela
janela = tk.Tk()

#nome da janela
janela.title("Sistema de Cadastro de Usuários")

#tamanho da janela
janela.geometry("900x600")

#criar elemento
titulo = tk.Label(text="Meu app", font=Font(size=22, weight="bold", family="Arial"))
#posicionar na janela
titulo.pack(pady=(20,20))

#criar elemento
titulo = tk.Label(text="Meu app")
#posicionar na janela
titulo.pack(pady=(20,20))










#termina a janela
janela.mainloop()