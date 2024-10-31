from utils import *
from stuff import *


bot = telebot.TeleBot(TOKEN)
animals = {}
question_num = 0
working = False  # Quiz is working or not


@bot.message_handler(commands=['start', 'help'])
def instruction(message: telebot.types.Message):
    # User´s instruction how to start
    text = 'Добро пожаловать на тест на тотемное животное.\n\
Чтобы начать введите /quiz'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['quiz'])
def start_quiz(message: telebot.types.Message):
    global animals, question_num, working
    # Restarts the bot
    working = True
    animals = restart()
    question_num = 0

    # Start program/first question
    show_question(bot, message, question_num)


@bot.callback_query_handler(func=lambda call: True)
def answer(callback):
    global animals, question_num, working
    # Shows questions till the end
    if check_an_answer(callback, question_num, working):
        animals = manage_answer(callback, question_num, animals)
        question_num += 1

        if question_num == len(questions):
            show_results(bot, callback.message, animals)
            working = False
        else:
            show_question(bot, callback.message, question_num)


bot.polling(none_stop=True)
