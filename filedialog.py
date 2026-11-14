import tkinter
from tkinter import filedialog

arquivo = filedialog.askopenfilename(title="Titulo filedialog askopenfilename")

print(arquivo)

pasta = filedialog.askdirectory(title="Titulo filedialog askdirectory")

print(pasta)