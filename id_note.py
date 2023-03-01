import csv
import os

def get_id():
    if os.path.isfile('notes.csv') == False:
        file = open('notes.csv','w')
        file.close
        print('Отсутстует файл заметок. Создан новый')
    
    if os.stat('notes.csv').st_size == 0:
        next_id = 1
    else:
        with open('notes.csv', newline='') as data:
            reader = csv.reader(data, delimiter = ';')
            max_id = max(int(row[0]) for row in reader)
            next_id = max_id + 1
    
    return next_id