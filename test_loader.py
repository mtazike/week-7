import unittest
from loader import *

class TestLoader(unittest.TestCase):

    def test_valid_locations(self):
        geolocator = get_geolocator()

        # Test Museum of Modern Art
        result = fetch_location_data(geolocator, "Museum of Modern Art")
        self.assertAlmostEqual(result["latitude"], 40.7618552, places=3)
        self.assertAlmostEqual(result["longitude"], -73.9774838, places=3)
        self.assertEqual(result["type"].lower(), "museum")

        # Test USS Alabama Battleship Memorial Park
        result2 = fetch_location_data(geolocator, "USS Alabama Battleship Memorial Park")
        self.assertAlmostEqual(result2["latitude"], 30.684373, places=3)
        self.assertAlmostEqual(result2["longitude"], -88.015316, places=3)
        self.assertEqual(result2["type"].lower(), "park")

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        # Expect NA or None values for invalid location
        self.assertIsNone(result["latitude"])
        self.assertIsNone(result["longitude"])
        self.assertEqual(result["type"], "NA")

if __name__ == "__main__":
    unittest.main()
