# Python Alerta Notificação

Este é um projeto simples em Python que utiliza a biblioteca plyer para exibir alertas de notificação.

## Como Usar

1. Instale as dependências:

   ```bash
   pip install plyer
   pip install datetime


## Dependências

- Python 3.x
- Plyer
- datetime


## Exemplos

```python
from plyer import notification
import time

def criar_alerta(titulo, mensagem):
    notification.notify(
        title=titulo,
        message=mensagem,
        app_icon=None,
        timeout=10,
    )

# Exemplo de uso
titulo = "Alerta Importante"
mensagem = "Isso é uma mensagem de teste."

# Crie o alerta
criar_alerta(titulo, mensagem)

# Aguarde um pouco antes de encerrar o programa
time.sleep(15)


## Contribuição

Se você quiser contribuir para este projeto, por favor, abra uma issue ou envie um pull request.
