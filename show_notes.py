import csv
import file

def show_data():
    file.exist_file()
    with open('notes.csv', "r") as data:
        reader = csv.reader(data, delimiter = ';')
        result_all = []
        for row in reader:
            result_all.append(row)
    return result_all