# ******************************************************************************
#  * FILE NAME: create_figures.py
#  * INPUT: a pandas dataframe based on Final_data_set.csv (the housing dataset)
#  * OUTPUT: a list of tuples in the following format:
#  *            (zip code, .png image data in bytes)
#  * DESCRIPTION: This python script includes a create_figures function that
#  *              uses the "Zip" (Code) column of the housing dataframe to
#  *              extract and return the corresponding zip codes and figures
#  *              of the housing trend plots in bytes.
#  ******************************************************************************

import sqlite3, base64
from os.path import join, dirname, realpath

def create_figures(df):
    # create an empty list that will contain (zip code, .png image data in bytes) tuples
    zip_figures = []

    # connect to the figures1.db and figures2.db databases in the figures folder
    conn1 = sqlite3.connect(join(dirname(realpath(__file__)),"figures/figures1.db"))
    conn2 = sqlite3.connect(join(dirname(realpath(__file__)),"figures/figures2.db"))

    # create cursor objects to execute SQL commands
    cursor1 = conn1.cursor()
    cursor2 = conn2.cursor()

    # extract all the zip codes from the dataframe
    zip_codes = tuple([int(df["Zip"][k]) for k in list(df.T.keys())])

    # SQL query the figures that correspond to the zip codes
    sql_query = """SELECT * FROM figure_table WHERE zip_code IN {0}""".format(zip_codes)
    data1 = cursor1.execute(sql_query)
    data2 = cursor2.execute(sql_query)

    # find the index of the zip code and figure columns in the database
    column_names = [description[0] for description in data1.description]
    figure_index = column_names.index("figure")
    zip_code_index = column_names.index("zip_code")

    # append (zip code, .png image data in bytes) tuples to the zip_figures list
    for x in data1.fetchall():
        zip_figures.append((x[zip_code_index], base64.b64encode(x[figure_index]).decode("utf-8")))
    for x in data2.fetchall():
        zip_figures.append((x[zip_code_index], base64.b64encode(x[figure_index]).decode("utf-8")))
    
    # save (commit) the changes
    conn1.commit()
    conn2.commit()
    
    # close the cursor objects
    cursor1.close()
    cursor2.close()
    
    # close the connections
    conn1.close()
    conn2.close()

    # return the list of (zip code, .png image data in bytes) tuples
    return zip_figures