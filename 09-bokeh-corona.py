# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 21:39:00 2021

@author: Sayedul
"""
import pandas as pd

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import column

raw=pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
raw_melt=pd.melt(raw, id_vars=['Province/State', 'Country/Region', 'Lat', 
                             'Long'], var_name='date', 
                value_name='confirmed_case')
raw_melt["date"]=pd.to_datetime(raw_melt.date)
df=pd.pivot_table(raw_melt, index="date", columns="Country/Region", 
                  values="confirmed_case",
                  aggfunc='sum')
df=df.diff().dropna()
bangladesh=pd.DataFrame(df.Bangladesh).reset_index()
source=ColumnDataSource(dict(date=bangladesh.date, daily_case=bangladesh.iloc[:,-1]))

country_list=df.columns.tolist()

p=figure(plot_width=600, plot_height=300, x_axis_type="datetime", 
         sizing_mode="stretch_both")
p.line(x="date", y="daily_case", source=source, color="DarkBlue", 
      line_width=2)
select=Select(title="Country", options= country_list, 
              value="Bangladesh", background="orange")

def update_data(attr, old, new):
    desired_country=select.value
    source_data=pd.DataFrame(df[desired_country]).reset_index()
    source.data=dict(date=source_data.date, daily_case=source_data.iloc[:,-1])

select.on_change("value", update_data)
inputs=column(select, p)
curdoc().add_root(inputs)





