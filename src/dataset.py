import os
import pandas as pd
import  constants

data = pd.read_csv('../data/vocgroup.csv',na_filter=False)
meaning = [item for item in data['Unnamed: 0'] if item!='']
words = [item.split() for item in data['Unnamed: 1'] if item!='']