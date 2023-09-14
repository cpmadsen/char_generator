import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(style={
'background-image': 'url("/assets/old_paper_background.png")',
'background-repeat': 'no-repeat',
'background-position': 'absolute',
'background-size': '1920px 1080px'
},children = [
html.H1('Hello World'),
html.P('This image has an image in the background')
])

if __name__ == '__main__':
    app.run(debug=True)