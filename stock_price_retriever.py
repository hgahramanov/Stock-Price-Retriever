import pandas as pd
import numpy as np
import matplotlib
import pandas_datareader.data as web
import os.path
from os import path
import datetime as dt

class price_retriever():
    def __init__(self, stock_name):
        self.stock_name = stock_name

    def retrieve(self):
        df = web.DataReader(self.stock_name, 'yahoo', dt.datetime(1970,1,1))
        df.to_csv(self.stock_name + '.csv')
        df = pd.read_csv(self.stock_name + '.csv', parse_dates = True, index_col = 0)
        return df
        
tsla = price_retriever('TSLA').retrieve()
print(tsla.head())
amzn = price_retriever('AMZN')
amzn = amzn.retrieve()
print(amzn.head())
#print(dt.datetime(2000, 1, 1))