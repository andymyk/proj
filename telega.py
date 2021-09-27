from telebot import TeleBot
from envparse import Env
import requests
CHAT_ID = 758419206


TOKEN = '1988620539:AAGTWZZVJHacA67KinzZ1Wdfl6bWQ7Ztidw'
bot = TeleBot(TOKEN)


def send_messages(text):
    requests.post(f'https://api.telegram.org/bot1988620539:AAGTWZZVJHacA67KinzZ1Wdfl6bWQ7Ztidw/sendMessage?chat_id={CHAT_ID}&text={text}')


while True:
    bot.polling()
    text = input('Enter: ')
    send_messages(text)