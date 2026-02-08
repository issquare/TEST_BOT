import os # встроенная библиотека Python для работы с операционной системой
from dotenv import load_dotenv # библиотека для загрузки переменных окружения из файла .env
import telebot # библиотека pyTelegramBotAPI для работы с Telegram Bot API

load_dotenv() # загружает переменные из файла .env в окружение
TOKEN = os.getenv('TOKEN') # получает значение переменной TOKEN из окружения

bot = telebot.TeleBot(TOKEN) # создается объект бота с использованием полученного токена

@bot.message_handler(commands=['start']) # декоратор - это функция, которая принимает другую функцию и изменяет/расширяет её поведение. Бот внутренне сохраняет связь: "если придет команда /start → вызвать функцию start()"
def start(message): # message - параметр функции. При вызове функции бот автоматически передает сюда объект сообщения.
    print("start")
    bot.reply_to(message, f"Привет, {message.from_user.username}!") # reply_to() - отправляет сообщение как ответ на конкретное сообщение
    bot.send_message(message.chat.id, "Я здесь и я работаю.") # bot.send_message() - метод объекта бота для отправки сообщения

bot.infinity_polling() # бесконечный цикл работы бота