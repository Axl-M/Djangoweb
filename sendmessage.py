import requests

token = '1991124690:AAENy2gDNu9gSGWEsrDePyl2TI7bpPoyKe4'
chat_id = '-510990311'
text = "Моё тестовое сообщение"

def sendTelegram():
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method, data={
       'chat_id': chat_id,
        'text': text
    })

sendTelegram()