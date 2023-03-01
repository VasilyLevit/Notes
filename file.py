import os.path

def exist_file():
    if os.path.isfile('notes.csv') == False:
        file = open('notes.csv','w')
        file.close
        print('Отсутствует файл заметок. Создан новый')