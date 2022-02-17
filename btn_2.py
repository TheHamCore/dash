from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
app = Dash(__name__)

ALLOWED_TYPES = (
    "number",
)


app.layout = html.Div(
    [
        dcc.Input(id='input-1-state', type='number', value=''),
        html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
        html.Div(id='output-state')
        #for _ in ALLOWED_TYPES
    ]
    #[html.Div(id="out-all-types")]
)


@app.callback(
    Output("output-state", "children"),
    Input('submit-button-state', 'n_clicks'),
    State('input-1-state', 'value'),
)
def update_output(n_clicks, input1):
    print(input1)
    for i in range(3):
        print(i)
    locations = [go.Scattermapbox(
        lon=[10, 20 , 30],
        lat=[-10, -20, -30],
        mode='markers',
    )]
    return {
        'data': locations,
        'layout': go.Layout(
            uirevision='foo',  # preserves state of figure/map after callback activated
            clickmode='event+select',
            hovermode='closest',
            hoverdistance=2,
            title=dict(text="Where to Recycle My Stuff?", font=dict(size=50, color='green')),
            mapbox=dict(
                bearing=25,
                style='dark',
                center=dict(
                    lat=40.80105,
                    lon=-73.945155
                ),
                pitch=40,
                zoom=11.5
            ),
        )
    }



if __name__ == "__main__":
    app.run_server(debug=True)

# @app.callback(
#     Output("out-all-types", "children"),
#     [Input("input_{}".format(_), "value") for _ in ALLOWED_TYPES],
# )
# def cb_render(*vals):
#     print(" | ".join((str(val) for val in vals if val)))
#     return " | ".join((str(val) for val in vals if val))
#
#
# if __name__ == "__main__":
#     app.run_server(debug=True)
dcc.Input(id='input_input',
                      placeholder='Enter geopoint id',
                      type='number',
                      value='',
                      min='1',
                      max=list_[-1],
                      # list='browsers'
                      ),