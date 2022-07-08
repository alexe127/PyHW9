from process_file import writer_planned
from process_file import writer_compl
from logger import add_in_log
from process_file import del_record


def build_planned(string):
    record = string
    final_record = tuple( i for i in record.split(' '))
    message = str(f'добавлено в базу: {record}')
    add_in_log(message)
    writer_planned(final_record)


def build_compl(string):
    message = str(f'{string}  выполнено')
    add_in_log(message)
    writer_compl(string)


def build_del(string):
    message = str(f'удалено из базы: {string}')
    add_in_log(message)
    del_record(string)





