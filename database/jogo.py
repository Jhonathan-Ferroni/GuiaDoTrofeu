from database.db import get_connection

def criar_jogo(id_jogo, app_id_steam, nome, conquistas_totais, icone_url):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO jogo (
            id_jogo, app_id_steam, nome, conquistas_totais, icone_url
        ) VALUES (?, ?, ?, ?, ?)
    """, (id_jogo, app_id_steam, nome, conquistas_totais, icone_url))

    conn.commit()
    conn.close()
