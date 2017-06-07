import unittest
from split_data import split_uber_data, split_taxi_data
from read_json import read_json
from process_coordinates import process_coordinates
from geo_convert import geo_forward, geo_reverse
from find_neighborhood import find_neighborhood
from check_points import point_inside_polygon


class TestAllFunctions(unittest.TestCase):
    """
    A unit test class to test our methods.
    """

    # a function test split_data method
    def test_split_data(self):
        self.assertTrue(split_uber_data("test_uber.csv"), True) # fake file to test the function
        self.assertTrue(split_taxi_data("test_taxi.csv"), True) # fake file to test the function

    # a function test read_json method
    def test_read_json(self):
        """
        read_json function returns a dictionary with
        Key: neighborhood
        Value: list of (latitude, longitude)

        We should expect to have 195 neighborhood in New York City
        """

        result = read_json("NYC_Shapes.json")
        neighborhood = [result.keys()]
        self.assertEqual(len(neighborhood), 195)

    # a function test process_coordinates method
    def test_process_coordinates(self):
        """
        process_coordinate function return a dictionary with
        Key: neighborhood
        Value: a inner dictionary { 'Lat' : [...], 'Lon' : [...] }

        For example polygon = { 'Airport' : { 'Lat' : [...], 'Lon' : [...] }, .... }

        We should expect the type of polygon is equal to the type of polygon['Airport']
        """

        polygons = process_coordinates("NYC_Shapes_Cleaned.json")
        self.assertEqual(type(polygons), type(polygons['Airport']))

    # a function test geo_forward and geo_reverse methods
    def test_geo_convert(self):
        api_key = "Apz4N0shxHlg9r_WGJBPvMl-oi8F26rnkGFsJXa7QlDlSa7CbzWcnAPMVtW3-JHJ"
        address = "4326 University Way NE, Seattle, WA 98105"
        latitude, longitude = geo_forward(address, api_key)
        self.assertEqual(latitude, 47.660424) and self.assertEqual(longitude, -122.312818)
        zipcode = geo_reverse(latitude, longitude, api_key)
        self.assertEqual(zipcode, 98105)

    # a function test find_neighborhood method
    def test_find_neighborhood(self):
        result = {'Airport':[[1, 2], [2, 3]]} # fake dictionary to test the function
        self.assertTrue(find_neighborhood(result, "test.csv"))

    # a function test point_inside_polygon method
    def test_point_inside_polygon(self):
        self.assertTrue(point_inside_polygon(4, 3, [5, 5])) # fake points to test the function
        self.assertFalse(point_inside_polygon(6, 5, [5, 5])) # fake points to test the function

if __name__ == '__main__':
    unittest.main()