# pip install plyer
# pip install datetime
# use o comando informado na linha superior para instalar a biblioteca "plyer" para executar esse código e funcionar o alerta

from plyer import notification
from datetime import datetime, time

def criar_alerta(nivel, base, etapa):


    if nivel == 1:
        titulo = "Alerta Baixo"
    elif nivel == 2:
        titulo = "Alerta Médio"
    elif nivel == 3:
        titulo = "Alerta Alto"
    else:
        titulo = "Alerta Desconhecido"


    notification.notify(
        title=titulo,
        message = f"Falha no carregamento da base {base} na etapa {etapa}\nData: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        app_icon=None,  # Aqui você pode adicionar um ícone personalizado se desejar
        timeout=10,  # Aqui pode configurar por qto tempo vai durar o alerta
    )

# Crie o alerta
criar_alerta(1, "leads", "dedup")

# Aqui vc pode configurar pra encerrar o programa
time.sleep(15)