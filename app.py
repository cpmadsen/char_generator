from dash import Dash, dcc, html, Input, Output, callback
import pandas as pd

app = Dash(__name__)

scroll_header = html.Div([
    html.Img(src='/assets/scroll-horizontal.png', height = 200, width = 400)
])

app.layout = html.Div([
    scroll_header,
    html.Div(
        className="app-header",
        children=[
            html.Div(
                html.H2('Dungeons and Dragons Character Generation'), 
                className="app-header--title",
                style = {
                    ##'position': 'absolute',
                    'background-image': 'url("/assets/scroll-horizontal.png")', 
                    'background-height': 200,
                    'background-width': 400
                    }
                    ),
            dcc.Input(id='my-input', value = 1, type = 'number')
            ]
    ),
    html.Div(
        children=html.Div([
            html.H1('Output'),
            html.Div(id='my-output'),
            html.Div('''
                This is an example of a simple Dash app with
                local, customized CSS.
            ''')
        ])
    )
],
style = {
            'background-image': 'url("/assets/old_paper_background.png")',
            'background-repeat': 'no-repeat',
            'background-position': 'absolute',
            'background-size': '1920px 1080px'
        }
)

@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)

def update_output_div(input_value):
    return f'Output: {input_value}'

if __name__ == '__main__':
    app.run(debug=True)