import ui
import save_note
import show_notes
import find
import edit
import delete

def button_click():
    operation = 0
    while operation != 'q':
        try:
            operation = ui.get_comand()
            if operation == 'a':
                save_note.log_data(ui.get_data()) # получение данных из пользоватлеьского интерфейса и передача для записи       
            elif operation == 'v':
                ui.print_data(show_notes.show_data())
            elif operation == 'f':
                ui.print_data(find.find_data(ui.get_find_string()))
            elif operation == 'e':
                ui.print_data(edit.edit_data(ui.get_find_string()))
            elif operation == 'd':
                delete.del_note(ui.get_find_string())
                ui.info_del_note()
            elif operation !='q':
                print("Ошибка ввода. Введите правильную команду")
            else:
                operation = 'q'
        except:
            print("Ошибка ввода. Введите команду из списка")
