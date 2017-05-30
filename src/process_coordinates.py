# result = {"Borough Park" : [[lat1, lon1], [lat2, lon2], ...]}

"""
polygons =
{
"Borough Park" : {Lat : [], Lon : []}
"East Flushing" : {Lat : [], Lon : []}
"Auburndale" : {Lat : [], Lon : []}
.
.
.
"Elmhurst" : {Lat : [], Lon : []}
}
"""

def process_coordinates(result):
    """
    A function read the dictionary contains

    key: neighborhood
    value: list of coordinates (latitude, longitude)

    and reconstruct a new dictionary contains
    key: neighborhood
    value: a dictionary contains a list of latitudes and a list of longitudes.

    Parameter: result dictionary, contains neighborhoods and list of coordinates

    Return: polygon dictionary, contains neighborhoods
            and a list of latitudes and a list of longitudes
    """

    polygons = {}

    # for neighborhood, coordinates in result.items():
    for neighborhood in result.keys():

        coordinates = result[neighborhood]

        lat_list = []
        lon_list = []

        for coordinate in coordinates:
            lat_list.append(coordinate[1])
            lon_list.append(coordinate[0])
        polygons[neighborhood] = {}
        polygons[neighborhood]["Lat"] = lat_list
        polygons[neighborhood]["Lon"] = lon_list

    return polygons