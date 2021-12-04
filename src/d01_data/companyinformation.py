import yfinance as yf 

def getcompanyinformation(all_tickers):
    for ticker in all_tickers: 
        search_result = yf.Ticker(ticker).info 
        print(search_result)