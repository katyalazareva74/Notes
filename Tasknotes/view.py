from functional import addnote, findnote, editnote, delnote, shownotes, shownotesperiod

def view():
    print("""Выберете режим работы:
            1 - создание заметки
            2 - просмотр заметок
            3 - просмотр периода заметок
            4 - найти заметку
            5 - изменение заметки
            6 - удаление заметки
            7 - выход
              """)
    mode = int(input('Введите номер режима: '))
    while mode < 1 or mode > 7:
        mode = int(input('Введите корректный номер: '))
    if mode == 1:
        addnote()
    elif mode == 2:
        shownotes()
    elif mode == 3:
        shownotesperiod()
    elif mode == 4:
        findnote()
    elif mode == 5:
        editnote()
    elif mode == 6:
        delnote()
    elif mode == 7:
        exit()
    view()