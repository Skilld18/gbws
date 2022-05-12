import plotly.graph_objects as go
import itertools
from bike_models import bikes
from bike import *

empty_bike = Bike("not_a_bike", Sram.none, Shimano.none, Wheel.w29, Manufactuer.kona)
priv = Bike("141", Sram.nx, Shimano.none, Wheel.w29, Manufactuer.privateer)

categories = list(vars(empty_bike).keys())
categories.remove("model")
categories.remove("manufactuer")
vector_mod_catagories = list(map(lambda x: 0, categories))

fig = go.Figure()
names = list(map(lambda x: x.model, bikes))
dataset = list(map(lambda x: [vars(x).get(key).value for key in categories], bikes))



for i, data in enumerate(dataset):
    fig.add_trace(go.Scatterpolar(
      r=data,
      theta=categories,
      fill='toself',
      name=names[i]
    ))


fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5]
    )),
  showlegend=False
)

for i, e in enumerate(dataset):
    dataset[i].insert(0, bikes[i].model)
print(dataset)

fig1 = go.Figure(data=[go.Table(header=dict(values=[""] + categories),
                 cells=dict(values=list(zip(*dataset))))])

all_data = []
for n in bikes:
    all_data.append([])
    for o in bikes:
        all_data[-1].append(str(o-n))

fig2 = go.Figure(data=[go.Table(header=dict(values=[""] + names),
                 cells=dict(values=[names] + all_data))])

fig3 = go.Figure(data=[go.Table(header=dict(values=["field", "value"]),
                 cells=dict(values=[categories, vector_mod_catagories]))])


import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    html.Div(id='body-div', children=[
    dcc.Graph(figure=fig, style={'display': 'inline-block'}),
    dcc.Graph(figure=fig2, style={'display': 'inline-block'}),
    dcc.Graph(id="table", figure=fig3, style={'display': 'inline-block'}    )]),
    dcc.Graph(figure=fig1)
])

from dash import Output, Input

app.run_server(debug=True, use_reloader=True)  # Turn off reloader if inside Jupyter

