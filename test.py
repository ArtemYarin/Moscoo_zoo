import telebot
from telebot import types
from stuff import *


class Questions:
    def __init__(self, questions: list):
        self.questions = questions


class Question:
    def __init__(self, question: str, answers: dict):
        self.question = question
        self.answers = answers


def show_question(bot, message: telebot.types.Message, question_num: int):
    markup = types.InlineKeyboardMarkup(row_width=1)

    ans = []
    for i in all_quiz.questions[question_num].answers.keys():
        ans.append(types.InlineKeyboardButton(i, callback_data=i))

    markup.add(*ans)
    bot.send_message(message.chat.id, all_quiz.questions[question_num].question, reply_markup=markup)


def manage_answer(callback, question_num: int, animals):
    if callback.message:
        for i in all_quiz.questions[question_num].answers[callback.data]:
            animals[i] += 1
    return animals


def check_an_answer(callback, question_num: int):
    return callback.data in all_quiz.questions[question_num].answers.keys()


def restart():
    data = {}
    for i in animals_list:
        data[i] = 0
    return data


def result(animals):
    big = ''
    for i in animals.keys():
        if not big:
            big = i
        elif animals[big] < animals[i]:
            big = i
    return big


def show_results(bot, message, animals):
    totem_animal = result(animals)
    bot.send_message(message.chat.id, f"Твоё тотемное животное в Московском зоопарке – {totem_animal}\n\
{animals_info[totem_animal]}")

    bot.send_message(message.chat.id, "\nЕсли хотите узнать подробнее: https://moscowzoo.ru/about/guardianship\n\
Оставить отзыв: exampleMail@gmail.com\n\
Попробовать ещё раз /quiz")


question_one = Question(text_1, ans_1)
question_two = Question(text_2, ans_2)
question_three = Question(text_3, ans_3)
question_four = Question(text_4, ans_4)

all_quiz = Questions([question_one, question_two, question_three, question_four])

