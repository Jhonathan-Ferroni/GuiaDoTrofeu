import tkinter as tk
from rotas.menu import Menu


class TelaInicial(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Seja bem-vindo ao Guia do Troféu!").pack(pady=20)

        tk.Button(
            self,
            text="Entrar no Menu",
            command=master.mostrar_menu
        ).pack(pady=10)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Guia do Troféu")
        self.geometry("400x400")

        self.tela_atual = None
        self.mostrar_tela_inicial()

    def trocar_tela(self, nova_tela):
        if self.tela_atual:
            self.tela_atual.destroy()

        self.tela_atual = nova_tela
        self.tela_atual.pack(fill="both", expand=True)

    def mostrar_tela_inicial(self):
        self.trocar_tela(TelaInicial(self))

    def mostrar_menu(self):
        self.trocar_tela(Menu(self))


if __name__ == "__main__":
    app = App()
    app.mainloop()
