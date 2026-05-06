from tkinter import *
from tkinter import ttk
from tkinter import messagebox
janela = Tk()
janela.title("cadastro de clientes")
janela.geometry("700x400")
abas = ttk.Notebook(janela)
abas.pack(fill="both", expand=True)
aba1 = Frame(abas)
abas.add(aba1, text="cadastro")
aba2 = Frame(abas)
abas.add(aba2, text="clientes cadastrados")

Label(aba1, text="nome").pack(pady=5)
entry_nome = Entry(aba1, width=40)
entry_nome.pack()

Label(aba1, text="telefone").pack(pady=5)
entry_telefone = Entry(aba1, width=40)
entry_telefone.pack()

Label(aba1, text="email").pack(pady=5)
entry_email = Entry(aba1, width=40)
entry_email.pack()

Label(aba1, text="cidade").pack(pady=5)
entry_cidade = Entry(aba1, width=40)
entry_cidade.pack()


Button(aba1, text="cadastrar", bg="green", fg="white", width=20).pack(pady=20)

colunas = ("nome", "telefone", "email", "cidade")
tabela = ttk.Treeview(aba2, columns=colunas, show="headings")
for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=150)
tabela.pack(fill="both", expand=True, pady=20)
janela.mainloop()
