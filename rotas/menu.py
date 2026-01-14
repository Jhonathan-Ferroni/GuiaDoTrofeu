import tkinter as tk


class Menu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Menu").pack(pady=20)

        tk.Button(self, text="Jogos", command=self.acao_jogos).pack(pady=10)
        tk.Button(self, text="Configurações", command=self.acao_config).pack(pady=10)
        tk.Button(self, text="Sair", command=master.destroy).pack(pady=10)

    def acao_jogos(self):
        print("Clicou em Jogos")

    def acao_config(self):
        print("Clicou em Configurações")
