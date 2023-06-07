from functional import addnote, findnote, editnote, delnote, shownotes

def view():
    print("""Выберете режим работы:
            1 - создание записи
            2 - просмотр записей
            3 - найти запись
            4 - удаление записи
            5 - изменение записи
            6 - выход
              """)
    mode = int(input('Введите номер режима: '))
    while mode < 1 or mode > 6:
        mode = int(input('Введите корректный номер: '))
    if mode == 1:
        addnote()
    elif mode == 2:
        shownotes()
    elif mode == 3:
        findnote()
    elif mode == 4:
        delnote()
    elif mode == 5:
        editnote()
    elif mode == 6:
        exit()
    view()