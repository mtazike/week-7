import unittest
from loader import *

class TestLoader(unittest.TestCase):

    def test_valid_locations(self):
        geolocator = get_geolocator()

        # Test Museum of Modern Art
        result = fetch_location_data(geolocator, "Museum of Modern Art")
        self.assertIsNotNone(result, "Result should not be None")
        self.assertEqual(result["location"], "Museum of Modern Art")
        self.assertAlmostEqual(result["latitude"], 40.7618, places=2)
        self.assertAlmostEqual(result["longitude"], -73.9778, places=2)
        self.assertIn(result["type"].lower(), ["museum", "art", "building"])

        # Test USS Alabama Battleship Memorial Park
        result2 = fetch_location_data(geolocator, "USS Alabama Battleship Memorial Park")
        self.assertIsNotNone(result2, "Result should not be None")
        self.assertEqual(result2["location"], "USS Alabama Battleship Memorial Park")
        self.assertAlmostEqual(result2["latitude"], 30.6844, places=2)
        self.assertAlmostEqual(result2["longitude"], -88.0153, places=2)
        self.assertIn(result2["type"].lower(), ["park", "attraction", "museum"])

    def test_invalid_location(self):
        geolocator = get_geolocator()

        # Invalid address test
        result = fetch_location_data(geolocator, "asdfqwer1234")

        # Expect None or 'NA'
        self.assertIsNone(result["latitude"])
        self.assertIsNone(result["longitude"])
        self.assertEqual(result["type"], "NA")
        self.assertEqual(result["location"], "asdfqwer1234")

if __name__ == "__main__":
    unittest.main()
