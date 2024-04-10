# from telebot import types
# import telebot
# import os
# from dotenv import load_dotenv, find_dotenv


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

