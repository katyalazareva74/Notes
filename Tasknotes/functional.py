import os
import csv
import pandas as pd
from datetime import datetime   
    
from data_create import name_data, text_data, dattime_data

filename = 'notes3.csv'
def addnote(): 
    if os.path.exists(filename):   
        with open(filename, "r", newline="") as file:
            df = pd.read_csv(file)
            df['Date'] = pd.to_datetime(df['Date'])
            print('Введите данные для заметки: ')
            name = name_data()
            text = text_data()
            dattime = dattime_data()
            df.loc[ len(df.index )] = [dattime, name, text]
            print(df)
            df.to_csv (r'notes3.csv', index= False )
    else:
        with open(filename, "w", newline="", encoding='utf-8') as file:
            csv_columns = ['Date','Name','Text']
            writer = csv.DictWriter(file, fieldnames=csv_columns)
            writer.writeheader()
            print('Создан новый файл')
            

addnote()
