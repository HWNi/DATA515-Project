import numpy as np
import pandas as pd
from random import sample

taxi_path = ['C:\\Users\\HAOWEN-PC\\Desktop\\yellow_tripdata_2014-04.csv',
            'C:\\Users\\HAOWEN-PC\\Desktop\\yellow_tripdata_2014-05.csv',
            'C:\\Users\\HAOWEN-PC\\Desktop\\yellow_tripdata_2014-06.csv',
            'C:\\Users\\HAOWEN-PC\\Desktop\\yellow_tripdata_2014-07.csv',
            'C:\\Users\\HAOWEN-PC\\Desktop\\yellow_tripdata_2014-08.csv',
            'C:\\Users\\HAOWEN-PC\\Desktop\\yellow_tripdata_2014-09.csv']

uber_path = ['C:\\Users\\HAOWEN-PC\\Desktop\\apr_time.csv',
            'C:\\Users\\HAOWEN-PC\\Desktop\\may_time.csv',
            'C:\\Users\\HAOWEN-PC\\Desktop\\jun_time.csv',
            'C:\\Users\\HAOWEN-PC\\Desktop\\jul_time.csv',
            'C:\\Users\\HAOWEN-PC\\Desktop\\aug_time.csv',
            'C:\\Users\\HAOWEN-PC\\Desktop\\sep_time.csv']

path = ''


month = 4
data = pd.read_csv(path)
# data = data.drop(data.columns[[0,2,7,8,9,10,11,12,13,14,15,16]], 1) # for clean taxi data
rand_index =  np.array(sample(range(len(data)), 10000)) # create random index
data_sample = data.iloc[rand_index] # get 10000 random rows from df

#data_sample.to_csv('C:\\Users\\HAOWEN-PC\\Desktop\\taxi_0'+str(month)+'_2014_sample.csv', index = False)
data_sample.to_csv('C:\\Users\\HAOWEN-PC\\Desktop\\uber_0'+str(month)+'_2014_sample.csv', index = False)