from dash import Dash, html
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
                )
        ]
        ),
    html.Div(
        children=html.Div([
            html.H1('Overview'),
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

@app.callback(
    Output('output-text', 'children'),
    [Input('dropdown-selector', 'value')]
)

if __name__ == '__main__':
    app.run(debug=True)