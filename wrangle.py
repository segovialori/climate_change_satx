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
    df['year'] = df.index.year
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
    #get seasons
    df['season'] = df['month'].apply(get_seasons)
    #get decades
    df['decade'] = df['year'].apply(get_decades)
    #drop columns
    df.drop(columns=['city', 'country', 'latitude', 'longitude'], inplace=True)
    # Celcius to Fareheit (I can't read celcius :( )
    df.avg_temp = (df.avg_temp) * (1.8) + 32

    return df

#Function to get seasons
def get_seasons(month):
    if month >= 3 and month <= 5:
        return 'spring'
    elif month >= 6 and month <= 8:
        return 'summer'
    elif month >= 9 and month <= 11:
        return 'fall'
    else:
        return 'winter'

#Function to get decades
def get_decades(year):
    if year < 1830:
        return '1820s'
    elif year >= 1830 and year < 1840:
        return '1830s'
    elif year >= 1840 and year < 1850:
        return '1840s'
    elif year >= 1850 and year < 1860:
        return '1850s'
    elif year >= 1860 and year < 1870:
        return '1860s'    
    elif year >= 1870 and year < 1880:
        return '1870s'
    elif year >= 1880 and year < 1890:
        return '1880s'
    elif year >= 1890 and year < 1900:
        return '1890s'
    elif year >= 1900 and year < 1910:
        return '1900s'
    elif year >= 1910 and year < 1920:
        return '1910s'
    elif year >= 1920 and year < 1930:
        return '1920s'
    elif year >= 1930 and year < 1940:
        return '1930s'
    elif year >= 1940 and year < 1950:
        return '1940s'
    elif year >= 1950 and year < 1960:
        return '1950s'
    elif year >= 1960 and year < 1970:
        return '1960s'
    elif year >= 1970 and year < 1980:
        return '1970s'
    elif year >= 1980 and year < 1990:
        return '1980s'
    elif year >= 1990 and year < 2000:
        return '1990s'
    elif year >= 2000 and year < 2010:
        return '2000s'
    else:
        return '2010s'




def wrangle_satx():
    '''
    This function will acquire, prep, and clean the dataframe.
    '''
    df = clean_satx()
    return df
