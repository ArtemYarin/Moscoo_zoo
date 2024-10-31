import telebot
from stuff import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['example'])
def image(message: telebot.types.Message):
    with open('Zoo_fotos/КИТАЙСКИЙ АЛЛИГАТОР.jpg', 'rb') as img:
        bot.send_photo(message.chat.id, img)


bot.polling(none_stop=True)
