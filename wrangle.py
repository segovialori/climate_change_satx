import numpy as np
import pandas as pd

#acquire satx dataset
def get_satx():
    '''
    This function will change the GlobalLandTemperaturesByCity.csv
    downloaded from kaggle into a dataframe.
    '''
    df = pd.read_csv('GlobalLandTemperaturesByCity.csv')
    df = df[(df.City == "San Antonio")]
    return df

#clean satx dataframe
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
