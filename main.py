import os
import time
from telebot import TeleBot
from dotenv import load_dotenv, find_dotenv
from pars import get_search_results
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import json

load_dotenv(find_dotenv())

bot = TeleBot(os.getenv("TOKEN"))

@bot.message_handler(func=lambda message: True)
def handle_message(message, page=1):
    search_term = message.text
    search_results = get_search_results(search_term)
    print(search_results)
    markup = InlineKeyboardMarkup()

    button_data = f'load_more|{page + 1}|{search_term}'
    button = InlineKeyboardButton("Load More", callback_data=button_data)
    markup.add(button)

    if search_results and len(search_results) > page - 1 and search_results[page - 1]:
        bot.send_message(message.chat.id, search_results[page - 1], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Not Found... Please adjust your query and try again")
        

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    decoded_data = call.data.split('|')

    action = decoded_data[0]
    page = int(decoded_data[1])
    search_term = decoded_data[2]

    if action == "load_more":
        original_message = bot.send_message(call.message.chat.id, "Loading...")
        original_message.text = search_term
        handle_message(original_message, page=page)

if __name__ == "__main__":
    bot.infinity_polling()
