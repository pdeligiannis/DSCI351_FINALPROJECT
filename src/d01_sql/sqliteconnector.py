import os
import sqlite3
from sqlite3 import Error
from os import path 


#Creates database, and connection 
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")
        return conn
    except Error as e:
        print(e)

    return conn


#call to create different tables 
def create_table(conn, create_table_sql):
    #establishing connection and cursor 
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


        
def create_database(dbpath):

    # if (path.exists(dbpath)):
    #     print('Database exists!') 
    
    #parent table, company info 
    sql_company_info_table = """ CREATE TABLE IF NOT EXISTS company (
                                        id integer ,
                                        ticker text NOT NULL,
                                        name text NOT NULL,
                                        market text NOT NULL,
                                        city text NOT NULL,
                                        PRIMARY KEY(id)
                                    ); """

    sql_financial_info_table = """CREATE TABLE IF NOT EXISTS financialinformation (
                                    id integer ,
                                    currency text NOT NULL,
                                    market_cap integer,
                                    average_volume_traded integer,
                                    fifty_two_wk_high decimal,
                                    fifty_two_wk_low decimal,
                                    current_price decimal,
                                    fifty_two_wk_change decimal,
                                    divident_yield decimal,
                                    FOREIGN KEY (id) REFERENCES company (id)
                                );"""

    sql_timeseries_info_table = """CREATE TABLE IF NOT EXISTS security_price (
                        id integer,
                        Date text NOT NULL,
                        Open decimal NOT NULL,
                        High decimal NOT NULL,
                        Low decimal NOT NULL,
                        Close decimal NOT NULL,
                        Volume decimal NOT NULL,
                        adj_close decimal NOT NULL,
                        returns decimal NOT NULL,
                        cumulative_returns decimal NOT NULL,
                        FOREIGN KEY (id) REFERENCES company (id)
                    );"""
    
    # create a database connection
    conn = create_connection(dbpath)
    # print('Database Connection Created!')

    # create tables
    if conn is not None:
        # create company parent table
        create_table(conn, sql_company_info_table)

        # create financial info table
        create_table(conn, sql_financial_info_table)
        
        # create ts info table
        create_table(conn, sql_timeseries_info_table)
        
    else:
        print("Error! cannot establish the database connection. Try again.") #some error to know 


    return conn 
