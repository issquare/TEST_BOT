import os
from dotenv import load_dotenv
import telebot
from kinopoisk.movie import Movie

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def find_movie(message):
    movie_list = Movie.objects.search(message.text) # message.text - текст сообщения от пользователя
    result = ''
    for movie in movie_list:
        result = result + str(movie) + '\n'
    bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['start'])
def start(message):
    print("start")
    bot.reply_to(message, f"Привет, {message.from_user.username}!")
    bot.send_message(message.chat.id, "Я здесь и я работаю.")

bot.infinity_polling()