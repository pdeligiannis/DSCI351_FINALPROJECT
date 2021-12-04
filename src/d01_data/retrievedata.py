import yfinance as yf 
import pandas as pd 
import numpy as np 
from os import path 


def gettimeseries(all_tickers,timeseriessavepath,companyinformationsavepath,financialinformationsavepath): 
    list_of_columns = ['id','Date','Open','High','Low','Close','Volume','adj_close','returns','cumulative_returns']
    if(path.exists(timeseriessavepath)): 
        print('Timeseries file already exists!')
    else: 
        list_of_dfs = [] 
        list_of_dfs_2 = []
        list_of_dfs_3 = []  
        aggregate_df = pd.DataFrame()  #ts data 
        aggregate_company_info_df = pd.DataFrame()  #company info data 
        aggregate_fin_info_df = pd.DataFrame()  #fundamental info data 
        id = 0 
        for ticker in all_tickers: 
            #creating TS df 
            data = yf.download(ticker,period='5y',interval='1d')
            # data['Ticker'] = ticker 
            data['id'] = id 
            data = data.rename(columns={"Adj Close": "adj_close"}) 
            data['returns'] = data['adj_close'].pct_change() 
            data['cumulative_returns'] = data['returns'].cumsum()
            data = data.dropna() 
            list_of_dfs.append(data)
            #creating the company info df 
            company_info_df = pd.DataFrame(np.zeros((1, 5)),columns=[
                'id', 'ticker', 'name', 'market', 'city']) 
            company_info_df['id'] = id 
            company_info_df['ticker'] = ticker 
            search_result = yf.Ticker(ticker).info 
            company_name = search_result['shortName']
            market = search_result['market']
            city = search_result['city']
            company_info_df['name'] = company_name
            company_info_df['market'] = market
            company_info_df['city'] = city
            list_of_dfs_2.append(company_info_df)
            #creating the company financial information table 
            fin_info = pd.DataFrame(np.zeros((1, 9)),columns=[
                'id', 'currency', 'market_cap', 'average_volume_traded', 'fifty_two_wk_high','fifty_two_wk_low','current_price','fifty_two_wk_change','divident_yield']) 
            fin_info['id'] = id 
            fin_info['currency'] = 'USD'
            fin_info['market_cap'] = search_result['marketCap']
            fin_info['average_volume_traded'] = search_result['volume']
            fin_info['fifty_two_wk_high'] = search_result['fiftyTwoWeekHigh']
            fin_info['fifty_two_wk_low'] = search_result['fiftyTwoWeekLow']
            fin_info['current_price'] = search_result['currentPrice']
            fin_info['fifty_two_wk_change'] = search_result['52WeekChange']
            fin_info['divident_yield'] = search_result['dividendYield']
            fin_info = fin_info.fillna(value=0.0)
            list_of_dfs_3.append(fin_info)
            #** 
            id += 1 #creating unique ids 
        aggregate_fin_info_df = pd.concat(list_of_dfs_3)
        aggregate_company_info_df = pd.concat(list_of_dfs_2)
        aggregate_df = pd.concat(list_of_dfs)
        aggregate_df = aggregate_df.dropna() 
        #order types for fin info 
        aggregate_fin_info_df['currency'] = aggregate_fin_info_df['currency'].astype('|S80')
        aggregate_fin_info_df['fifty_two_wk_change'] = aggregate_fin_info_df['fifty_two_wk_change'].astype(float)
        aggregate_fin_info_df['divident_yield'] = aggregate_fin_info_df['divident_yield'].astype(float)
        #types for others 
        aggregate_company_info_df.to_pickle(companyinformationsavepath)
        aggregate_fin_info_df.to_pickle(financialinformationsavepath)
        aggregate_df['Open'] = aggregate_df['Open'].astype(float)
        aggregate_df['High'] = aggregate_df['High'].astype(float)
        aggregate_df['Low'] = aggregate_df['Low'].astype(float)
        aggregate_df['Close'] = aggregate_df['Close'].astype(float)
        aggregate_df['adj_close'] = aggregate_df['adj_close'].astype(float)
        aggregate_df['returns'] = aggregate_df['returns'].astype(float)
        aggregate_df['cumulative_returns'] = aggregate_df['cumulative_returns'].astype(float)
        aggregate_df['Volume'] = aggregate_df['Volume'].astype(float)
        aggregate_df = aggregate_df.reset_index() 
        aggregate_df['Date'] = pd.to_datetime(aggregate_df['Date'])
        aggregate_df['Date'] = aggregate_df['Date'].dt.strftime('%m-%d-%Y')
        aggregate_df['Date'] = pd.to_datetime(aggregate_df['Date'])
        aggregate_df = aggregate_df[list_of_columns]
        aggregate_df.to_pickle(timeseriessavepath)
        print('Timeseries Data Retrieved!')
        print('Company Information Data Retrieved!')
        print('Financial Information Data Retrieved!')

#currency
#marketCap 
#avg volume ->volume 
#fiftyTwoWeekHigh
#fiftyTwoWeekLow 
#dividentYield 
#dp52WeekChange 
#currentPrice 

# def main(): 
#     all_tickers = ['AAPL','MSFT']
#     timeseriessavepath = './data/data_retrieval/rawts.pickle'
#     companyinformationsavepath = './data/data_retrieval/companyinfo.pickle'
#     financialinformationsavepath = './data/data_retrieval/financialinfo.pickle'
#     gettimeseries(all_tickers,timeseriessavepath,companyinformationsavepath,financialinformationsavepath)
#     fin_info = pd.read_pickle(financialinformationsavepath)
#     print(fin_info.info())
# main() 
