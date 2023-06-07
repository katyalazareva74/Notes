import os
import csv
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
    filename = 'notes3.csv'
    if os.path.exists(filename):   
        with open(filename, "r", newline="") as file:
            df = pd.read_csv(file, sep=';')
            df['Date'] = pd.to_datetime(df['Date'])
            df=df.sort_values (by='ID')
            print(df)
            if(df.empty):
                return 1
            else:
                col=df.shape [0]
                id = df.at[col-1, 'ID']
                return id+1
    else:
        print('Файл не найден.')