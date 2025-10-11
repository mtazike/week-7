import unittest
import pandas as pd
from loader import *

class TestLoader(unittest.TestCase):

    def test_valid_locations(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "New York")

        # Check that latitude and longitude are not None for a valid place
        self.assertIsNotNone(result["latitude"], "Latitude should not be None for a valid location.")
        self.assertIsNotNone(result["longitude"], "Longitude should not be None for a valid location.")

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        # Expect latitude to be None for an invalid location
        self.assertIsNone(result["latitude"], "Latitude should be None for an invalid location.")

if __name__ == "__main__":
    unittest.main()
