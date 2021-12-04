import pandas as pd


#this module reads a list of tickers from a .csv file of all nasdaq tickers 
#it's not really used within the module but more to scrap tickers when needed 

def gettickers(tickerspath, sector, numberoftickers, updateData):
    # no finance and no utilities sectors
    # some important parameters to be passed here such as sector, mktcap etc
    if (updateData):
        # tickerspath is a saved .csv of all nasdaq tickers
        df = pd.read_csv(tickerspath)
        # Greenblatt's Magic Formula excludes stocks from Finance and Utilities sector and MKT cap > 100m
        df = df.drop(df.index[df['Sector'] == 'Public Utilities'].to_list(
        )+df.index[df['Sector'] == 'Finance'].to_list())
        # market cap greater than 100 million
        df = df[df['Market Cap'] > 10000000000]  # 10 MIL
        # sort by market cap then take 40 biggest?
        df = df.sort_values(by=['Market Cap'], ascending=False)
        df = df.reset_index().drop(columns=['index'])
        # Going to chose stocks from tech sector for now
        # df = df[df['Sector'] == sector]
        start = 0
        df = df.iloc[start:start+numberoftickers]  # 350-390
        df['Symbol'] = df['Symbol']
        all_tickers = df.Symbol.tolist()
        print('Tickers Retrieved!')

        return all_tickers