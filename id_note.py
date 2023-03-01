import csv
# import os.path

def get_id():
    # if os.path.isfile('notes.csv') == False:
    #     file = open('notes.csv','w')
    #     file.close
    #     print('Отсутстует файл замето. Создан новый')
    
    with open('notes.csv', newline='') as data:
        reader = csv.reader(data, delimiter = ';')
        max_id = max(int(row[0]) for row in reader)
        next_id = max_id + 1
    
    return next_id