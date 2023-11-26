import __token__
import telebot as tlb

# print(__token__.TOKEN)

bot = tlb.TeleBot(__token__.TOKEN)

bot.set_my_commands(commands=[
    tlb.types.BotCommand('start', 'Старт работы бота'),
    tlb.types.BotCommand('hellow', 'Команда привеветствия'),
    tlb.types.BotCommand('getpho', 'Список фото пользователя'),
])

markup = tlb.types.ReplyKeyboardMarkup(resize_keyboard=True)
butn1 = tlb.types.KeyboardButton('💩')
markup.add(butn1)

# tlb.types.ReplyKeyboardMarkup
# tlb.types.InlineKeyboardMarkup