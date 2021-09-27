from telebot import TeleBot


TOKEN = '1988620539:AAGTWZZVJHacA67KinzZ1Wdfl6bWQ7Ztidw'
bot = TeleBot(TOKEN)

def send_message():
    bot.send_message(758419206,'Ваша заявка успешно создана!')

def closed():
    bot.send_message(758419206,'Ваша заявка закрыта!')


