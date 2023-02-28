import ui
import save_note as save
# import book_show as bsh
# import book_find as bf

def button_click():
    operation = 0
    while operation != '2':
        operation = ui.get_comand()
        if operation == '1':
            save.log_data(ui.get_data()) # получение данных из пользоватлеьского интерфейса и передача для записи
        
        # elif operation == '2':
        #     ui.print_data(bsh.show_data())          
             
        # elif operation == '3':
        #     ui.print_data(bf.find_data(ui.get_find_string()))
                   
        else:
            operation = '2'