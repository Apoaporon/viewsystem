import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import json

df = pd.read_csv('システムデータ1.csv', index_col=0)
df1 = pd.read_csv(
    '/Users/kawakamitatsuya/Documents/view_system/keizai-dash-master/data/longform.csv', index_col=0)
df2 = pd.read_csv('tasktask.csv', index_col=0)

dff = df1[df1['year'] == 1955]

# print(dff)

dffper = dff[dff['item'] == 'pergdp']

# print(dffper)

x = dffper[dffper['area'] == '北海道']['value']
# print(x)

DF = df[df['ep'] == 3]

dff_class = DF[DF['item'] == 'class']
# print(dff_class)
dff_rubric = DF[DF['item'] == 'rubric']
# print(dff_rubric)

for i in dff_class.value.unique():
    print(i)

a = dff_class[dff_class['group'] == 'Group1']['value']

# print(a)

DFF = DF['group']
print(DFF)
