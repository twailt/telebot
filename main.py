import os
import time
from telebot import TeleBot
from dotenv import load_dotenv, find_dotenv
from pars_anime import get_search_results
from pars import get_search_results as film_search
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import json
import telebot
from telebot import types
import config

load_dotenv(find_dotenv())

bot = TeleBot(os.getenv("TOKEN"))

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button_data_1 = f'select_anime|_|_'
    button_data_2 = f'select_films|_|_'
    btn1 = types.InlineKeyboardButton("Amine❓", callback_data=button_data_1)
    btn2 = types.InlineKeyboardButton("Films❓", callback_data=button_data_2)
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Select category", reply_markup=markup)

# @bot.message_handler(func=lambda message: True)
# def handle_message(message, page=1):
#     search_term = message.text
#     print(search_term)
#     print(message)
    
#     search_results = get_search_results(search_term)
#     # print(search_results)
#     markup = InlineKeyboardMarkup()

#     button_data = f'load_more|{page + 1}|{search_term}'
#     button = InlineKeyboardButton("Load More", callback_data=button_data)
#     markup.add(button)

#     if search_results and len(search_results) > page - 1 and search_results[page - 1]:
#         bot.send_message(message.chat.id, search_results[page - 1], reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, "Not Found... Please adjust your query and try again")
        

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    decoded_data = call.data.split('|')

    action = decoded_data[0]

    if action == "load_more":
        page = int(decoded_data[1])
        search_term = decoded_data[2]
        category = decoded_data[3]

        original_message = bot.send_message(call.message.chat.id, "Loading...")
        original_message.text = search_term
        search(original_message, category, page=page)
    elif action == "select_anime":
        bot.clear_step_handler(call.message)
        bot.register_next_step_handler(call.message, search, "select_anime")
        bot.send_message(call.message.chat.id, "Write a name...")
    elif action == "select_films":
        bot.clear_step_handler(call.message)
        bot.register_next_step_handler(call.message, search, "select_films")
        bot.send_message(call.message.chat.id, "Write a name...")


def search(message, category, page=1):
    search_term = message.text
    if category == "select_anime":
        search_results = get_search_results(search_term)
    else:
        search_results = film_search(search_term)
    
    # print(search_results)
    markup = InlineKeyboardMarkup()

    button_data = f'load_more|{page + 1}|{search_term}|{category}'
    button = InlineKeyboardButton("Load More", callback_data=button_data)
    markup.add(button)

    bot.register_next_step_handler(message, search, category)
    if search_results and len(search_results) > page - 1 and search_results[page - 1]:
        bot.send_message(message.chat.id, search_results[page - 1], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Not Found... Please adjust your query and try again")
        

if __name__ == "__main__":
    bot.infinity_polling()
