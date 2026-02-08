import os
from dotenv import load_dotenv
import telebot

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: "доброе утро" in message.text.lower())
def morning(message):
    bot.reply_to(message, "Всем доброе утро! ☕️\nИлья ещё спит или чем-то занят, поэтому я отвечаю за него в качестве личного ассистента))\nПожелание доброго утра - это пока все, что я умею. Но это только пока...")

bot.infinity_polling()