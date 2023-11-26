import botinit
import photograph

import telebot as tlb

bot = botinit.bot
pho = photograph.Photgraph()

@bot.message_handler(commands=['start'])
def reaction_comand_start(mess:tlb.types.Message):
    message = f'Start BOT!'
    bot.send_message(mess.from_user.id, message, reply_markup=botinit.markup)

@bot.message_handler(commands=['hellow'])
def reaction_comand_hellow(mess:tlb.types.Message):
    message = f'Hellow, dear {mess.from_user.username}'
    bot.send_message(mess.from_user.id, message)

@bot.message_handler(commands=['getpho'])
def reaction_comand_hellow(mess:tlb.types.Message):
    photos = pho.get_photos_list(str(mess.from_user.id))
    bot.send_message(mess.from_user.id, photos)

@bot.message_handler(content_types=['photo'])
def reaction_photo(mess:tlb.types.Message):
    photos = mess.photo
    pho.main(photos=photos, user_id=str(mess.from_user.id))
    # bot.send_message(mess.from_user.id, mess)

@bot.message_handler(content_types=['text'])
def reaction_text(mess:tlb.types.Message):
    if mess.text == '💩':
        markup = tlb.types.InlineKeyboardMarkup()
        btn = tlb.types.InlineKeyboardButton('или хочешь поспорить?', callback_data='qwe')
        markup.add(btn)
        message = 'Сам такой!!!'
        bot.send_message(mess.from_user.id, message, reply_markup=markup)
    else:
        bot.send_message(mess.from_user.id, mess.text)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call:tlb.types.CallbackQuery):
    if call.data == 'qwe':
        bot.send_message(call.message.chat.id, 'Нет смысла, это же ты отправил этот смайлик')

    bot.answer_callback_query(call.id)

if __name__ == '__main__':
    bot.polling(non_stop=True)

'''
def json_writer_mess(func):
    def wraper(mess:tlb.types.Message):
        atr = vars(mess)
        with open (f'Mess ID_{mess.message_id}.json', 'w', encoding='utf-8') as file:
            print(atr)
            json.dump(atr, file)
        return func(mess)
    return wraper

@bot.message_handler(content_types=['document'])
def reaction_photo(mess:tlb.types.Message):
    bot.send_message(mess.from_user.id, mess)

@bot.message_handler(commands=['reset'])
def reaction_comand_reset(mess:tlb.types.Message):
    message = 'Перезапускаю бот!'
    bot.send_message(mess.from_user.id, mess)
'''