import requests

from celery import shared_task
from django.conf import settings


class TelegramBot:
    pass


@shared_task
def send_reminder(telegram_id, text):
    bot_data = requests.get(f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/getUpdates').json()
    chat_id = None
    for b in bot_data['result']:
        if b['message']['chat']['username'] == telegram_id:
            chat_id = b['message']['chat']['id']
        else:
            return ValueError(f'Пользователь https://t.me/{telegram_id} не активировал бот')
    response = requests.post(f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/sendMessage',
                             data={'chat_id': chat_id, 'text': text})
    return response.json()
