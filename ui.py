def get_comand():
    print('\n1 - добавить заметку')

    return input('Введите номер операции: ')

def get_data():
    # now = datetime.datetime.now()
    note_entry = []
    # note_entry.append(book_id.get_id())
    note_entry.append(input('Введите заголовок заметки: '))
    # note_entry.append(input('Введите текст заметки: '))
    # note_entry.append(now.strftime("%d-%m-%Y %H:%M"))
    return note_entry