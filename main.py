import tkinter as tk
from rotas.menu import Menu
from rotas.jogos import Jogos


class TelaInicial(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Guia do Troféu", font=("Arial", 16)).pack(pady=10)
        tk.Label(self, text="Digite seu SteamID:").pack(pady=5)

        self.entry_steam = tk.Entry(self, width=30)
        self.entry_steam.pack(pady=5)

        tk.Button(
            self,
            text="Entrar",
            command=self.entrar
        ).pack(pady=10)

    def entrar(self):
        steam_id = self.entry_steam.get()

        if not steam_id:
            print("SteamID vazio!")
            return

        self.master.login(steam_id)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Guia do Troféu")
        self.geometry("400x400")

        self.steam_id = None
        self.tela_atual = None

        self.mostrar_tela_inicial()

    def trocar_tela(self, nova_tela):
        if self.tela_atual:
            self.tela_atual.destroy()

        self.tela_atual = nova_tela
        self.tela_atual.pack(fill="both", expand=True)

    def login(self, steam_id):
        self.steam_id = steam_id
        print(f"SteamID logado: {steam_id}")
        self.mostrar_menu()

    def mostrar_tela_inicial(self):
        self.trocar_tela(TelaInicial(self))

    def mostrar_menu(self):
        self.trocar_tela(Menu(self))

    def mostrar_jogos(self):
        self.trocar_tela(Jogos(self))


if __name__ == "__main__":
    app = App()
    app.mainloop()
