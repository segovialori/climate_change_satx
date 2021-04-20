import numpy as np
import pandas as pd

# Acquire satx dataset
def get_satx():
    '''
    This function will change the GlobalLandTemperaturesByCity.csv
    downloaded from kaggle into a dataframe.
    '''
    df = pd.read_csv('GlobalLandTemperaturesByCity.csv')
    df = df[(df.City == "San Antonio")]
    return df

# Clean satx dataframe
def clean_satx():
    '''
    This function will take in the dataframe from get_satx() and 
    prepare the dataframe for EDA.  The following steps are used
    in this function to clean and prepare the dataframe
    - Reassign the dt object type column to be a datetime type
    - Sort rows by the date and then set the index as that date
    - make new columns for month and weekday
    - rename column names
    - fill nulls
    - convert celsius to fareheit 
    '''
    # Dataframe from get_satx
    df = get_satx()
    # Reassign the sale_date column to be a datetime type
    df.dt = pd.to_datetime(df.dt)
    # Sort rows by the date and then set the index as that date
    df = df.set_index("dt").sort_index()
    # Make new columns for month and weekday
    df['month'] = df.index.month
    df['weekday'] = df.index.day_name()
    #change column names
    df.rename(columns={
        "AverageTemperature": "avg_temp",
        "AverageTemperatureUncertainty": "avg_temp_uncertainty", 
        "City": "city", 
        "Country": "country", 
        "Latitude": "latitude", 
        "Longitude": "longitude"}, inplace=True)
    # Fill nulls
    #jan 1822
    df.at['1822-01-01', 'avg_temp'] = 10.2945
    df.at['1822-01-01', 'avg_temp_uncertainty'] = 2.959
    #feb 1822
    df.at['1822-02-01', 'avg_temp_uncertainty'] = 2.891
    df.at['1822-02-01', 'avg_temp'] = 11.775
    #march 1822
    df.at['1822-03-01', 'avg_temp_uncertainty'] = 2.696
    df.at['1822-03-01', 'avg_temp'] = 16.193
    #sep 1822
    df.at['1822-09-01', 'avg_temp_uncertainty'] = 1.909
    df.at['1822-09-01', 'avg_temp'] = 24.818
    #oct 1822
    df.at['1822-10-01', 'avg_temp_uncertainty'] = 2.170
    df.at['1822-10-01', 'avg_temp'] = 20.251
    #nov 1822
    df.at['1822-11-01', 'avg_temp_uncertainty'] = 2.573
    df.at['1822-11-01', 'avg_temp'] = 15.373
    #nov 1821
    df.at['1821-11-01', 'avg_temp_uncertainty'] = 2.573
    df.at['1821-11-01', 'avg_temp'] = 15.373
    #dec 1821
    df.at['1821-12-01', 'avg_temp_uncertainty'] = 2.999
    df.at['1821-12-01', 'avg_temp'] = 11.336
    #dec 1822
    df.at['1822-12-01', 'avg_temp_uncertainty'] = 2.999
    df.at['1822-12-01', 'avg_temp'] = 11.336

    # Celcius to Fareheit (I can't read celcius :( )
    df.avg_temp = (df.avg_temp) * (1.8) + 32

    return df

def wrangle_satx():
    '''
    This function will acquire, prep, and clean the dataframe.
    '''
    df = clean_satx()
    return df
