import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Yo"),  # Title
    dcc.Dropdown(
        id='dropdown-selector',
        options=[
            {'label': 'Option 1', 'value': 'option1'},
            {'label': 'Option 2', 'value': 'option2'},
            {'label': 'Option 3', 'value': 'option3'}
        ],
        value='option1'  # Default selected value
    ),
    html.Div(id='output-text')  # Display selected value here
])

# Define a callback to update the output text
@app.callback(
    Output('output-text', 'children'),
    [Input('dropdown-selector', 'value')]
)
def update_output(selected_value):
    return f"You selected: {selected_value}"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)