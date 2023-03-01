import csv
import file

def find_data(find_str):
    file.exist_file()
    with open('notes.csv', "r") as data:
        reader = csv.reader(data, delimiter = ';')
        result = []
        for row in reader:
            if find_str in row:
                result.append(row)
        # else:
        #     result.append('Не найдено')
    
    return result

