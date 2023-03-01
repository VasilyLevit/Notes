import csv
import ui
import os

def edit_data(find_str):
    # проверка наличия файла с заметками
    if os.path.isfile('notes.csv') == False:
        file = open('notes.csv','w')
        file.close
        print('Отсутствует файл заметок. Создан новый')
    
    with open('notes.csv', "r", newline = '') as data:
        reader = csv.reader(data, delimiter = ';')
        result = []
        for row in reader:
            if find_str in row:
                result.append(ui.get_edit_data(find_str))
            else:
                result.append(row)
       
    with open('notes.csv', "w", newline = '') as data:
        writer = csv.writer(data, delimiter = ';')
        writer.writerows(result)