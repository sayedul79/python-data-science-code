# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 14:22:26 2021

@author: Sayedul 
"""
import numpy as np

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.layouts import row, column

N=300
x=np.linspace(0, 6*np.pi, N)
y=np.cos(x)
source=ColumnDataSource(data=dict(x=x, y=y))

p=figure(plot_width=600, plot_height=300, 
         title="Cosine function", 
         x_range=(0, 6*np.pi), 
         y_range=(-2, 2))
p.line("x", "y", source=source, color="red", 
       line_width=2)
p.title.align="left"
p.title.text_color="Orange"
p.title.text_font_size="25px"
p.title.text_font="ecotype"

text=TextInput(title="Set figure title",
               value="Cosine function")
amplitude=Slider(title="Amplitude",
                 start=1, 
                 end=10, 
                 value=1, 
                 step=1)
frequency=Slider(title="Frequency", 
                 start=1, 
                 end=5.1, 
                 step=0.1, 
                 value=1)
phase=Slider(title="Phase angle (radian)", 
             start=0, 
             end=2*np.pi, 
             step=0.1, 
             value=0)
offset=Slider(title="Offset", 
              start=-5, 
              end=5, 
              step=0.1, 
              value=0)

#callback
def text_update(attr, old, new):
    p.title.text=text.value
text.on_change("value", text_update)

def update_data(attr, old, new):
    a=amplitude.value
    f=frequency.value
    w=phase.value
    b=offset.value
    x=np.linspace(0, 6*np.pi, N)
    y=a*np.cos(f*x+w)+b
    source.data=dict(x=x, y=y)

for update in [amplitude, frequency, phase, offset]:
    update.on_change("value", update_data)
    
inputs=column(text, amplitude, frequency, phase, offset)
curdoc().add_root(row(inputs, p, width=800))
curdoc().title = "Sliders"
