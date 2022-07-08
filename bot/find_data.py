
def find(filename):

    find_plans = open(filename, mode='r+')

    find_plans = find_plans.readlines()

    for line in find_plans:

        if key_word.lower() in line.lower():

            print(line)