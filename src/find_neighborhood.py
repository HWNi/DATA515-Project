import numpy as np
import pandas as pd
import pickle
import csv

from check_points import point_inside_polygon


def find_neighborhood(result, csv_file, month):
    """
    A function determines the coordinates belongs to which neighborhood.
    Add a new column 'neighborhood' to the given csv file, then output a new csv file.

    Parameter: result, a dictionary with key: neighborhood, value: (Lat, Lon) pairs
               csv_file, input csv file
               month, the month corresponding to the csv file
    """

    list_neighborhood = []

    with open(csv_file, 'r') as csv_input:
        reader = csv.reader(csv_input)
        # skip the headers
        next(reader, None)
        for row in reader:
            lat = float(row[2])     # Lat = row[2]
            lon = float(row[3])     # Lon = row[3]

            for neighborhood in result.keys():
                if point_inside_polygon(lon, lat, result[neighborhood]):
                    list_neighborhood.append(neighborhood)
                else:
                    list_neighborhood.append('NA')

    pickle.dump(list_neighborhood, open(month + '_neighborhood_column', 'wb'))
    neighborhood_list = pickle.load(open(month + '_neighborhood_column'), 'rb') # a list of neighborhood
    df = pd.read_csv(csv_file, sep=',', index_col=0)
    neighborhoods = np.asarray(neighborhood_list)
    df['neighborhood'] = neighborhoods


    df = df[df.neighborhood != 'NA']    # remove all the 'NA' rows

    # converts the data frame to csv file
    df.to_csv(month + "_neighborhood.csv")
