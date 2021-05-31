# -*- coding: utf-8 -*-
"""
Created on Mon May 31 18:01:56 2021

@author: Sayedul
"""
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.layouts import layout
from bokeh.models import Div,Spinner,RangeSlider

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [4, 5, 5, 7, 2, 6, 4, 9, 1, 3]

output_file("first_steps.html")
p=figure(plot_width=600, plot_height=300, x_range=(1,9))
points=p.circle(x,y, color="firebrick")

div=Div(text=""" <p>Select the circle size using this control element</p>""", width=250, height=30)

spinner=Spinner(title="Circle size", low=0, high=40, value=points.glyph.size, step=4)
spinner.js_link("value",points.glyph, "size")

range_slider=RangeSlider(title="Adjust x-axis range", start=0, end=10, step=1, value=(p.x_range.start, p.x_range.end))
range_slider.js_link("value", p.x_range, "start", attr_selector=0)
range_slider.js_link("value", p.x_range, "end", attr_selector=1)

layout=layout([[div, spinner], [range_slider], [p]])
show(layout)       
