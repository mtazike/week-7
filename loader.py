'''
Script to load geographical data into a pandas DataFrame, and save it as a CSV file.
'''

from geopy.geocoders import Nominatim
import pandas as pd


def get_geolocator(agent='h501-student'):
    """
    Initiate a Nominatim geolocator instance given an `agent`.

    Parameters
    ----------
    agent : str, optional
        Agent name for Nominatim, by default 'h501-student'
    """
    return Nominatim(user_agent=agent)

def fetch_location_data(geolocator, loc):
    try:
        # Try to get the location (with a timeout)
        location = geolocator.geocode(loc, timeout=10)
    except Exception as e:
        # Handle timeout or other errors safely
        print(f"Error fetching location for '{loc}': {e}")
        return {
            "location": loc,
            "latitude": None,
            "longitude": None,
            "type": "NA"
        }

    # If location not found
    if location is None:
        return {
            "location": loc,
            "latitude": None,
            "longitude": None,
            "type": "NA"
        }

    # If found, return coordinates
    return {
        "location": loc,
        "latitude": location.latitude,
        "longitude": location.longitude,
        "type": location.raw.get("type", "NA")
    }



def build_geo_dataframe(geolocator, locations):
    geo_data = [fetch_location_data(geolocator, loc) for loc in locations]

    return pd.DataFrame(geo_data)


if __name__ == "__main__":
    geo = get_geolocator()

    locations = ["Museum of Modern Art", "Alaska", "Franklin's Barbecue", "Burj Khalifa"]

    df = build_geo_dataframe(geo, locations)
    print(df)

    df.to_csv("./geo_data.csv", index=False)
    print("geo_data.csv file created successfully!")

