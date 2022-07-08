from turtle import update
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler


bot = Bot(token= '5599679578:AAEhvBVvBmPU6KWu1kX080WmRnIxmRI7AH4')
updater = Updater(token='5599679578:AAEhvBVvBmPU6KWu1kX080WmRnIxmRI7AH4', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет")
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")


def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Меня создала компания GB!")


def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'И тебе привет..')
    else:
        context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Шо сказал, не пойму')


start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
message_handler = MessageHandler(Filters.text, message)
unknown_handler = MessageHandler(Filters.command, unknown) #/game


dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)

print('server started')
updater.start_polling()
updater.idle()