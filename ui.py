import id_note
import datetime

def get_comand():
    print('\n - Список команд')
    print('1 - добавить заметку')
    print('2 - показать заметки')
    print('3 - найти заметку')
    print('q - выход из программы')

    return input('Введите номер операции: ')

def get_data():
    note_entry = []

    # get id
    note_entry.append(id_note.get_id())
    
    # get time note
    now = datetime.datetime.now()  
    note_entry.append(now.strftime("%d-%m-%Y %H:%M"))
    
    # get note's head
    note_entry.append(input('Введите номер заметки: '))

    # get note's text
    # note_entry.append(input('Введите текст заметки: '))
    
    return note_entry

def print_data(data):
    # print(data)
    for i in data:
        for j in i:
            print(j)

def get_find_string():
    return input('Введите слово для поиска: ') # поиск по номеру. сделать поиск по другим полям