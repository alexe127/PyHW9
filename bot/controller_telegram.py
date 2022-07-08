

from email import message
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


def plan(update, context):
    work = True
    while work:
        try:
            task = update.message.text
            # task = start(update, context)  # так зацикливается      
            
            if task == '1':
                user_input = update.message.text
                # print(user_input)
                
                context.bot.send_message(update.effective_chat.id,"Введите задачу в формате (Дата задача примечание): ")
                # user_input = str(input("Введите задачу в формате (Дата задача примечание): "))
                # user_input = update.message.text
                # print(user_input)
                build_planned(user_input)                
                # print("Запись добавлена!")
                # continue
                return
            elif task == '2':
                var_choice = plann_or_compl()    
                if var_choice == "c":
                    context.bot.send_message(update.effective_chat.id,"Введите задачу которую выполнили(в конце пробел): ")
                    
                    # user_input = str(input("Введите задачу которую выполнили(в конце пробел): "))
                    build_compl(user_input)
                    print("Задача выполнена!")
                    
                elif var_choice == "d":
                    context.bot.send_message(update.effective_chat.id,"Введите задачу которую удаляем(в конце пробел): ")
                    # user_input = str(input("Введите задачу которую удаляем(в конце пробел): "))
                    
                    build_del(user_input)
                    print("Задача удалена!")

            elif task == '3':
                    print_file()
                    continue
                
            elif task != '1' or task != '2' or task != '3' or task != '4':
                context.bot.send_message(update.effective_chat.id,"Введен не правильный запрос")
                # print("Введен не правильный запрос!")
                message = 'Введен не правильный запрос!' 
                add_in_log(f'{message}') 
                # continue             
                return
        except ValueError:
            context.bot.send_message(update.effective_chat.id,"Введен не корректный запрос!")
            # print("Введен не корректный запрос!")  
            mes = 'Введен не корректный запрос!' 
            add_in_log(f'{mes}')           
    else:
        context.bot.send_message(update.effective_chat.id,"Всего доброго!")
        mes = 'выход'
        add_in_log(f'{mes}')
        
#

def plann_or_compl():
    user_choice = str(input("Отметить задачу выполненной - c   Удалить задачу - d :" ))
    return user_choice

