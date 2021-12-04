import sqlite3
from sqlite3 import Error

def db(conn, company_table,financial_table,timeseries_table): 
    company_table.to_sql("company",conn,if_exists="append",index=False) 
    financial_table.to_sql("financialinformation", conn, if_exists="append", index=False)
    timeseries_table.to_sql("security_price", conn, if_exists="append", index=False)
    # print('Database Tables Created!')