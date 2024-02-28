import requests
from telegram import Bot


def get_chat_id(bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['result'] :
            chat_id = data['result'][0]['message']['chat']['id']
            return chat_id
        else:
            print('No update found')
    else:
        print(f'{response.status_code}')

async def send_message(bot_token, chat_id, text):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=text)


chat_id = get_chat_id('6966526344:AAFZSxgE7uNvMcP1HIvsysB9yp5cXSTBNEw')

async def main(text):
    await send_message('6966526344:AAFZSxgE7uNvMcP1HIvsysB9yp5cXSTBNEw', chat_id, text)




'6966526344:AAFZSxgE7uNvMcP1HIvsysB9yp5cXSTBNEw'