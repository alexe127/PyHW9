

# from email import message
from process_file import print_file
from process_data import build_compl
from process_data import build_planned
from process_data import build_del
from logger import add_in_log

def project():
    work = True
    while work:
        try:
            task = request()
            if task == 4:
                work = False
            elif task == 1:
                user_input = str(input("Введите задачу в формате (Дата задача примечание): "))
                build_planned(user_input)
                print("Запись добавлена!")
                continue
            elif task == 2:
                var_choice = plann_or_compl()    
                if var_choice == "c":
                    user_input = str(input("Введите задачу которую выполнили(в конце пробел): "))
                    build_compl(user_input)
                    print("Задача выполнена!")
                    
                elif var_choice == "d":
                    user_input = str(input("Введите задачу которую удаляем(в конце пробел): "))
                    build_del(user_input)
                    print("Задача удалена!")

            elif task == 3:
                    print_file()
                    continue
                
            elif task < 1 or task > 4:
                print("Введен не правильный запрос!")
                message = 'Введен не правильный запрос!' 
                add_in_log(f'{message}')              
                continue
        except ValueError:
            print("Введен не корректный запрос!")  
            message = 'Введен не корректный запрос!' 
            add_in_log(f'{message}')           
    else:
        print("Всего доброго!")
        message = 'выход'
        add_in_log(f'{message}')
def request():
    print("Планируем дела")
    user_request = int(input("Добавить новую задачу - 1   Редактировать задачу - 2   Просмотр дел -3   Выход - 4 :"))

    return user_request

def plann_or_compl():
    user_choice = str(input("Отметить задачу выполненной - c   Удалить задачу - d :" ))
    return user_choice

