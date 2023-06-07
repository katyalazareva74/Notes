import os
import csv
import pandas as pd
from datetime import datetime   
    
from data_create import name_data, text_data, dattime_data, id_data

filename = 'notes3.csv'
def addnote(): 
    if os.path.exists(filename):   
        with open(filename, "r", newline="") as file:
            df = pd.read_csv(file, sep=';')
            df['Date'] = pd.to_datetime(df['Date'])
            print('Введите данные для заметки: ')
            name = name_data()
            id = id_data()
            text = text_data()
            dattime = dattime_data()
            dat = datetime.strptime(dattime, "%Y-%m-%d %H:%M")
            df.loc[ len(df.index )] = [id, dat, name, text]
            strnew=df.iloc [[df.shape [0]-1]]
            print(strnew,'\nЗапись сохранена\n')
            df.to_csv (r'notes3.csv', index= False, sep=';')
    else:
        with open(filename, "w", newline="", encoding='utf-8') as file:
            csv_columns = ['ID','Date','Name','Text']
            writer = csv.DictWriter(file, delimiter = ';', fieldnames=csv_columns)
            writer.writeheader()
            print('Создан новый файл\n')
            
def findnote():
    if os.path.exists(filename):   
        with open(filename, "r", newline="") as file:
            df = pd.read_csv(file, sep=';')
            df['Date'] = pd.to_datetime(df['Date'])
            dat1=dattime_data()
            print(dat1)
            filtr=df.loc[(df['Date'] == dat1)]
            if(filtr.empty):
                print('Запись не найдена\n')
            else:
                print(filtr)
    else:
        print('Файл не найден\n')

def editnote():
    if os.path.exists(filename):   
        with open(filename, "r", newline="") as file:
            df = pd.read_csv(file, sep=';')
            df['Date'] = pd.to_datetime(df['Date'])
            dat1=dattime_data()
            print(dat1)
            filtr=df.loc[(df['Date'] == dat1)]
            if(filtr.empty):
                print('Запись не найдена\n')
            else:
                print(filtr)
                ifiltr=filtr.index [ 0 ]
                dat2=input('По какому столбцу редактировать запись  (Name или Text)? ')
                if (dat2 == 'Name'):
                    df.at[ifiltr, 'Name']= name_data()
                else:
                    df.at[ifiltr,'Text'] = text_data()
                df.at[ifiltr, 'Date'] = dattime_data()
                print(filtr,'\nЗапись отредактирована\n')
                df.to_csv (r'notes3.csv', index= False, sep=';')
    else:
        print('Файл не найден\n')

def delnote():
    if os.path.exists(filename):   
        with open(filename, "r", newline="") as file:
            df = pd.read_csv(file, sep=';')
            df['Date'] = pd.to_datetime(df['Date'])
            dat1=dattime_data()
            filtr=df.loc[(df['Date'] == dat1)]
            if(filtr.empty):
                print('Запись не найдена\n')
            else:
                print(filtr,'\nЗапись удалена\n')
                ifiltr=filtr. index [ 0 ]
                df = df.drop (index= ifiltr )
                df.to_csv (r'notes3.csv', index= False, sep=';')
    else:
        print('Файл не найден\n')

def shownotes():
    if os.path.exists(filename):   
        with open(filename, "r", newline="") as file:
            df = pd.read_csv(file, sep=';')
            df['Date'] = pd.to_datetime(df['Date'])
            df=df.sort_values (by='Date')
            print(df)
            df.to_csv (r'notes3.csv', index= False, sep=';')
    else:
        print('Файл не найден\n')
