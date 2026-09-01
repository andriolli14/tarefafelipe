import datetime

def mostrar_hora():
    agora = datetime.datetime.now()
    hora_formatada = agora.strftime("%H:%M:%S")
    print("A hora atual do computador é:", hora_formatada)

mostrar_hora()
#iNÍCIO
#  IMPORTAR módulo de data/hora

 # FUNÇÃO mostrar_hora()
  #   agora ← OBTER data e hora atual do sistema
  #   hora_formatada ← FORMATAR agora como "HH:MM:SS"
  #   ESCREVER "A hora atual do computador é:", hora_formatada
 # FIM FUNÇÃO

 # CHAMAR mostrar_hora()
#FIM
#                 ┌───────────┐
#                 │   INÍCIO  │
#                 └─────┬─────┘
#                       │
#                       ▼
#           ┌────────────────────────┐
#           │ Importar módulo        │
#           │ datetime                │
#           └───────────┬────────────┘
#                       │
#                       ▼
#           ┌────────────────────────┐
#           │ Obter data e hora      │
#           │ atual do sistema       │
#           └───────────┬────────────┘
#                       │
#                       ▼
#           ┌────────────────────────┐
#           │ Formatar hora no       │
#           │ padrão HH:MM:SS        │
#           └───────────┬────────────┘
#                       │
#                       ▼
#           ┌────────────────────────┐
#           │ Exibir a hora          │
#           │ na tela                │
#           └───────────┬────────────┘
#                       │
#                       ▼
#                 ┌───────────┐
#                 │    FIM    │
#                 └───────────┘