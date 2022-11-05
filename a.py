import yfinance as yf
import pandas as pd 

index = pd.read_csv("nifty-next-50.csv", index_col=False)
nifty_next_50 = index["SYMBOL \n"][1:]

tickers = '.NS '.join(nifty_next_50) +'.NS'

# print(tickers)


# data = yf.download(tickers, period = "1mo",interval = "1mo")
data = yf.download("ADANIENT.NS", start = "2022-10-06",end = "2022-11-04" )

print(data)
