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

    button_data = json.dumps({"action": "load_more", "page": page + 1, "search_term": search_term})
    button = InlineKeyboardButton("Load More", callback_data=button_data)
    markup.add(button)

    if search_results and len(search_results) > page - 1 and search_results[page - 1]:
        time.sleep(2)
        bot.send_message(message.chat.id, search_results[page - 1], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Not Found... Please adjust your query and try again")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    decoded_data = json.loads(call.data)

    action = decoded_data.get("action", "default_action") 
    page = decoded_data.get("page", 1)
    search_term = decoded_data.get("search_term", "")

    if action == "load_more":
        original_message = bot.send_message(call.message.chat.id, "Loading...")
        original_message.text = search_term
        handle_message(original_message, page=page)
if __name__ == "__main__":
    bot.infinity_polling()













































# from telebot import types
# import telebot
# import os
# from dotenv import load_dotenv, find_dotenv
# # from pars import search_term

# load_dotenv(find_dotenv())

# botTimeWeb = telebot.TeleBot(os.getenv("TOKEN"))
# @botTimeWeb.message_handler(commands=['start'])
# def startBot(message):
#     first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nХочешь найти фильм?"
#     markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     button_yes = telebot.types.KeyboardButton(text='Да')
#     button_no = telebot.types.KeyboardButton(text='Нет')

#     markup.add(button_yes, button_no)
#     botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

# @botTimeWeb.message_handler(func=lambda message: True)
# def response(message):
#     if message.text == "Да":
#         second_mess = "Веди что хочешь найти!"
#         markup = types.InlineKeyboardMarkup()
#         markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://animego.org/"))
#         botTimeWeb.send_message(message.chat.id, second_mess, reply_markup=markup)
#         botTimeWeb.answer_callback_query(message.id)
        
#         botTimeWeb.send_message(message.chat.id, second_mess)
#     elif message.text == "Нет":
#         second_mess = "До следующей встречи"
#         botTimeWeb.send_message(message.chat.id, second_mess)

# botTimeWeb.infinity_polling()
