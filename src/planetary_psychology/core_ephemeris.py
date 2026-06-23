import ephem
import math
from datetime import datetime, timezone


def calculate_transit_data(target_date=None, lat="0", lon="0"):
    """
    Calculates public research ephemeris metrics for a given time and location.

    No private birth data or natal chart anchors are used.
    Default coordinates are neutral: 0 latitude, 0 longitude.
    """
    if target_date is None:
        target_date = datetime.now(timezone.utc).strftime("%Y/%m/%d %H:%M:%S")

    observer = ephem.Observer()
    observer.lat = lat
    observer.lon = lon
    observer.date = target_date

    sun = ephem.Sun()
    moon = ephem.Moon()
    mars = ephem.Mars()

    sun.compute(observer)
    moon.compute(observer)
    mars.compute(observer)

    return {
        "Sun_Altitude_deg": math.degrees(sun.alt),
        "Moon_Illumination_percent": moon.phase,
        "Mars_Azimuth_deg": math.degrees(mars.az),
    }


if __name__ == "__main__":
    demo_timestamp = datetime.now(timezone.utc).strftime("%Y/%m/%d %H:%M:%S")

    print("Initializing Planetary Psychology public ephemeris engine...")
    print(f"Calculating neutral observer metrics for {demo_timestamp} UTC\n")

    metrics = calculate_transit_data(demo_timestamp)

    for metric, value in metrics.items():
        print(f"{metric}: {value:.2f}")
