
from datetime import datetime

def name_data():
    name = input('Введите название заметки: ')
    return name

def text_data():
    text = input('Введите текст заметки: ')
    return text

def dattime_data():
    dattime = input('Введите дату и время создания заметки  в формате yyyy-dd-mm hh:mm: ')
    #dat = datetime.strptime(dattime, "%Y-%d-%m %H:%M")
    return dattime