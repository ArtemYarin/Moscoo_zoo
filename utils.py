import telebot
from telebot import types
from stuff import *


class Question:
    # Each question has an answers dictionary - answer: animal
    def __init__(self, question: str, answers: dict):
        self.question = question
        self.answers = answers


def show_question(bot, message: telebot.types.Message, question_num: int):
    # Shows question menu
    markup = types.InlineKeyboardMarkup(row_width=1)

    ans = []
    for i in questions[question_num].answers.keys():
        ans.append(types.InlineKeyboardButton(i, callback_data=i))

    markup.add(*ans)
    bot.send_message(message.chat.id, questions[question_num].question, reply_markup=markup)


def manage_answer(callback, question_num: int, animals):
    # Processes the answer and returns dictionary with animals´ points
    if callback.message:
        for i in questions[question_num].answers[callback.data]:
            animals[i] += 1
    return animals


def check_an_answer(callback, question_num: int, working):
    # Checking if the input is correct
    if working:
        return callback.data in questions[question_num].answers.keys()


def restart():
    # Returns empty animals dictionary
    data = {}
    for i in animals_list:
        data[i] = 0
    return data


def result(animals):
    # returns an animal with the highest number of points
    big = ''
    for i in animals.keys():
        if not big:
            big = i
        elif animals[big] < animals[i]:
            big = i
    return big


def show_results(bot, message, animals):
    # Output totem animal, image, zoo link, feedback gmail and try again command
    totem_animal = result(animals)
    bot.send_message(message.chat.id, f"Твоё тотемное животное в Московском зоопарке – {totem_animal}\n\
{animals_info[totem_animal]}")

    path = f'Zoo_fotos/{totem_animal}.jpg'
    with open(path, 'rb') as img:
        bot.send_photo(message.chat.id, img)

    bot.send_message(message.chat.id, "\nЕсли хотите узнать подробнее: https://moscowzoo.ru/about/guardianship\n\
Оставить отзыв: exampleMail@gmail.com\n\
Попробовать ещё раз /quiz")


question_one = Question(text_1, ans_1)
question_two = Question(text_2, ans_2)
question_three = Question(text_3, ans_3)
question_four = Question(text_4, ans_4)

questions = [question_one, question_two, question_three, question_four]
