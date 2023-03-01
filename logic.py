import ui
import save_note
import show_notes
import find

def button_click():
    operation = 0
    while operation != 'q':
        operation = ui.get_comand()
        if operation == '1':
            save_note.log_data(ui.get_data()) # получение данных из пользоватлеьского интерфейса и передача для записи
        
        elif operation == '2':
            ui.print_data(show_notes.show_data())          
             
        elif operation == '3':
            ui.print_data(find.find_data(ui.get_find_string()))
                   
        else:
            operation = 'q'