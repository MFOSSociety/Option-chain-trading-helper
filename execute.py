import pandas as pd
import matplotlib.pyplot as plt
import os
def call_execute(csv_path,strikeprice):
    os.system('clear')
    data = pd.read_csv(csv_path)

    strikeprice = int(strikeprice)

    data['Date']= pd.to_datetime(data['Date'])
    pd.set_option('display.max_columns', 25)
    pd.set_option('display.width', 100)

    dict = {'Date':[],'LTP':[],'STRIKE PRICE':[],'UNDERLYING VALUE':[]}

    data = data[data.iloc[:,16]!='-']
    data = data.reset_index()
    data = data.drop(columns =  ['index'])

    indicesofinterest = data[data['Strike Price']>=strikeprice].index.values.astype(int)

    for i in range(0,len(indicesofinterest)):
        dict['Date'].append(data.iloc[indicesofinterest[i],:][1])
        dict['STRIKE PRICE'].append(data.iloc[indicesofinterest[i],:][4])
        dict['UNDERLYING VALUE'].append(data.iloc[indicesofinterest[i],:][16])
        dict['LTP'].append(str(data.iloc[indicesofinterest[i],:][9]) + data.iloc[indicesofinterest[1],:][16])

    frame = pd.DataFrame(dict)

    plt.title('LTP vs U.VALUE')
    plt.figure(figsize=(3,8))
    plt.plot(  'Date','LTP', data=frame, marker='*', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4, label = 'OPTION PRICE')
    plt.plot(  'Date','UNDERLYING VALUE', data=frame, marker='*', color='olive', linewidth=2, label = 'U VALUE')
    plt.xticks(rotation = 'vertical')
    plt.legend(loc = 'upper right')


    plt.show()