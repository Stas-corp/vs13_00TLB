import botinit

import telebot as tlb

bot = botinit.bot

@bot.message_handler(commands=['hellow'])
def reaction_comand_hellow(mess:tlb.types.Message):
    message = f'Hellow, dear {mess.from_user.username}'
    bot.send_message(mess.from_user.id, message)

@bot.message_handler(commands=['reset'])
def reaction_comand_reset(mess:tlb.types.Message):
    message = 'Перезапускаю бот!'
    bot.send_message(mess.from_user.id, mess)

@bot.message_handler(content_types=['photo'])
def reaction_photo(mess:tlb.types.Message):
    bot.send_message(mess.from_user.id, mess)

@bot.message_handler(content_types=['document'])
def reaction_photo(mess:tlb.types.Message):
    bot.send_message(mess.from_user.id, mess)

@bot.message_handler(content_types=['text'])
def reaction_photo(mess:tlb.types.Message):
    if mess.text == '💩':
        message = 'Сам такой!!!'
        bot.send_message(mess.from_user.id, message)
    else:
        bot.send_message(mess.from_user.id, mess.text)

if __name__ == '__main__':
    bot.polling(non_stop=True)
