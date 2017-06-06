import json


def read_json(filename):
    """
    A function read the json file and process the Neighborhoods and Coordinates

    Parameter: filename, a json file)

    Return: result, a dictionary contains
            key: Neighborhood,
            value: a list of coordinate corresponding to the that neighborhood
    """

    with open(filename) as f:
        data = json.load(f)

    result = {}
    for feature in data['features']:

        # NATName = Neighborhood Tabulation Area Name

        neighborhood = feature['properties']['NTAName']
        coordinates = feature['geometry']['coordinates'][0]  # 3 layers or 2 layers

        if len(coordinates[0]) > 2:
            # 3 layers
            coordinates = coordinates[0]

        result[neighborhood] = coordinates

    return result