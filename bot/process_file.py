

def print_file():
    with open('planned_task.csv', "r") as file:
        print(file.read())

def print_compl_file():
    with open('planned_task.csv', "r") as file:
        print(file.read())

def del_record(string):
    with open('planned_task.csv', "r") as file:
        lines = file.readlines()
    with open('planned_task.csv', 'w') as new_file:
        for line in lines:
            if line != (string+"\n"):
                new_file.write(line)

def writer_compl(string):
    with open('planned_task.csv', 'r') as file:
        p_data = file.read()
    c_data = p_data.replace(string, string +'+')
    with open('planned_task.csv', 'w') as file:
        file.write(c_data)
                

def writer_planned(list):
    with open('planned_task.csv', 'a+', encoding='UTF-8') as file:

        for e in list:
            file.write(f'{e} ')
        file.write('\n')    
  

