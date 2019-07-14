import os
try:
    os.system('sudo pip install nsepy')
    os.system('sudo pip3 install nsepy')

except:
    pass
from nsepy import get_history
from datetime import date
import time

os.system('clear')
print()
print("Enter date in form of year,month,date")
time.sleep(3)
print()
print()
symbol = input("Enter Symbol: ")
print()
start = list(map(int,input("Start Date [ year,month,date] [ 2015,1,1 ] ").split(",")))
print()
end = list(map(int,input("End Date [ year,month,date] [ 2015,1,10 ] ").split(",")))
print()
strike_price = int(input("Strike Price "))
print()
expiry_date = list(map(int,input("Expiry Date [ year,month,date] [ 2015,1,29 ] ").split(",")))

stock_opt = get_history(symbol,
                        start=date(start[0],start[1],start[2]),
                        end=date(end[0],end[1],end[2]),
                        option_type="CE",
                        strike_price=strike_price,
                        expiry_date=date(expiry_date[0],expiry_date[1],expiry_date[2]))

stock_opt.to_excel('test.xlsx')
os.system('libreoffice --calc test.xlsx')