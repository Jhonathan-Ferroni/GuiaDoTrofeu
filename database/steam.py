import requests
import sqlite3

API_KEY = "CF01FD0A733D98B10B9A10BBBFFE8BB7"

def buscar_jogos_steam():
    url = (
        "https://api.steampowered.com/"
        "IPlayerService/GetOwnedGames/v1/"
    )

    params = {
        "key": API_KEY,
        "steamid": steam_id,
        "include_appinfo": True
    }

    response = requests.get(url, params=params)
    return response.json()

def buscar_conquistas(appid):
    url = (
        "https://api.steampowered.com/"
        "ISteamUserStats/GetSchemaForGame/v2/"
    )

    params = {
        "key": API_KEY,
        "appid": appid
    }

    response = requests.get(url, params=params)
    return response.json()

def salvar_jogos(jogos):
    conn = sqlite3.connect("database/app.db")
    cursor = conn.cursor()

    for jogo in jogos:
        cursor.execute("""
            INSERT OR IGNORE INTO jogo (id, nome)
            VALUES (?, ?)
        """, (jogo["appid"], jogo["name"]))

    conn.commit()
    conn.close()

