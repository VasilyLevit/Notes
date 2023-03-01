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
            if operation == '1':
                save_note.log_data(ui.get_data()) # получение данных из пользоватлеьского интерфейса и передача для записи       
            elif operation == '2':
                ui.print_data(show_notes.show_data())
            elif operation == '3':
                ui.print_data(find.find_data(ui.get_find_string()))
            elif operation == '4':
                ui.print_data(edit.edit_data(ui.get_find_string()))
            elif operation == '5':
                delete.del_note(ui.get_find_string())
                ui.info_del_note()
            else:
                operation = 'q'
        except:
            print("Ошибка ввода. Введите число от 1 до 6")

# def enter_first_menu() -> int:
   
#     while True:
#         try:
#             answer = int(input("Please enter that do you want to do. \n" +
#                                "enter 1: to add a new note,\nenter 2: to read one note,\n" +
#                                "enter 3: to read all notes that you have,\nenter 4: to update an existing note,\n" +
#                                "enter 5: to delete an existing note,\nenter 6: to exit the application\n"))
#             if 0 <= answer <= 6:
#                 return answer
#             else:
#                 print("You entered wrong number")
#         except:
#             print("You're wrong. Try again")