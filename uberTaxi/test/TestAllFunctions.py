import unittest
from split_data import split_uber_data, split_taxi_data
from read_json import read_json
from process_coordinates import process_coordinates
from geo_convert import geo_forward, geo_reverse
from find_neighborhood import find_neighborhood
from check_points import point_inside_polygon


class TestAllFunctions(unittest.TestCase):


    def test_split_data(self):
        self.assertTrue(split_uber_data("test_uber.csv"), True) # fake file to test the function
        self.assertTrue(split_taxi_data("test_taxi.csv"), True) # fake file to test the function

    # def test_read_json(self):
    #     self.assertTrue()

    # def test_process_coordinates(self):
    #     self.assertTrue()


    # def test_geo_convert(self):
    #     self.assertTrue(geo_forward())
    #     self.assertTrue(geo_reverse())


    def test_find_neighborhood(self):
        result = {'Airport':[[1, 2], [2, 3]]}   # fake dictionary to test the function
        self.assertTrue(find_neighborhood(result, "test.csv"))

    def test_point_inside_polygon(self):
        self.assertTrue(point_inside_polygon(4, 3, [5, 5])) # fake points to test the function
        self.assertFalse(point_inside_polygon(6, 5, [5, 5])) # fake points to test the function

if __name__ == '__main__':
    unittest.main()