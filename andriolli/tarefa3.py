import psutil
from datetime import datetime

def mostrar_usuarios():
    usuarios = psutil.users()

    if not usuarios:
        print("Nenhum usuário conectado no momento.")
        return

    for usuario in usuarios:
        nome = usuario.name
        terminal = usuario.terminal or "desconhecido"
        host = usuario.host or "local"
        hora_login = datetime.fromtimestamp(usuario.started).strftime("%d/%m/%Y %H:%M:%S")
        print(f"Usuário: {nome} | Terminal: {terminal} | Host: {host} | Login em: {hora_login}")

mostrar_usuarios()
# INÍCIO
#   IMPORTAR biblioteca de monitoramento do sistema (psutil)
#   IMPORTAR biblioteca de data e hora (datetime)
#
#   FUNÇÃO mostrar_usuarios()
#      usuarios ← OBTER lista de usuários conectados
#
#      SE usuarios estiver vazio ENTÃO
#         ESCREVER "Nenhum usuário conectado"
#         RETORNAR
#      FIM SE
#
#      PARA CADA usuario EM usuarios FAÇA
#         nome ← nome do usuário
#         terminal ← terminal utilizado
#         host ← origem do acesso
#         hora_login ← FORMATAR data e hora de início da sessão
#         ESCREVER nome, terminal, host e hora_login
#      FIM PARA
#   FIM FUNÇÃO
#
#   CHAMAR mostrar_usuarios()
# FIM
#                 ┌───────────┐
#                 │   INÍCIO  │
#                 └─────┬─────┘
#                       │
#                       ▼
#           ┌────────────────────────┐
#           │ Importar psutil e       │
#           │ datetime                │
#           └───────────┬────────────┘
#                       │
#                       ▼
#           ┌────────────────────────┐
#           │ Obter lista de          │
#           │ usuários conectados     │
#           └───────────┬────────────┘
#                       │
#                       ▼
#                  ╱──────────╲
#                 ╱  Existem     ╲       Não
#                ╱  usuários?      ╲──────────────┐
#                 ╲                ╱              │
#                  ╲──────────────╱                │
#                       │ Sim                       ▼
#                       │                  ┌──────────────────────┐
#                       ▼                  │ Exibir mensagem:      │
#           ┌────────────────────────┐     │ "Nenhum usuário       │
#           │ Para cada usuário:      │     │  conectado"           │
#           │ obter nome, terminal,   │     └───────────┬───────────┘
#           │ host e hora de login    │                 │
#           └───────────┬────────────┘                 │
#                       │                                │
#                       ▼                                │
#           ┌────────────────────────┐                  │
#           │ Exibir dados do         │                  │
#           │ usuário na tela         │                  │
#           └───────────┬────────────┘                  │
#                       │                                │
#                       ▼                                │
#                       └──────────────┬─────────────────┘
#                                      ▼
#                                ┌───────────┐
#                                │    FIM    │
#                                └───────────┘