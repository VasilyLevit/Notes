import csv

def log_data(entry):
    with open('notes.csv', 'a') as data:           # сделать передачу имени файла (или напрямую при создании или из файла конфигурации)
        writer = csv.writer(data, delimiter = ';')
        writer.writerow(entry)