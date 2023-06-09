import os
import pandas as pd

def name_data():
    name = input('Введите название заметки: ')
    return name

def text_data():
    text = input('Введите текст заметки: ')
    return text

def dattime_data():
    dattime = input('Введите дату и время создания заметки  в формате yyyy-mm-dd hh:mm: ')
    return dattime

def id_data():
    filename = 'notes.csv'
    if os.path.exists(filename):   
        with open(filename, "r", newline="") as file:
            df = pd.read_csv(file, sep=';')
            if(df.empty):
                return 1
            else:
                max = df['ID'].max()
                return max+1
    else:
        print('Файл не найден\n')