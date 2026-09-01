def mostrar_log_acesso(caminho_arquivo="/var/log/auth.log"):
    try:
        with open(caminho_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo de log não encontrado.")
        return
    except PermissionError:
        print("Sem permissão para ler o arquivo de log.")
        return

    palavras_chave = ["login", "session opened", "accepted", "failed password"]
    linhas_encontradas = [linha for linha in linhas if any(p in linha.lower() for p in palavras_chave)]

    if not linhas_encontradas:
        print("Nenhum registro de acesso encontrado.")
        return

    for linha in linhas_encontradas:
        print(linha.strip())

mostrar_log_acesso()
# INÍCIO
#   DEFINIR caminho_arquivo ← "/var/log/auth.log"
#
#   FUNÇÃO mostrar_log_acesso(caminho_arquivo)
#      TENTAR
#         linhas ← LER todas as linhas do arquivo de log
#      SE arquivo não encontrado ENTÃO
#         ESCREVER "Arquivo de log não encontrado"
#         RETORNAR
#      FIM SE
#      SE sem permissão de leitura ENTÃO
#         ESCREVER "Sem permissão para ler o arquivo de log"
#         RETORNAR
#      FIM SE
#
#      palavras_chave ← ["login", "session opened", "accepted", "failed password"]
#      linhas_encontradas ← FILTRAR linhas que contêm alguma palavra_chave
#
#      SE linhas_encontradas estiver vazio ENTÃO
#         ESCREVER "Nenhum registro de acesso encontrado"
#         RETORNAR
#      FIM SE
#
#      PARA CADA linha EM linhas_encontradas FAÇA
#         ESCREVER linha
#      FIM PARA
#   FIM FUNÇÃO
#
#   CHAMAR mostrar_log_acesso(caminho_arquivo)
# FIM
#                 ┌───────────┐
#                 │   INÍCIO  │
#                 └─────┬─────┘
#                       │
#                       ▼
#           ┌────────────────────────┐
#           │ Definir caminho do      │
#           │ arquivo de log          │
#           └───────────┬────────────┘
#                       │
#                       ▼
#           ┌────────────────────────┐
#           │ Tentar abrir e ler o    │
#           │ arquivo de log          │
#           └───────────┬────────────┘
#                       │
#                       ▼
#                  ╱──────────╲
#                 ╱  Arquivo     ╲      Não
#                ╱  encontrado e   ╲─────────────┐
#                ╲  acessível?     ╱              │
#                 ╲──────────────╱                │
#                       │ Sim                      ▼
#                       │                 ┌───────────────────────┐
#                       ▼                 │ Exibir mensagem de     │
#           ┌────────────────────────┐    │ erro (não encontrado   │
#           │ Filtrar linhas com      │    │ ou sem permissão)      │
#           │ palavras-chave de       │    └────────────┬───────────┘
#           │ acesso (login, etc.)    │                 │
#           └───────────┬────────────┘                 │
#                       │                                │
#                       ▼                                │
#                  ╱──────────╲                          │
#                 ╱  Existem     ╲     Não                │
#                ╱  registros?    ╲─────────────┐         │
#                ╲                ╱              │         │
#                 ╲──────────────╱                │         │
#                       │ Sim                       ▼         │
#                       │                 ┌───────────────────┐│
#                       ▼                 │ Exibir mensagem:   ││
#           ┌────────────────────────┐    │ "Nenhum registro   ││
#           │ Exibir cada linha de    │    │  encontrado"       ││
#           │ log encontrada          │    └──────────┬─────────┘│
#           └───────────┬────────────┘                │          │
#                       │                              │          │
#                       ▼                              │          │
#                       └──────────────┬───────────────┘          │
#                                      │                           │
#                                      └─────────────┬─────────────┘
#                                                    ▼
#                                              ┌───────────┐
#                                              │    FIM    │
#                                              └───────────┘