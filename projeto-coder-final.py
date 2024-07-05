# Passo 1:
# Instalação de Bibliotecas necessárias para rodas os códigos:
#%pip install pandas #limpeza e manipulação 
#%pip install numpy #computação numérica
#%pip install plyer #envio da notificação
#%pip install datetime #data
#%pip install requests #interação com APIs

#Passo 2
#Importar as bibliotecas:
import pandas as pd
import numpy as np
import sqlite3
from plyer import notification #função de notificação
from datetime import datetime


notification.notify(
    title='Mensagem de erro:',
    message= 'Algo de errado não está certo',
    app_name='Python',
    timeout=10)

#Criação de Alerta em caso de erro
def alerta (nivel, base, etapa):
    now = str(datetime.now())
    
    msg = f"Falha no carregamento da base {base} na etapa {etapa}.\n{now}"

    if nivel == 1:
        title = 'ATENÇÃO: Alerta Baixo'
    elif nivel == 2:
        title = 'ATENÇÃO: Alerta Médio'
    elif nivel == 3:
        title = 'ATENÇÃO: Alerta Alto'
    else:
        print("Nivel", nivel, "não disponível!")

    notification.notify(
        title=title,
        message=msg,
        app_name='alerta',
        timeout=10
    )
alerta(nivel = 2,
        base = "TOP_BR_Spotify", 
        etapa = "PASSAGEM DO SAP")