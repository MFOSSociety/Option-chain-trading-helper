import pandas as pd
import matplotlib.pyplot as plt
import os
from nsepy import get_history
from datetime import date, timedelta
import time

def call_execute(symbol, strike_price,  option_type, expiry_date):
    os.system('clear')
    print('\n')

    expiry_date = expiry_date.split('-')

    #option_type = input('option type? (CE/ PE)')
    #start = list(map(int, input("Start Date [ year,month,date] [ 2015,1,1 ] ").split(",")))
    #end = list(map(int, input("End Date [ year,month,date] [ 2015,1,10 ] ").split(",")))
    #expiry_date = list(map(int, input("Expiry Date [ year,month,date] [ 2015,1,29 ] ").split(",")))

    strike_price = int(strike_price)

    start = str(date.today() - timedelta(days= 25 ))
    end = str(date.today())
    start = start.split('-')
    end = end.split('-')

    start[1] = start[1].replace('0', '')
    end[1] = end[1].replace('0', '')
    expiry_date[1] = expiry_date[1].replace('0', '')

    stock_opt = get_history(symbol,
                            start=date(int(start[0]), int(start[1]), int(start[2])),
                            end=date(int(end[0]), int(end[1]), int(end[2])),
                            option_type=option_type,
                            strike_price=strike_price,
                            expiry_date=date(int(expiry_date[0]), int(expiry_date[1]), int(expiry_date[2])))

    stock_opt.to_excel('test.xlsx', encoding='latin-1')
    print('stock opt')


    data = pd.read_excel('test.xlsx',  error_bad_lines=False, encoding = 'latin-1')
    print('read file')

    print(f'type {option_type}')
    print(data.head())


    data['Date']= pd.to_datetime(data['Date'])
    pd.set_option('display.max_columns', 15)
    pd.set_option('display.width', 100)

    dict = {'Date':[],'LTP':[],'STRIKE PRICE':[],'UNDERLYING VALUE':[]}

   # data = data[data.iloc[:,16] != '-']
   # data = data.reset_index()
   # data = data.drop(columns =  ['index'])

    indicesofinterest = data[data['Strike Price']>=strike_price].index.values.astype(int)

    for i in range(0,len(indicesofinterest)):
        dict['Date'].append(data.iloc[indicesofinterest[i],:][0])
        dict['STRIKE PRICE'].append(data.iloc[indicesofinterest[i],:][4])
        dict['UNDERLYING VALUE'].append(data.iloc[indicesofinterest[i],:][16])
        dict['LTP'].append(str(data.iloc[indicesofinterest[i],:][9] + data.iloc[indicesofinterest[1],:][16]))

    frame = pd.DataFrame(dict)

    plt.title('LTP vs U.VALUE')
    plt.figure(figsize=(3,8))
    plt.plot(  'Date','LTP', data=frame, marker='*', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4, label = 'OPTION PRICE')
    plt.plot(  'Date','UNDERLYING VALUE', data=frame, marker='*', color='olive', linewidth=2, label = 'U VALUE')
    plt.xticks(rotation = 'vertical')
    plt.legend(loc = 'upper right')



    plt.show()


'''import os
from nsepy import get_history
from datetime import date
import time


symbol = input("Enter Symbol: ")
print('\n')
start = list(map(int,input("Start Date [ year,month,date] [ 2015,1,1 ] ").split(",")))
print()
option_type = input('option type? (CE/ PE)')
end = list(map(int,input("End Date [ year,month,date] [ 2015,1,10 ] ").split(",")))
print()
strike_price = int(input("Strike Price "))
print()
expiry_date = list(map(int,input("Expiry Date [ year,month,date] [ 2015,1,29 ] ").split(",")))

stock_opt = get_history(symbol,
                        start=date(start[0],start[1],start[2]),
                        end=date(end[0],end[1],end[2]),
                        option_type=option_type,
                        strike_price=strike_price,
                        expiry_date=date(expiry_date[0],expiry_date[1],expiry_date[2]))

stock_opt.to_excel('test.xlsx')'''
#os.system(r'excel.exe C:\Users\Karan\PycharmProjects\calls options\Option-chain-trading-helper-master\test.xlsx
