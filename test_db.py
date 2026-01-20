from database.usuario import criar_usuario
from database.jogo import criar_jogo

criar_usuario(
    steam_id="76561198000000000",
    nome_perfil="Jhonathan",
    perfil_publico=1
)

criar_jogo(
    id_jogo="1",
    app_id_steam="570",
    nome="Dota 2",
    conquistas_totais=167,
    icone_url="https://..."
)

print("Teste concluído com sucesso")
