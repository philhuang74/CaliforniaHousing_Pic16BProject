import os, shutil, matplotlib
import pandas as pd
from fbprophet import Prophet
from os import listdir
from os.path import isfile, join

def create_figures(df):
    matplotlib.use('Agg')
    # save the figures in a folder names "figures"
    save_folder = os.path.join(os.path.dirname(__file__),"static/figures")
    if os.path.exists(save_folder):
            shutil.rmtree(save_folder)
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    filter_col = [col for col in df if col.startswith('X')]
    dfT=df[filter_col]
    for i in list(dfT.T.keys()):
        dfT.T[i].to_frame()
        inp = dfT.T[i].to_frame(name="y")
        inp["ds"]=inp.index
        inp=inp[["ds","y"]]
        inp["ds"] = inp["ds"].str.extract(r'(\d+.\d+.\d+)')
        inp["ds"]=pd.to_datetime(inp["ds"], infer_datetime_format=True)
        m = Prophet(weekly_seasonality=True, growth='linear',yearly_seasonality=0.0000001)
        m.add_seasonality(name='daily', period=1, fourier_order=2)
        m.fit(inp)
        future = m.make_future_dataframe(periods=365)
        forecast = m.predict(future)
        fig = m.plot(forecast)
        fig.gca().set_ylabel("Housing Price (in USD) for Zip Code: " + str(df["Zip"][i]))
        fig.gca().set_xlabel("Time (in year)")
        fig.savefig(os.path.join(save_folder,"figure"+str(i)+".png"),bbox_inches='tight')
    return [join("../static/figures",f) for f in listdir(save_folder) if isfile(join(save_folder, f))]