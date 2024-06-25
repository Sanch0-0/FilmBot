from telebot import TeleBot
import requests
import os
from dotenv import load_dotenv

load_dotenv()

bot=TeleBot(token=os.getenv("TOKEN"))
api_key=os.getenv("API_KEY")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привет , Введите название фильма чтобы получить информацию о нем")


@bot.message_handler(func= lambda message : True)
def search_movie(message):
    movie_title=message.text
    url= f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"

    responce= requests.get(url)

    data=responce.json()
    try:
        if data:
            reply=(
                f"Название : {data['Title']}\n"
                f"Год : {data['Year']}\n"
                f"Рейтинг : {data['Rated']}\n"
                f"Дата выхода : {data['Released']}\n "
                f"Длительность : {data['Runtime']}\n"
                f"Жанр : {data['Genre']}\n"
                f"Режиссер : {data['Director']}\n"
                f"Актеры : {data['Actors']}\n"
                f"Сюжет : {data['Plot']}\n"
                f"Язык : {data['Language']}"
                f"Cтрана : {data['Country']}\n"
                f"Награды : {data['Awards']}\n"
                f"Рейтинг  IMDb: {data['imdbRating']}\n"
                f"Постер : {data['Poster']}\n"

            )
    except KeyError :
            reply="Извините  фильм не найден . Попробуйте еще раз"
    bot.reply_to(message,reply)




