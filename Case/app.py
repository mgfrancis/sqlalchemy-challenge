# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:02:53 2020

@author: opusm
"""
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from flask import Flask

#%%

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn = engine.connect()

#%%

app = Flask(app)

#%%

@app.route('/api/v1.0/precipation')

def prcp:
    
    prcp_query = f'''
    
        select date, prcp from measurement 
        where prcp <> 0.00 
        and date between 
            (select date(max(date), '-12 month') from measurement) 
            and (select max(date) from measurement) 
            order by date desc
     '''

    #save the query results as a Pandas DataFrame and set the index to the date column

    prcp_data = pd.read_sql(prcp_query, conn)

    #Load the query results into a Pandas DataFrame and set the index to the date column.

    #Sort the DataFrame values by `date`.

    prcp_df = pd.DataFrame(prcp_data)
    prcp_df = prcp_df.sort_values('date', ascending=True)
    prcp_df = prcp_df.set_index('date')
       


