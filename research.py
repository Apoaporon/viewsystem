import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('tasktask.csv', index_col=0)


app.layout = html.Div([
    # 見出しを作ります

    # 2つ目のDiv
    html.Div([

        # 2つ目のDivのなかにDivがありますDiv2-1と命名
        html.Div([
            # グラフを作成したい
            dcc.Graph(
                id='scatter-chart',
                # ここを余裕があれば、selectedData？にして複数グループセレクトしたい
                hoverData={'points': [{'customdata': 'group1'}]},

            ),
            # スライダーを作成する（余裕があれば、ドロップダウンにしたい）
            dcc.Slider(
                id='slider-one',
                min=df['ep'].min(),
                max=df['ep'].max(),
                marks={i: '{}'.format(i) for i in range(
                    int(df['ep'].min()), int(df['ep'].max() + 1))},

            )

        ],
            # Div2-1のスタイルを決める
            style={
            'display': 'inline',
            'width': '60%',
        }

        ),  # Div2-1の終わり
        # 2つ目のDivのなかにDivがありますDiv2-2と命名
        html.Div([
            dcc.Graph(id='chart-one'),
            dcc.Graph(id='chart-two'),
            dcc.Graph(id='chart-three'),
        ],
            # Div2-2のスタイルを決定
            style={
            'display': 'inline-block',
            'width': '30%',
            'height': '300'
        }
        )  # Div2-2の終わり




    ])  # 2つ目のDivの終わり



])  # 1つ目のDivの終わり

# コールバックを作成する（アプリに動きを加える）


@app.callback(
    # 出力先を決定
    dash.dependencies.Output("scatter-chart", 'figure'),
    # 入力先を決定
    [dash.dependencies.Input('slider-one', 'value')]
)
# 関数を作るよ(でかいグラフについての関数にしたい)
def update_graph(selected_ep):
    dff = df[df['ep'] == selected_ep]
    print(dff)

    dff1 = dff['group']

    dff2 = dff['rubric']

    """
    ここはどーするか考えなければいけません
    dffchar1 = dff[dff['text'] == 'text']
    dffchar2 = dff[dff['tex_diff'] == 'text_diff']
    dffchar3 = dff[dff[''] == 'text']
    """
    return{
        'data': [go.Scatter(
            x=dff1,
            y=dff2,
            mode='markers',
            customdata=[i],
            marker={
                'color': df['class'],
                'size':df['text'] / 40,
                'showscale': True,
            },
            name=i,
        )
            for i in dff.group.unique()

        ],
        'layout': {
            'height': 500,
            'xaxis': {
                'title': 'グループナンバー'
            },
            'yaxis': {
                'title': 'ルーブリックの得点'
            },
            'hovermode': 'closest',

        }
    }

# 小さいグラフを指定していくよ


def create_smallChart(df, group):
    print(df)
    return{
        'data': [go.Bar(
            x=df['ep'],
            y=df['rubric']
        )],
        'layout': {
            #'height': 250,
            'title': '{}のデータ'.format(group)
        }
    }


def create_smallChart1(df, group):
    print(df)
    return{
        'data': [go.Scatter(
            x=df['ep'],
            y=df['rubric']
        )],
        'layout': {
            #'height': 250,
            'title': '{}のデータ'.format(group)
        }
    }


def create_smallChart2(df, group):
    print(df)
    return{
        'data': [go.Scatter(
            x=df['ep'],
            y=df['text_diff']
        )],
        'layout': {
            #'height': 250,
            'title': '{}のデータ'.format(group)
        }
    }

# コールバックを作るよ


@app.callback(
    # 出力先を決めるよ
    dash.dependencies.Output('chart-one', 'figure'),
    # 入力先を決めるよ
    [(dash.dependencies.Input('scatter-chart', 'hoverData'))]
)
def createRubric1(hoverdata):
    groupName = hoverdata['points'][0]['customdata']
    dff = df[df['group'] == groupName]
    print(dff)
    return create_smallChart(dff, groupName)


@app.callback(
    # 出力先を決めるよ
    dash.dependencies.Output('chart-two', 'figure'),
    # 入力先を決めるよ
    [(dash.dependencies.Input('scatter-chart', 'hoverData'))]
)
def createRubric2(hoverdata):
    groupName = hoverdata['points'][0]['customdata']
    dff = df[df['group'] == groupName]
    print(dff)
    return create_smallChart1(dff, groupName)


@app.callback(
    # 出力先を決めるよ
    dash.dependencies.Output('chart-three', 'figure'),
    # 入力先を決めるよ
    [(dash.dependencies.Input('scatter-chart', 'hoverData'))]
)
def createRubric3(hoverdata):
    groupName = hoverdata['points'][0]['customdata']
    dff = df[df['group'] == groupName]
    print(dff)
    return create_smallChart2(dff, groupName)

if __name__ == "__main__":
    app.run_server(debug=True)
