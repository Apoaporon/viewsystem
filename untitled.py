import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

# データの読み込み
tips = pd.read_csv("tasktask.csv", index_col=0)
# cssのサイトからレイアウトをとってくる
dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
# スタイルをあらかじめ決めておく
core_style = {"width": "50%", "height": "60%", "margin": "5 % auto"}
# Dashインスタンスを生成する
app = dash.Dash(__name__)
# レイアウトを作成する(Divはコンテンツを分割するときに使用する)
app.layout = html.Div(
    [
        html.Div([
            # H1は見出しです
            html.H1("3章から9章までのデータを可視化しています", style={"textAlign": "center"}),
            # 多分ドロップダウンの作成をこれでやっているはず
            dcc.Dropdown(
                # IDを追加する
                # id="my-dropdown",
                options=[
                    {"label": "ep3", "value": "3章"},
                    {"label": "ep4", "value": "4章"},
                    {"label": "ep8", "value": "8章"},
                    {"label": "ep9", "value": "9章"},
                ],
                # 初期値の設定かな？
                value="3章",
                style=core_style
            ),
            # グラフを作成するはず
            dcc.Graph(
                figure=px.scatter(tips, x="group", y="text_diff",
                                  size="task_text", color="class", size_max=60),
                # style=core_style,
            ),
            # スライダーの作成
            dcc.Slider(
                # id='slider-one',
                min=tips['ep'].min(),
                max=tips['ep'].max(),
                marks={i: '{}'.format(i) for i in range(
                    int(tips['ep'].min()), int(tips['ep'].max()))},
                # style=core_style,
            )
        ])

    ],
    # idの名前を追加する
    # id="all-components",
    style={
        'display': 'inline-block',
        'width': '60%',
    }

    html.Div([
        dcc.Graph(id='chart-one'),
        dcc.Graph(id='chart-two'),
        dcc.Graph(id='chart-three'),
    ], style={
        'display': 'inline-block',
        'width': '39%'
    })

)

# コールバックの作成はここから


if __name__ == "__main__":
    app.run_server(debug=True)
