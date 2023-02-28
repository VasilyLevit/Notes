# Задание
Необходимо написать проект, содержащий функционал работы с заметками. 
Программа должна уметь 
    создавать заметку
    сохранять её,
    читать список заметок, 
    редактировать заметку, 
    удалять заметку.
    
Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок.
Заметка должна содержать: 
идентификатор, 
заголовок, 
тело заметки, 
дату/время создания или последнего изменения заметки. 

Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой). Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры запуска программы (команда, данные), можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.  
    идентификатор, 
    заголовок,
    тело заметки, 
    дату/время создания или последнего изменения заметки. 
Сохранение заметок необходимо сделать в формате json или csv формат 
(разделение полей рекомендуется делать через точку с запятой). 

При чтении списка заметок реализовать фильтрацию по дате

Примеры реализации пользовательского интерфейса:

Пример 1

python notes.py add --title "новая заметка" –msg "тело новой заметки"

Пример 2

python note.py Введите команду: add
Введите заголовок заметки: новая заметка 
Введите тело заметки: тело новой заметки 
Заметка успешно сохранена
Введите команду: