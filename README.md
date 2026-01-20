# 🏆 Guia de Troféus Steam

> Uma aplicação integrada à Steam para otimizar a caça por conquistas (achievements).

Esta aplicação permitirá a visualização organizada de jogos e conquistas da sua biblioteca Steam. Cada conquista possui uma interface dedicada contendo dicas, guias em vídeo, imagens e conteúdos explicativos para auxiliar na "platina" (100% de conclusão) dos jogos.

## 📸 Screenshots

Aqui estão algumas prévias da interface do projeto:

| Menu de Login | Menu de Seleção |
|:---:|:---:|
| <img src="./imagens/1.png" alt="Tela Principal com lista de jogos" width="400"> | <img src="./imagens/2.png" alt="Detalhes da conquista e dicas" width="400"> |

---

## 🛠️ Funcionalidades

- **Sincronização com Steam:** Login via Steam OpenID e busca automática da biblioteca do usuário.
- **Dashboard de Progresso:** Visualização clara de quais jogos estão em progresso e quais foram completados.
- **Guias Detalhados:** Página específica para cada troféu com:
    - Descrição oficial.
    - Dificuldade estimada.
    - Links para vídeos do YouTube/guias da comunidade.
- **Filtros Inteligentes:** Filtrar conquistas por "Bloqueadas", "Desbloqueadas" ou "Ocultas".

## 🗺️ Roadmap

Este projeto está sendo desenvolvido em etapas. Abaixo, o status atual e os próximos passos:

### Fase 1: Backend e Integração (Core) ⚙️
- [ ] Configuração do servidor e ambiente de desenvolvimento.
- [ ] Implementação da autenticação via **Steam OpenID**.
- [ ] Consumo da **Steam Web API** para recuperar:
    - [ ] Lista de jogos do usuário (OwnedGames).
    - [ ] Schema do jogo e lista de conquistas.
    - [ ] Status de progresso do jogador (Global stats).
- [ ] Modelagem e integração com Banco de Dados (Salvar notas/dicas personalizadas).

### Fase 2: Interface (Frontend) 🎨
- [ ] Prototipação.
- [ ] Criação da **Home/Dashboard**: Cards com os jogos e barras de progresso.
- [ ] Criação da **Página do Jogo**: Lista filtrável de troféus.
- [ ] Criação do **Modal/Página de Detalhes**: Exibição de vídeos e textos de ajuda.
- [ ] Implementação de Responsividade.

### Fase 3: Conteúdo e Otimização 🚀
- [ ] Sistema de "Crowdsourcing" (permitir que usuários adicionem dicas).
- [ ] Cacheamento de dados para reduzir chamadas à API da Steam.
- [ ] Polimento de UI/UX e animações.
- [x] Documentação completa (README v1.0).

---

## 💻 Tecnologias Utilizadas

*(Preencha/altere conforme sua stack real)*

- **Front-end:** 
- **Back-end:** Python
- **Bibliotecas:** Tkinter
- **Banco de Dados:** 
- **API:** Steam Web API

## 🚀 Sobre mim

Meu nome é **Jhonathan**, sou um estudante brasileiro de tecnologia de 20 anos. Meu foco é desenvolver soluções úteis para a comunidade gamer enquanto aprimoro minhas habilidades em desenvolvimento Full Stack.

## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jhonathan-ferroni/)
