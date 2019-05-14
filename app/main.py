import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import json
import requests

external_stylesheets = [dbc.themes.BOOTSTRAP]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Iris data set playground!'),

    html.Div(children='''
        This is simple playground for calling a logistic regression model trained on the Iris data set through a REST api developed using Flask.
    '''),
    dbc.Row([
        dbc.Col([
            dbc.FormGroup([
                dbc.Label('Sepal length (cm)'),
                dcc.Slider(id='sepal-length-slider',
                           min=4.3,
                           max=7.9,
                           step=1e-1,
                           value=5),
            ]),
            html.Br(),
            dbc.FormGroup([
                dbc.Label('Sepal width (cm)'),
                dcc.Slider(id='sepal-width-slider',
                           min=2,
                           max=4.4,
                           step=1e-1,
                           value=2.5)
            ]),
            html.Br(),
            dbc.FormGroup([
                dbc.Label('Petal length (cm)'),
                dcc.Slider(id='petal-length-slider',
                           min=1,
                           max=6.9,
                           step=1e-1,
                           value=4.3)
            ]),
            html.Br(),
            dbc.FormGroup([
                dbc.Label('Petal width (cm)'),
                dcc.Slider(id='petal-width-slider',
                           min=0.1,
                           max=2.5,
                           step=1e-1,
                           value=1.1)
            ])
        ], align='center', md=3),
        dbc.Col(
            dcc.Graph(
                id='predictions-graph',
                figure={
                    'data': [
                        {'x': ['Setosa', 'Versicolor', 'Virginica'], 'y': [0, 0, 0], 'type': 'bar',
                         'name': 'Class probabilities'},
                    ],
                    'layout': {
                        'title': 'Class probability',
                        'yaxis': {'range':[0,1]}
                    }
                }
            )
        )
    ])
])

@app.callback(Output('predictions-graph','figure'),
              [Input('sepal-length-slider', 'value'), Input('sepal-width-slider', 'value'),
               Input('petal-length-slider', 'value'), Input('petal-width-slider', 'value')])
def update_figure(sepal_length, sepal_width, petal_length, petal_width):
    payload = [{'sepal length (cm)': sepal_length,
                'sepal width (cm)': sepal_width,
                'petal length (cm)': petal_length,
                'petal width (cm)': petal_width}
               ]
    res = requests.post('http://irisrest.azurewebsites.net/predict?key=a7444d96',
                        json=json.dumps(payload))
    json_ = res.json()

    figure = {
                'data': [
                    {'x': ['Setosa', 'Versicolor', 'Virginica'], 'y': json_['prediction'][0], 'type': 'bar',
                     'name': 'Setosa',
                     'marker': {
                         'color': ['rgba(200,0,0,1)', 'rgba(0,200,0,1)', 'rgba(0,0,200,1)']
                     }}
                ],
                'layout': {
                    'title': 'Class probability',
                    'yaxis': {'range': [0, 1]}
                },

            }

    return figure



if __name__ == '__main__':
    app.run_server(debug=False, port=80, host='0.0.0.0')