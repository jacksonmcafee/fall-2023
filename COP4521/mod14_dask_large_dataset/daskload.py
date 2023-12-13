"""
Name: Jackson McAfee 
Date: 12/4/2023
Assignment: Module 14: Dask Large Dataset 
Due Date: 12/3/2023 
About this project: This script loads and computes aggregates based on a passed file.
Assumptions: N/A
All work below was performed by Jackson McAfee
"""

import dask.dataframe as ddf
from dask.diagnostics import ProgressBar

# declare type dictionary
dtypes = {
    'ID': str,
    'Source': str,
    'Severity': int,
    'Start_Time': str,
    'End_Time': str,
    'Start_Lat': float,
    'Start_Lng': float,
    'End_Lat': float,
    'End_Lng': float,
    'Distance(mi)': float,
    'Description': str,
    'Street': str,
    'City': str,
    'County': str,
    'State': str,
    'Zipcode': str,
    'Country': str,
    'Timezone': str,
    'Airport_Code': str,
    'Weather_Timestamp': str,
    'Temperature(F)': float,
    'Wind_Chill(F)': float,
    'Humidity(%)': float,
    'Pressure(in)': float,
    'Visibility(mi)': float,
    'Wind_Direction': str,
    'Wind_Speed(mph)': float,
    'Precipitation(in)': float,
    'Weather_Condition': str,
    'Amenity': bool,
    'Bump': bool,
    'Crossing': bool,
    'Give_Way': bool,
    'Junction': bool,
    'No_Exit': bool,
    'Railway': bool,
    'Roundabout': bool,
    'Station': bool,
    'Stop': bool,
    'Traffic_Calming': bool,
    'Traffic_Signal': bool,
    'Turning_Loop': bool,
    'Sunrise_Sunset': str,
    'Civil_Twilight': str,
    'Nautical_Twilight': str,
    'Astronomical_Twilight': str,
}

filename = "US_Accidents_March23.csv"
df = ddf.read_csv(filename, dtype = dtypes)

with ProgressBar():
    # Wind Chill grouped by Temperature
    print(f"Wind_Chill Min grouped by Temperature\n", df.groupby(['Temperature(F)'])['Wind_Chill(F)'].min().compute())
    print(f"Wind_Chill Max grouped by Temperature\n", df.groupby(['Temperature(F)'])['Wind_Chill(F)'].max().compute())
    print(f"Wind_Chill Mean grouped by Temperature\n", df.groupby(['Temperature(F)'])['Wind_Chill(F)'].mean().compute())
