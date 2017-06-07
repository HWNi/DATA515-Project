import json
import os
import pyodbc
from collections import defaultdict

import numpy as np
import pandas as pd

import bokeh.layouts
from bokeh.io import curdoc, output_file, show
from bokeh.layouts import widgetbox
from bokeh.models import (
    BoxSelectTool,
    Circle,
    ColumnDataSource,
    CustomJS,
    DataRange1d,
    GMapPlot,
    GMapOptions,
    HoverTool,
    LogColorMapper,
    PanTool,
    Slider,
    WheelZoomTool,
)
from bokeh.models.glyphs import Patches
from bokeh.models.widgets import Button, RadioButtonGroup, Select, CheckboxButtonGroup
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure

from bokeh.resources import CDN
from bokeh.embed import file_html

# Query the database, obtain the data that can be displayed on the heat map
server = 'dataproject.database.windows.net'
database = 'Data515Project'
username = 'uberandtaxinyc'
password = 'Lzcnhwzcylyw515!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

uber_statement = 'SELECT [neighborhood], [month],[day],[hour], count(*) as pick_up\
                 FROM [dbo].[uber_2014] \
                 GROUP BY [month], [day], [hour],[neighborhood] \
                 ORDER BY [month], [day], [hour],[neighborhood]'

cursor.execute(uber_statement)
row = cursor.fetchone()
uber_data = []
uber_data.append(row)
while row:
    print(row)
    row = cursor.fetchone()
    uber_data.append(row)

taxi_statement = 'SELECT [neighborhood], [month],[day],[hour], count(*) as pick_up \
                 FROM [dbo].[uber_2014] \
                 GROUP BY [month], [day], [hour],[neighborhood] \
                 ORDER BY [month], [day], [hour],[neighborhood]'

cursor.execute(taxi_statement)
row = cursor.fetchone()
taxi_data = []
taxi_data.append(row)
while row:
    print(row)
    row = cursor.fetchone()
    taxi_data.append(row)

# Prepare bokeh input data
def flatten(d):
    res = []  # Result list
    if isinstance(d, dict):
        for key, val in d.items():
            res.extend(flatten(val))
    elif isinstance(d, list):
        res = d
    else:
        raise TypeError("Undefined type for flatten: %s"%type(d))

    return res

uber_dic = defaultdict(list)
for neighborhood, month, day, hour, pick_up in uber_data:
    uber_dic[neighborhood][month][day][hour].append(pick_up)

taxi_dic = defaultdict(list)
for neighborhood, month, day, hour, pick_up in taxi_data:
    taxi_dic[neighborhood][month][day][hour].append(pick_up)



with open('~/Data515/DATA515-Project/data/NYC_Shapes_Cleaned.json') as f:
    data = json.load(f)
nyc_neighborhoods = data
len(nyc_neighborhoods)


# Develop bokeh heat map
palette.reverse()

color_mapper = LogColorMapper(palette=palette)

neighborhood_xs = [neighborhood["Lon"] for neighborhood in nyc_neighborhoods.values()]
neighborhood_ys = [neighborhood["Lat"] for neighborhood in nyc_neighborhoods.values()]

neighborhood_names = list(nyc_neighborhoods.keys())

# Warning
# It is critical to note that no python code is ever executed when a CustomJS callback is used.
# A CustomJS callback is only executed inside a browser JavaScript interpreter,
# and can only directly interact JavaScript data and functions (e.g., BokehJS Backbone models).
#
# Thoughts:
# Prepare the Uber pickup counts data, save them in to a matrix
# Dimensions: row number = month# * day#  * hour#  = 3*31*24 = 2232
#            column number = 195
#
uber_pickup = [flatten(uber_dic[neighborhood]) for neighborhood in neighborhood_names]
neighborhood_counts_uber = uber_pickup

taxi_pickup = [flatten(taxi_dic[neighborhood]) for neighborhood in neighborhood_names]
neighborhood_counts_taxi = taxi_pickup


indicators = ['Uber' for i in range(195)]

months = np.zeros(len(nyc_neighborhoods), dtype=int) + 4

days = np.zeros(len(nyc_neighborhoods), dtype=int) + 1

hours = np.zeros(len(nyc_neighborhoods), dtype=int)

# 0-based
# One month: 31*24 = 744 rows
# One day: 24 rows
#

# April: row 0-743 (0:744)
# Day: chunck size 31
# hour: chunck size 24
# May: row 744-1487 (744:1488)
# Jun: row 1488-end

