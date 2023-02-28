# import current_time as ctime
import datetime

def get_comand():
    print('\n1 - добавить заметку')

    return input('Введите номер операции: ')

def get_data():
    note_entry = []
    now = datetime.datetime.now()
    # note_entry.append(book_id.get_id())
    # now = ctime.get_time
   
    note_entry.append(now.strftime("%d-%m-%Y %H:%M"))
    note_entry.append(input('Введите заголовок заметки: '))
    # note_entry.append(input('Введите текст заметки: '))
    
    return note_entry