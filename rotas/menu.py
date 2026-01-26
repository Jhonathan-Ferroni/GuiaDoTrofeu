import tkinter as tk


class Menu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Menu").pack(pady=20)

        tk.Button(self, text="Jogos", command=master.mostrar_jogos).pack(pady=10)
        tk.Button(self, text="Configurações", command=self.acao_config).pack(pady=10)
        tk.Button(self, text="Sair", command=master.destroy).pack(pady=10)
        
    def acao_config(self):
        print("Clicou em Configurações")
