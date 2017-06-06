import pandas as pd
import os

def split_uber_data(file_name):
    """
    A function split the data/time of Uber data set.

    Parameter: Uber data file, month

    Return: True or False for unittest purpose
            True, the output file saved
            False, the output file fail to saved
    """

    df = pd.read_csv(file_name, sep=',', header=0)

    # process the Data/Time column
    time = pd.DatetimeIndex(df['Date/Time'])
    df['year'] = time.year
    df['month'] = time.month
    df['day'] = time.day
    df['dayofweek'] = time.dayofweek
    df['hour'] = time.hour
    df['minute'] = time.minute
    df['time'] = time.time

    # converts the data frame to csv file
    df.to_csv("split_" + file_name, index=False)

    # return True or False for unittest purpose
    if os.path.exists("split_" + file_name):
        return True
    else :
        return False


def split_taxi_data(file_name):
    """
    A function split the data/time of Uber data set.

    Parameter: taxi data file, month
    """
    df = pd.read_csv(file_name, sep=',', header=0)

    # process the Data/Time column
    time = pd.DatetimeIndex(df.icol(0))
    df['year'] = time.year
    df['month'] = time.month
    df['day'] = time.day
    df['dayofweek'] = time.dayofweek
    df['hour'] = time.hour
    df['minute'] = time.minute
    df['time'] = time.time

    # converts the data frame to csv file
    df.to_csv("split_" + file_name, index=False)

    # return True or False for unittest purpose
    if os.path.exists("split_" + file_name):
        return True
    else :
        return False
