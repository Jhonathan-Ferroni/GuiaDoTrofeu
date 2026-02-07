# ...existing code...
import os
import requests
import sqlite3

API_KEY = "CF01FD0A733D98B10B9A10BBBFFE8BB7"

def buscar_jogos_steam(steam_id):
    """Retorna lista de jogos (ou [] em caso de erro)."""
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    params = {
        "key": API_KEY,
        "steamid": steam_id,
        "include_appinfo": True,
        "include_played_free_games": True
    }

    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data.get("response", {}).get("games", [])
    except Exception:
        return []

def buscar_conquistas(appid):
    url = "https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/"
    params = {"key": API_KEY, "appid": appid}

    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {}

def salvar_jogos(jogos):
    db_path = os.path.join(os.path.dirname(__file__), "app.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for jogo in jogos:
        appid = jogo.get("appid")
        nome = jogo.get("name")
        if appid and nome:
            cursor.execute(
                "INSERT OR IGNORE INTO jogo (id_jogo, nome) VALUES (?, ?)",
                (appid, nome)
            )

    conn.commit()
    conn.close()

def buscar_e_salvar_jogos(steam_id):
    jogos = buscar_jogos_steam(steam_id)
    if jogos:
        salvar_jogos(jogos)
    return len(jogos)
# ...existing code...