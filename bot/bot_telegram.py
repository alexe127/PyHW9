from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from mod import *
# from controller_telegram import *

bot = Bot(token= '  ')
updater = Updater(token=' ', use_context=True)
dispatcher = updater.dispatcher




start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('4', cancel)
cancel_handler2 = CommandHandler('1', plan)


plan_handler = MessageHandler(Filters.text, plan)
# plan_handler2 = MessageHandler(Filters.command, plan)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(cancel_handler2)
dispatcher.add_handler(cancel_handler)
dispatcher.add_handler(plan_handler)
# dispatcher.add_handler(plan_handler2)


print('бот запущен')
updater.start_polling()
updater.idle()