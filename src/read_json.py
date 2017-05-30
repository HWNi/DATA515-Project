import json

def read_json(filename):

    """
    A function read the json file and process the Neighborhoods and Coordinates

    Parameter: filename, a json file)

    Return: result, a dictionary contains
            key: neighborhood,
            value: a list of coordinate corresponding to the that neighborhood
    """

    with open(filename) as f:
        data = json.load(f)

    result = {}
    for feature in data['features']:
        # NATName = Neighborhood Tabulation Area Name
        result[feature['properties']['NTAName']] = feature['geometry']['coordinates']

    return result