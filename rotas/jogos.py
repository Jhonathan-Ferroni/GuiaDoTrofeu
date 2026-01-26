import tkinter as tk
from tkinter import ttk
import sqlite3


def buscar_jogos():
    conn = sqlite3.connect("database/app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id_jogo, nome FROM jogo")
    dados = cursor.fetchall()
    conn.close()
    return dados


class Jogos(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Título
        tk.Label(self, text="Tela de Jogos", font=("Arial", 16)).pack(pady=10)

        # Tabela
        self.tree = ttk.Treeview(
            self,
            columns=("id", "nome"),
            show="headings"
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Carregar dados do banco
        self.carregar_jogos()

        # Botão voltar
        tk.Button(
            self,
            text="Voltar ao Menu",
            command=master.mostrar_menu
        ).pack(pady=10)

    def carregar_jogos(self):
        for jogo in buscar_jogos():
            self.tree.insert("", tk.END, values=jogo)
