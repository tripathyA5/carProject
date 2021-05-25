import pandas as pd
import csv
import plotly.figure_factory as ff
df=pd.read_csv('carData.csv')
fig=ff.create_distplot([df['Avg Rating']],['Average Rating'])
fig.show()