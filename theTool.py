import pandas as pd
import matplotlib.pyplot as plt

csv_name = str(input('Name of the csv file? (example - wipro.csv)'))
strikeprice = int(input('strike price ? :: '))
data = pd.read_csv(f'C:\\Users\\keerti\\Downloads\\{csv_name}.csv')
data['Date']= pd.to_datetime(data['Date'])
pd.set_option('display.max_columns', 25)
pd.set_option('display.width', 100)

dict = {'Date':[],'LTP':[],'STRIKE PRICE':[],'UNDERLYING VALUE':[]}


indicesofinterest = data[data['Strike Price']==strikeprice].index.values.astype(int)
print(indicesofinterest)
for i in range(0,len(indicesofinterest)):
    dict['Date'].append(data.iloc[indicesofinterest[i],:][1])
    print(data.iloc[indicesofinterest[i],:][1])
    dict['STRIKE PRICE'].append(data.iloc[indicesofinterest[i],:][4])
    dict['UNDERLYING VALUE'].append(data.iloc[indicesofinterest[i],:][16])
    dict['LTP'].append(data.iloc[indicesofinterest[i],:][9] + data.iloc[indicesofinterest[1],:][16])

frame = pd.DataFrame(dict)
print(frame)
plt.title('LTP vs U.VALUE')
plt.figure(figsize=(3,8))
plt.plot(  'Date','LTP', data=frame, marker='*', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4, label = 'OPTION PRICE')
plt.plot(  'Date','UNDERLYING VALUE', data=frame, marker='*', color='olive', linewidth=2, label = 'U VALUE')
plt.xticks(rotation = 'vertical')
plt.legend(loc = 'upper right')


plt.show()
