import os
import sys
import pandas as pd 
import sqliteconnector 
import sqlitedb 

def main(dbpath,rawtimeseries,companyinfo,financialinfo):
    #first we load all the local file datas into dataframes 
    company_table = pd.read_pickle(companyinfo)
    financial_table = pd.read_pickle(financialinfo)
    timeseries_table = pd.read_pickle(rawtimeseries)
    #then we create the database 
    conn = sqliteconnector.create_database(dbpath) #creates db and returns connection 
    sqlitedb.db(conn,company_table,financial_table,timeseries_table) #creates tables 
    print('Database created!')

    #after establishing the database and connection, we create the tables 
    # company_table.to_sql("company",conn,if_exists="append",index=False) 
    # financial_table.to_sql("financialinformation", conn, if_exists="append", index=False)
    # timeseries_table.to_sql("security_price", conn, if_exists="append", index=False)

if __name__ == "__main__":
    databasepath = './data/database/'
    datapath = './data/data_retrieval/' 

    #**need a used list of sectors file 

    try:
        dbpath = sys.argv[1]
    except:
        dbpath = databasepath+'sqlp1.db'
    try:
        rawtimeseries = sys.argv[2]
    except: 
        rawtimeseries = datapath+'rawtimeseries_Technology_.pickle'
    try:
        companyinfo = sys.argv[3]
    except: 
        companyinfo = datapath+'companyinformation_Technology_.pickle'
    try:
        financialinfo = sys.argv[4]
    except: 
        financialinfo = datapath+'financialinformation_Technology_.pickle'


    main(dbpath,rawtimeseries,companyinfo,financialinfo)

#def gettickers(tickerspath, sector, numberoftickers, updateData):