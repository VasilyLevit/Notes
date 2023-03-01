import csv
import file

def del_note(find_str):
    
    file.exist_file()
    
    with open('notes.csv', "r", newline = '') as data:
        reader = csv.reader(data, delimiter = ';')
        result = []
        for row in reader:
            if find_str not in row:
                result.append(row)
       
    with open('notes.csv', "w", newline = '') as data:
        writer = csv.writer(data, delimiter = ';')
        writer.writerows(result)