import csv
import os.path

def show_data():
    
    if os.path.isfile('notes.csv') == False:
        file = open('notes.csv','w')
        file.close
        print('Отсутстует файл замето. Создан новый')
    with open('notes.csv', "r") as data:
        reader = csv.reader(data, delimiter = ';')
        result_all = []
        for row in reader:
            result_all.append(row)
    return result_all