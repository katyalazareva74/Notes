import os
import csv
import pandas as pd
from datetime import datetime   
    
from data_create import name_data, text_data, dattime_data, id_data

filename = 'notes.csv'
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
            try:
                dat = datetime.strptime(dattime, "%Y-%m-%d %H:%M")
                df.loc[ len(df.index )] = [id, dat, name, text]
                strnew=df.iloc [[df.shape [0]-1]]
                print(strnew,'\nЗапись сохранена\n')
                df.to_csv (r'notes.csv', index= False, sep=';')
            except ValueError:
                    print('Дата и время не соответствуют формату. Попробуйте еще раз!')
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
            try:
                dat1 = datetime.strptime(dat1, "%Y-%m-%d %H:%M")
                print(dat1)
                filtr=df.loc[(df['Date'] == dat1)]
                if(filtr.empty):
                    print('Заметка не найдена. Уточните дату и время.\n')
                else:
                    print(filtr)
            except ValueError:
                    print('Дата и время не соответствуют формату. Попробуйте еще раз!')
    else:
        print('Файл не найден\n')

def editnote():
    if os.path.exists(filename):   
        with open(filename, "r", newline="") as file:
            df = pd.read_csv(file, sep=';')
            df['Date'] = pd.to_datetime(df['Date'])
            dat1=dattime_data()
            try:
                dat1 = datetime.strptime(dat1, "%Y-%m-%d %H:%M")
                print(dat1)
                filtr=df.loc[(df['Date'] == dat1)]
                if(filtr.empty):
                    print('Заметка не найдена. Уточните дату и время.\n')
                else:
                    print(filtr)
                    ifiltr=filtr.index [ 0 ]
                    dat2=input('По какому столбцу редактировать заметку  (Name или Text)? ')
                    if (dat2 == 'Name'):
                        df.at[ifiltr, 'Name']= name_data()
                    else:
                        df.at[ifiltr,'Text'] = text_data()
                    df.at[ifiltr, 'Date'] = dattime_data()
                    stredit=df.loc[[ifiltr]]
                    print(stredit,'\nЗаметка отредактирована\n')
                    df.to_csv (r'notes.csv', index= False, sep=';')
            except ValueError:
                print('Дата и время не соответствуют формату. Попробуйте еще раз!')
    else:
        print('Файл не найден\n')

def delnote():
    if os.path.exists(filename):   
        with open(filename, "r", newline="") as file:
            df = pd.read_csv(file, sep=';')
            df['Date'] = pd.to_datetime(df['Date'])
            dat1=dattime_data()
            try:
                dat1=datetime.strptime(dat1, "%Y-%m-%d %H:%M" )
                filtr=df.loc[(df['Date'] == dat1)]
                if(filtr.empty):
                    print('Заметка не найдена. Уточните дату и время.\n')
                else:
                    print(filtr,'\nЗаметка удалена\n')
                    ifiltr=filtr. index [ 0 ]
                    df = df.drop (index= ifiltr )
                    df.to_csv (r'notes.csv', index= False, sep=';')
            except ValueError:
                    print('Дата и время не соответствуют формату. Попробуйте еще раз!')
    else:
        print('Файл не найден\n')

def shownotes():
    if os.path.exists(filename):   
        with open(filename, "r", newline="") as file:
            df = pd.read_csv(file, sep=';')
            df['Date'] = pd.to_datetime(df['Date'])
            df=df.sort_values (by='Date')
            print(df)
            df.to_csv (r'notes.csv', index= False, sep=';')
    else:
        print('Файл не найден\n')

def shownotesperiod():
    if os.path.exists(filename):   
        with open(filename, "r", newline="") as file:
            df = pd.read_csv(file, sep=';')
            df['Date'] = pd.to_datetime(df['Date'])
            dat1=input('Введите дату начала периода в формате yyyy-mm-dd: ')
            try:
                dat1=datetime.strptime(dat1, "%Y-%m-%d")
                dat2=input('Введите дату окончания периода в формате yyyy-mm-dd: ')
                try:
                    filtr=df.loc[(df['Date'] > dat1)&(df['Date'] < dat2)]
                    if(filtr.empty):
                        print('Заметок не найдено. Уточните даты.\n')
                    else:
                        print(filtr)
                except ValueError:
                    print('Дата и время не соответствуют формату. Попробуйте еще раз!')
            except ValueError:
                    print('Дата и время не соответствуют формату. Попробуйте еще раз!')
    else:
        print('Файл не найден\n')
