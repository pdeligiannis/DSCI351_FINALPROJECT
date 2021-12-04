import os
import sys
import tickers 
import retrievedata 
import companyinformation 


def main(readtickerspath,sector,numberoftickers,timeseriessavepath,companyinformationsavepath,financialinformationsavepath,updateData=True):

    #returns list of tickers from the given paremeters 
    all_tickers = tickers.gettickers(readtickerspath,sector,numberoftickers,updateData) 
    print('Tickers Retrieved!')
    retrievedata.gettimeseries(all_tickers,timeseriessavepath,companyinformationsavepath,financialinformationsavepath)
    print('Data Retrieved!')
    # companyinformation.getcompanyinformation(all_tickers)


if __name__ == "__main__":
    
    datapath = './data/data_retrieval/'

    try:
        readtickerspath = sys.argv[1]
    except:
        readtickerspath = datapath+'00_nasdaqtickers.csv'

    #do we pass a list of sectors here ? 
    try:
        sector = sys.argv[2]
    except:
        sector = 'Technology'

    try:
        numberoftickers = sys.argv[3]
    except:
        numberoftickers = 4 

    try:
        updateData = sys.argv[4]
    except:
        updateData = True 

    try:
        timeseriessavepath = sys.argv[5]
    except: 
        timeseriessavepath = datapath+'rawtimeseries_'+sector+'_.pickle'

    try: 
        companyinformationsavepath = sys.argv[6]
    except: 
        companyinformationsavepath = datapath+'companyinformation_'+sector+'_.pickle'
    
    try: 
        financialinformationsavepath = sys.argv[7]
    except: 
        financialinformationsavepath = datapath+'financialinformation_'+sector+'_.pickle'


    main(readtickerspath,sector,numberoftickers,timeseriessavepath,companyinformationsavepath,financialinformationsavepath,updateData)

#def gettickers(tickerspath, sector, numberoftickers, updateData):