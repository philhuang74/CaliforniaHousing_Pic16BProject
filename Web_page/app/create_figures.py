import sqlite3, base64
from os.path import join, dirname, realpath

def create_figures(df):
    figure_binaries = []
    conn1 = sqlite3.connect(join(dirname(realpath(__file__)),"figures/figures1.db"))
    conn2 = sqlite3.connect(join(dirname(realpath(__file__)),"figures/figures2.db"))
    cursor1 = conn1.cursor()
    cursor2 = conn2.cursor()
    filter_col = [col for col in df if col.startswith('X')]
    dfT=df[filter_col]
    keys = list(dfT.T.keys())
    zip_codes = tuple([int(df["Zip"][k]) for k in keys])
    sql_query = """SELECT * FROM figure_table WHERE zip_code IN {0}""".format(zip_codes)
    data1 = cursor1.execute(sql_query)
    data2 = cursor2.execute(sql_query)
    column_names = [description[0] for description in data1.description]
    figure_index = column_names.index("figure")
    for x in data1.fetchall():
        figure_binaries.append(base64.b64encode(x[figure_index]).decode("utf-8"))
    for x in data2.fetchall():
        figure_binaries.append(base64.b64encode(x[figure_index]).decode("utf-8"))
    conn1.commit()
    cursor1.close()
    conn1.close()
    conn2.commit()
    cursor2.close()
    conn2.close()
    return figure_binaries