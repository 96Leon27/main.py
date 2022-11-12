import telebot
import config
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('images/hi_sticker.jfif', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.reply_to(message, "Привет, {0.first_name}!\n<b>Я - {1.first_name}</b>".format(message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
