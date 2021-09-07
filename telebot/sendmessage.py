import requests
from .models import TeleSettings

# token = '1991124690:AAENy2gDNu9gSGWEsrDePyl2TI7bpPoyKe4'
# chat_id = '-510990311'
# text = "Моё тестовое сообщение"

def sendTelegram():
    settings = TeleSettings.objects.get(pk=1)
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = str(settings.tg_message)
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method, data={
       'chat_id': chat_id,
        'text': text
    })

