
from datetime import datetime as dt


def add_in_log(str_log):
    date = dt.now().strftime("Date: %d/%m/%Y  time: %H:%M:%S")
    with open(file_log, 'a', encoding='UTF-8') as log:
               
        log.write('{} {}\n'. format(str_log, date))
        
        
file_log = 'log.txt'
# file_log = 'log.csv'




# import logging  ## https://python-scripts.com/logging-python  https://habr.com/ru/post/144566/

# logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)


# logging.basicConfig(filename="sample.log", level=logging.INFO) 
# logging.debug("This is a debug message")
# logging.info("Informational message")
# logging.error("An error has happened!")
