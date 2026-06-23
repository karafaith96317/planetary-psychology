import ephem
import math

def calculate_transit_data(target_date, lat='41.4993', lon='-81.6944'):
    """
    Calculates the exact position of key celestial bodies for a given time and location.
    Coordinates default to the Northern Ohio sector.
    """
    # Initialize the primary observer
    kara = ephem.Observer()
    kara.lat = lat
    kara.lon = lon
    kara.date = target_date

    # Define the celestial bodies to track
    sun = ephem.Sun()
    moon = ephem.Moon()
    mars = ephem.Mars()

    # Compute positions relative to the observer's exact coordinate in spacetime
    sun.compute(kara)
    moon.compute(kara)
    mars.compute(kara)

    # Return key metrics (converting radians to degrees for easier system ingestion)
    return {
        'Sun_Altitude (deg)': math.degrees(sun.alt),
        'Moon_Illumination (%)': moon.phase,
        'Mars_Azimuth (deg)': math.degrees(mars.az)
    }

if __name__ == "__main__":
    # Establishing the temporal anchor for the test run
    anchor_timestamp = '1989/9/6 15:17:00'
    
    print(f"Initializing Planetary Engine...")
    print(f"Calculating coordinates for Observer at {anchor_timestamp} UTC\n")
    
    metrics = calculate_transit_data(anchor_timestamp)
    
    for metric, value in metrics.items():
        print(f"{metric}: {value:.2f}")
