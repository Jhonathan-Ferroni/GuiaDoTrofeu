from database.db import get_connection

def criar_usuario(steam_id, nome_perfil, perfil_publico):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO usuario (
            steam_id, nome_perfil, perfil_publico, data_cadastro
        ) VALUES (?, ?, ?, DATE('now'))
    """, (steam_id, nome_perfil, perfil_publico))

    conn.commit()
    conn.close()
