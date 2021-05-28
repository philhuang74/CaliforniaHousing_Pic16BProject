
def query_function(Q1_ans,Q2_ans,Q3_ans,Q4_ans,minb,maxb):
    #read in dataset
    data = pd.read_csv('Final_data_set.csv')
    data1 = data
    #sort based on user inputs

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


    data1 = data1[data1['X2021.03.31'] <= minb]
    data1 = data1[data1['X2021.03.31'] >= maxb]

    #only return the necessary info for users
    data1 = data1[['County','Zip','City_x','Population_density','Crime_rate_Per1000',
                  'Latitude','Longitude','X2021.03.31']]

    return data1
