import id_note
import datetime

def get_comand():
    print('\n ** Список команд **')
    print('1 - добавить заметку')
    print('2 - показать заметки')
    print('3 - найти заметку')
    print('4 - редактировать заметку')
    print('5 - удалить заметку')
    print('q - выход из программы')

    return input('Введите команду: ')

def get_data():
    note_entry = []

    # get id
    note_entry.append(id_note.get_id())
    
    # get time note
    now = datetime.datetime.now()  
    note_entry.append(now.strftime("%d-%m-%Y %H:%M"))
    
    # get note's head
    note_entry.append(input('Введите название заметки: '))

    # get note's text
    # note_entry.append(input('Введите текст заметки: '))
    
    return note_entry

def get_edit_data(find_str):
    now = datetime.datetime.now()
    note_entry = []
    
    # присвоения id редактируемой заметки
    note_entry.append(find_str)
    
    note_entry.append(now.strftime("%d-%m-%Y %H:%M"))
    note_entry.append(input('Введите новый заголовок заметки: '))
    # note_entry.append(input('Введите новый текст заметки: '))
  
    return note_entry

def get_del_note():
    return input('Введите номер заметки для удаления: ')

def get_find_string():
    return input('Введите номер для поиска: ') # поиск по номеру. сделать поиск по другим полям

def info_del_note():
    print('Заметка удалена')

def print_data(data):
    
    for i in data:
        for j in i:
            print(j)

