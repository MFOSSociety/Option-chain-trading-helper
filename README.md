# Option-chain-trading-helper
A tool to help detect insider trading, by comparing Option chain prices against the underlying value of the stock


# Use - 

- visit https://www.nseindia.com/products/content/derivatives/equities/historical_fo.htm '
- Select -> stock options-> symbol of choice -> The Year -> expiry date -> (CE/PE) in option type  (_example: stock options-> BHEL -> 2019 -> 25-07-19 -> CE_)
- Download the CSV file
- Run theTool.py, provide the path to the csv and then the strike price 
- The graph shows true value for underlying value and a scaled value for the option type for easy comparison

