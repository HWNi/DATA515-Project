import json

def read_json(filename):

    """
    A function read the json file and process the Zipcodes and Coordinates

    Parameter: filename, a json file)

    Return: result, a dictionary contains
            key: zipcode,
            value: a list of coordinate corresponding to the that zipcode
    """

    with open(filename) as f:
        data = json.load(f)

    result = {}
    for feature in data['features']:
        result[feature['properties']['ZIPCODE']] = feature['geometry']['coordinates']

    for zipcode, coor in result.items():
        print("Zipcode {}, Coordinate {}".format(zipcode, coor))

    return result