CREATE TABLE IF NOT EXISTS usuario (
    steam_id TEXT PRIMARY KEY,
    nome_perfil TEXT,
    perfil_publico INTEGER,
    data_cadastro DATE,
    ultima_sincronizacao DATE
);

CREATE TABLE IF NOT EXISTS jogo (
    id_jogo TEXT PRIMARY KEY,
    app_id_steam TEXT,
    nome TEXT,
    conquistas_totais INTEGER,
    icone_url TEXT
);

CREATE TABLE IF NOT EXISTS usuario_jogo (
    steam_id TEXT,
    id_jogo TEXT,
    ultima_execucao DATE,
    tempo_jogado REAL,
    numero_de_conquistas INTEGER,
    PRIMARY KEY (steam_id, id_jogo),
    FOREIGN KEY (steam_id) REFERENCES usuario(steam_id),
    FOREIGN KEY (id_jogo) REFERENCES jogo(id_jogo)
);

CREATE TABLE IF NOT EXISTS conquista (
    id_conquista TEXT PRIMARY KEY,
    id_jogo TEXT,
    nome TEXT,
    descricao TEXT,
    raridade TEXT,
    icone_url TEXT,
    FOREIGN KEY (id_jogo) REFERENCES jogo(id_jogo)
);

CREATE TABLE IF NOT EXISTS usuario_conquista (
    steam_id TEXT,
    id_conquista TEXT,
    desbloqueada INTEGER,
    data_desbloqueio DATE,
    PRIMARY KEY (steam_id, id_conquista),
    FOREIGN KEY (steam_id) REFERENCES usuario(steam_id),
    FOREIGN KEY (id_conquista) REFERENCES conquista(id_conquista)
);

CREATE TABLE IF NOT EXISTS sincronizacao (
    id_sync TEXT PRIMARY KEY,
    steam_id TEXT,
    data_sync DATE,
    status TEXT,
    mensagem_erro TEXT,
    FOREIGN KEY (steam_id) REFERENCES usuario(steam_id)
);
