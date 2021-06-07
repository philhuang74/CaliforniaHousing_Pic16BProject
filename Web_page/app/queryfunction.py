# ******************************************************************************
#  * FILE NAME: queryfunction.py
#  * DESCRIPTION: This python script includes a query_function function that
#  *              returns a pandas dataframe of Final_data_set.csv based on
#  *              the answers submitted in the questionarie form in ask.html
#  ******************************************************************************

import pandas as pd
import os
def query_function(Q1_ans,Q2_ans,Q3_ans,Q4_ans,Min_ans,Max_ans):
    """
    :param Q1_ans (int): care for population density (scale: 0-5)
    :param Q2_ans (int): care for crime rate (scale: 0-5)
    :param Q3_ans (int): care for public high school ranking (scale: 0-5)
    :param Q4_ans (int): Northern California (1), Southern California (2)
    :param Min_ans (int/float): minimum budget
    :param Max_ans (int/float): maximum budget
    :return: a pandas dataframe based on Final_data_set.csv (the housing dataset)
    """
    # Read in Dataset
    data = pd.read_csv(os.path.join(os.path.dirname(__file__),'Final_data_set.csv'))
    data1 = data

    # Sort Based on User Inputs
    if Q1_ans== 0:
        data1 = data1
    else:
        data1 = data1[data1.label_density == Q1_ans]


    if Q1_ans == 0:
        data1 = data1
    else:
        data1 = data1[data1.crime_rate == Q2_ans]


    if Q1_ans == 0:
        data1 = data1
    else:
        data1 = data1[data1.crime_rate <= Q3_ans]


    separation_lat = 35 # THIS IS THE LATITUDE THAT SEPERATES CALIFORNIA INTO NORTH AND SOUTH
    if Q4_ans == 1:
        data1 = data1[data1.Latitude >= separation_lat]
    if Q4_ans == 2:
        data1 = data1[data1.Latitude <= separation_lat]

    # filter based on minimum/maximum budget
    data1 = data1[data1['X2021.03.31'] <= Max_ans]
    data1 = data1[data1['X2021.03.31'] >= Min_ans]

    #only return the necessary info for users
    data1 = data1[['County','Zip','City_x','Population_density','Crime_rate_Per1000',
                  'Latitude','Longitude','X2021.03.31']]
    return data1

# Unit Test
# query_function(int("3"),int("2"),int("4"),int("2"),int("100"),int("100000000"))
