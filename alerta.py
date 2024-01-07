# pip install plyer
# use o comando informado na linha superior para instalar a biblioteca "plyer" para executar esse código e funcionar o alerta

from plyer import notification
import time

def criar_alerta(titulo, mensagem):
    notification.notify(
        title=titulo,
        message=mensagem,
        app_icon=None,  # Aqui você pode adicionar um ícone personalizado se desejar
        timeout=10,  # Aqui pode configurar por qto tempo vai durar o alerta
    )

# Exemplo de uso
titulo = "Aula Python"
mensagem = "Para de jogar e vai estudar, sua aula de python vai começar!!!"

# Crie o alerta
criar_alerta(titulo, mensagem)

# Aqui vc pode configurar pra encerrar o programa
time.sleep(15)