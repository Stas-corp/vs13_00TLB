import __token__
import telebot as tlb

# print(__token__.TOKEN)

bot = tlb.TeleBot(__token__.TOKEN)

bot.set_my_commands(commands=[
    tlb.types.BotCommand('hellow', 'Команда привеветствия'),
    tlb.types.BotCommand('reset', 'Перезапуск бота'),

])