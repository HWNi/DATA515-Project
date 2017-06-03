import numpy as np
import pandas as pd
import pickle
import csv

from check_points import point_inside_polygon


def find_neighborhood(result, csv_file):
    """
    A function determines the coordinates belongs to which neighborhood.
    Add a new column 'neighborhood' to the given csv file, then output a new csv file.

    Parameter: result, a dictionary with key: neighborhood, value: (Lat, Lon) pairs
               csv_file, input csv file
               month, the month corresponding to the csv file
    """

    neighborhoods_list = []
    found = False
    with open(csv_file, 'r') as csv_input:
        reader = csv.reader(csv_input)

        # skip the headers
        next(reader, None)
        for row in reader:
            lat = float(row[4])  # Taxi, (row[4], row[3])
            lon = float(row[3])

            for neighborhood in result.keys():
                if point_inside_polygon(lon, lat, result[neighborhood]):
                    neighborhoods_list.append(neighborhood)
                    found = True
                    break
            if found == False:
                neighborhoods_list.append('NA')
            found = False

    df = pd.read_csv(csv_file, sep=',', index_col=0)
    neighborhoods = np.asarray(neighborhoods_list)
    df['neighborhood'] = neighborhoods

    # remove all the 'NA' rows
    df = df[df.neighborhood != 'NA']

    # converts the data frame to csv file
    df.to_csv("final_" + csv_file)