# Example:month 5 day 12 hour 18
# index = 744*($5$-4) + 24*($12$-1) + $18$

# value = neighborhood_counts[744*(min(months)-4) + 24*(min(days)-1) + min(hours)]

source = ColumnDataSource(data=dict(
    x=neighborhood_xs,
    y=neighborhood_ys,
    name=neighborhood_names,

    indicator=indicators,
    month=months,
    day=days,
    hour=hours,

    values_uber=neighborhood_counts_uber,
    values_taxi=neighborhood_counts_taxi,
    value=neighborhood_counts_uber[0],
))

callback_month = CustomJS(args=dict(source=source), code="""
    var data = source.data;
    var month = month.value;

    idc = data['indicator'][0]
    m = month
    d = data['day'][0]
    h = data['hour'][0]

    for (i = 0; i < data['month'].length; i++) {
        data['month'][i] = month
    }

    if (idc == 'Uber') {
        values = data['values_uber']
        data['value'] = values[744*(m-4) + 24*(d-1) + h]
    } else {
        values = data['values_taxi']
        data['value'] = values[744*(m-4) + 24*(d-1) + h]
    }

    source.trigger('change');
""")

callback_day = CustomJS(args=dict(source=source), code="""
    var data = source.data;
    var day = day.value;

    idc = data['indicator'][0]
    m = data['month'][0]
    d = day
    h = data['hour'][0]

    for (i = 0; i < data['day'].length; i++) {
        data['day'][i] = day
    }

    if (idc == 'Uber') {
        values = data['values_uber']
        data['value'] = values[744*(m-4) + 24*(d-1) + h]
    } else {
        values = data['values_taxi']
        data['value'] = values[744*(m-4) + 24*(d-1) + h]
    }

    source.trigger('change');
""")

callback_hour = CustomJS(args=dict(source=source), code="""
    var data = source.data;
    var hour = hour.value;

    idc = data['indicator'][0]
    m = data['month'][0]
    d = data['day'][0]
    h = hour

    for (i = 0; i < data['hour'].length; i++) {
        data['hour'][i] = hour
    }

    if (idc == 'Uber') {
        values = data['values_uber']
        data['value'] = values[744*(m-4) + 24*(d-1) + h]
    } else {
        values = data['values_taxi']
        data['value'] = values[744*(m-4) + 24*(d-1) + h]
    }

    source.trigger('change');
""")

callback_indicator = CustomJS(args=dict(source=source), code="""
    var data = source.data
    var indicator = indicator.value

    for (i = 0; i < data['indicator'].length; i++) {
        data['indicator'][i] = indicator        
    }

    m = data['month'][0]
    d = data['day'][0]
    h = data['hour'][0]

    if (indicator == 'Uber') {
        values = data['values_uber']
        data['value'] = values[744*(m-4) + 24*(d-1) + h]   
    } else {
        values = data['values_taxi']
        data['value'] = values[744*(m-4) + 24*(d-1) + h]
    }

    source.trigger('change');  
""")

TOOLS = "pan,wheel_zoom,reset,hover,save"

plot = figure(title="Uber Pickup Distribution", tools=TOOLS,
              x_axis_location=None, y_axis_location=None)

plot.grid.grid_line_color = None

plot.patches('x', 'y', source=source,
              fill_color={'field': 'value', 'transform': color_mapper},
              fill_alpha=0.7, line_color="black", line_width=0.5)

hover = plot.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [
    ("Name", "@name"),
    ("(Long, Lat)", "($x, $y)"),
    ("Number of pickups", "@value"),
    ("Month", "@month"),
    ("Day", "@day"),
    ("Hour", "@hour")
]

map_select = Select(title="Map:", value='Uber', options=['Uber', 'Taxi'], callback=callback_indicator)
callback_indicator.args["indicator"] = map_select

month_select = Select(title="Month:", value='4', options=['4', '5', '6'], callback=callback_month)
callback_month.args["month"] = month_select

days = [str(i) for i in list(range(1,32))]
day_select = Select(title="Day:", value='1', options=days, callback=callback_day)
callback_day.args["day"] = day_select

hour_slider = Slider(start=0, end=23, step=1, value=0, title="Hour", callback=callback_hour)
callback_hour.args["hour"] = hour_slider

curdoc().clear()
final_plot = bokeh.layouts.row(plot, widgetbox(map_select, month_select, day_select, hour_slider, width=300))
show(final_plot)

Html_file= open("NYC_Uber_Taxi.html","w")
my_html = file_html(final_plot, CDN, "my plot")
Html_file.write(my_html)
Html_file.close()

