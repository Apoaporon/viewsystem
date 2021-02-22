import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import json


div_style = {
    "height": "700px",
    "width": "90%",
    "margin": "auto",

}

div_style1 = {
    "height": "400px",
    "width": "45%",
    "margin": "1.5%",
    'display': 'inline-block',
    "backgroundColor": "skyblue"
}

# スタイルシートの読み込み
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('システムデータ1.csv', index_col=0)
df1 = pd.read_csv('tasktask.csv', index_col=0)

ep_options = []
for ep in df['ep'].unique():
    ep_options.append({'label': str(ep), 'value': ep})


print(ep_options)


app.layout = html.Div(
    [
        html.H1("グループワークを分析します"),

        html.Div(
            [
                dcc.Graph(
                    id='scatter-chart',
                    # hoverData='group',
                    hoverData={'points': [{'customdata': 'Group10'}]},

                ),
                dcc.Dropdown(
                    id='Dropdown',
                    options=ep_options,
                    value=df['ep'].min(),
                ),

            ],
            # style=div_style,
            id="first_leader",
        ),
        html.Div(
            [
                dcc.Graph(id='chart-one', style=div_style1),
                dcc.Graph(id='chart-two', style=div_style1),
                #dcc.Graph(id='chart-three', style=div_style1),

            ],

        ),
    ]

)


@app.callback(
    dash.dependencies.Output("scatter-chart", 'figure'),
    [dash.dependencies.Input('Dropdown', 'value')]
)
def update_graph(selected_ep):
    dff = df[df['ep'] == selected_ep]

    dff_class = dff[dff['item'] == 'class']
    dff_rubric = dff[dff['item'] == 'rubric']
    color_box = []
    for j in dff_class.value.unique():
        color_box.append(j)
        print(color_box)

    return{
        'data': [go.Scatter(
            x=dff_class[dff_class['group'] == i]['group'],
            y=dff_rubric[dff_rubric['group'] == i]['value'],
            mode='markers',
            customdata=[i],
            marker={

                #'color': dff_class[dff_class['group'] == i]['value'],
                #'color': df1['class'],
                'size': dff_rubric[dff_rubric['group'] == i]['value'] * 2,
                #'showscale': True
            },
            name=i,

        )
            for i in dff_class.group.unique()


        ],
        'layout': {
            'xaxis': {'title': 'グループナンバー'},
            'yaxis': {'title': 'ルーブリックの得点'},
            'hovermode': 'closest',
            "margin": "auto",
        }
    }


def create_small(dff, data1, data2):
    return{
        'data': [go.Scatter(
            x=dff['ep'].unique(),
            y=dff['value']
        )],
        'layout': {
            'titel': '{}の{}データ'.format(data1, data2)

        }

    }


@app.callback(
    dash.dependencies.Output('chart-one', 'figure'),
    [(dash.dependencies.Input('scatter-chart', 'hoverData'))]
)
def create_Rubric(hoverdata):
    groupName = hoverdata['points'][0]['customdata']
    dff = df[df['group'] == groupName]
    dff = dff[dff['item'] == 'rubric']
    return create_small(dff, groupName, 'ルーブリックの得点')


if __name__ == "__main__":
    app.run_server(debug=True)
