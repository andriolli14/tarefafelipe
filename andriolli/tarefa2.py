import psutil

def mostrar_temperatura():
    temperaturas = psutil.sensors_temperatures()

    if not temperaturas:
        print("Não foi possível obter a temperatura (sensor não disponível neste sistema).")
        return

    for nome_sensor, leituras in temperaturas.items():
        for leitura in leituras:
            print(f"{nome_sensor} ({leitura.label or 'geral'}): {leitura.current}°C")

mostrar_temperatura()
# INÍCIO
#   IMPORTAR biblioteca de monitoramento do sistema (psutil)
#
#   FUNÇÃO mostrar_temperatura()
#      temperaturas ← OBTER leituras de temperatura dos sensores
#      
#      SE temperaturas estiver vazio ENTÃO
#         ESCREVER "Temperatura não disponível"
#         RETORNAR
#      FIM SE
#
#      PARA CADA sensor EM temperaturas FAÇA
#         PARA CADA leitura DO sensor FAÇA
#            ESCREVER nome do sensor, rótulo e valor em °C
#         FIM PARA
#      FIM PARA
#   FIM FUNÇÃO
#
#   CHAMAR mostrar_temperatura()
# FIM
#                 ┌───────────┐
#                 │   INÍCIO  │
#                 └─────┬─────┘
#                       │
#                       ▼
#           ┌────────────────────────┐
#           │ Importar psutil         │
#           │ (biblioteca de          │
#           │ monitoramento)          │
#           └───────────┬────────────┘
#                       │
#                       ▼
#           ┌────────────────────────┐
#           │ Obter leituras de       │
#           │ temperatura dos         │
#           │ sensores                │
#           └───────────┬────────────┘
#                       │
#                       ▼
#                  ╱──────────╲
#                 ╱  Leituras   ╲        Não
#                ╱  disponíveis? ╲──────────────┐
#                 ╲              ╱              │
#                  ╲────────────╱                │
#                       │ Sim                     ▼
#                       │                ┌────────────────────┐
#                       ▼                │ Exibir mensagem:    │
#           ┌────────────────────────┐   │ "Temperatura não    │
#           │ Exibir cada leitura:    │   │  disponível"        │
#           │ sensor, rótulo e        │   └──────────┬──────────┘
#           │ valor em °C             │              │
#           └───────────┬────────────┘              │
#                       │                            │
#                       ▼                            │
#                       └─────────────┬──────────────┘
#                                     ▼
#                               ┌───────────┐
#                               │    FIM    │
#                               └───────────┘