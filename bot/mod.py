from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from process_file import print_file
from process_data import build_compl
from process_data import build_planned
from process_data import build_del
from logger import add_in_log

def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет, планируем дела") 
        context.bot.send_message(update.effective_chat.id, "Добавить новую задачу - 1 Редактировать задачу - 2  Просмотр  дел -3 Выход - /4 :")
        # context.bot.send_message(update.effective_chat.id, "Добавить новую задачу - /1 Редактировать задачу - /2  Просмотр  дел -/3 Выход - /4 :")           
    
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")


def cancel(update, context): 
    text = update.message.text   
    context.bot.send_message(update.effective_chat.id, 
    "Выход произведён, если передумаете: запустите командой /start")
    print(text)
    add_in_log(f'нажата команда выход')

# def message(update, context):
#      context.bot.send_message(update.effective_chat.id, "Добавить новую задачу - /1 Редактировать задачу - 2  Просмотр  дел -3 Выход - /4 :")
     

def plan(update, context):
    # arg = context.args
    text = update.message.text
    print(text)
    build_planned(text)
    if text == '1':
        context.bot.send_message(update.effective_chat.id, 'Введите задачу в формате (Дата задача примечание): ')
        # text2 = update.message.text
        # print(text2)
        # build_planned(text2)
           
            
    elif text == '2':
        var_choice = plann_or_compl(update, context)
        if var_choice == "c":
            user_input = context.bot.send_message(update.effective_chat.id,"Введите задачу которую выполнили(в конце пробел): ")
            # user_input = str(input("Введите задачу которую выполнили(в конце пробел): "))
            build_compl(user_input)
            # print("Задача выполнена!")
                    
        elif var_choice == "d":
            user_input = context.bot.send_message(update.effective_chat.id,"Введите задачу которую удаляем(в конце пробел): ")
            # user_input = str(input("Введите задачу которую удаляем(в конце пробел): "))
            build_del(user_input)
            # print("Задача удалена!")

        # context.bot.send_message(update.effective_chat.id, 'Отметить задачу выполненной - c   Удалить задачу - d :')
        # build_planned(text)
        # context.bot.send_message(update.effective_chat.id, "Запись добавлена")
    
        

    
def plann_or_compl(update, context):
    user_choice = context.bot.send_message(update.effective_chat.id, 'Отметить задачу выполненной - c   Удалить задачу - d :')
    # user_choice = str(input("Отметить задачу выполненной - c   Удалить задачу - d :" ))
    return user_choice