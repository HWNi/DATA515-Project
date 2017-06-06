import pandas as pd

def split_uber_data(filename):
    """
    A function split the data/time of Uber data set.

    Parameter: Uber data file, month
    """
    df = pd.read_csv(filename, sep=',', header=0)

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
    df.to_csv("split_" + filename, index=False)


def split_taxi_data(filename):
    """
    A function split the data/time of Uber data set.

    Parameter: taxi data file, month
    """
    df = pd.read_csv(filename, sep=',', header=0)

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
    df.to_csv("split_" + filename, index=False)