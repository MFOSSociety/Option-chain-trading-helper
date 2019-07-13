# Option-chain-trading-helper
A tool to help detect insider trading, by comparing Option chain prices against the underlying value of the stock


# Use - 

- Visit this [link](https://www.nseindia.com/products/content/derivatives/equities/historical_fo.htm)
- Select -> stock options-> symbol of choice -> The Year -> expiry date -> (CE/PE) in option type  (_example: stock options-> BHEL -> 2019 -> 25-07-19 -> CE_)
- Download the CSV file
- Run theTool.py, provide the path to the csv and then the strike price 
- The graph shows true value for underlying value and a scaled value for the option type for easy comparison

# The working - 
- The option types we're interested in are Puts and Calls ( PE and CE) 
- The knowledge relevant to our task is, the price of CE is directly proportional to the price of the stock (underlying value) and the price of PE is inversely proportional to the price of the stock. 
- If the pyplot shows that the values dont follow the pattern, then we can say with some confidence that someone is trading on the inside or maybe someone is manipulating the prices. What often follows is a drastic change in all the values ( CE PE and the underlying value) 


EXAMPLE : _ICICPRU How a Put against u.value should look like_ - https://imgur.com/a/Y4Pi2Zc 
           

This is the PE option type vs U.value for ICICIPRU . PE varies inversely with the underlying value as can be seen. This implies everything is normal.

EXAMPLE 2: _BHEL How a Call against u.value **should not** look like_ - https://imgur.com/a/vHtWDcZ

This is the CE option type vs U.value for BHEL. CE varies directly with underlying value but in the red circled area, the stock price drops and the CE option price doesnt. This means somebody knew that the stock price would go back up and hence they bought a lot of call options, you can see the stock price then did skyrocket, where this insider sold off their call options, making a huge profit. 

_This is the anomaly that we want to detect._



