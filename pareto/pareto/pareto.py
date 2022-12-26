import plotly.graph_objects as go
from pareto_utils import *
from bike_models import *
from dash import html, dcc, Dash

app = Dash()

categories = removed_labels(bikes)
vmc = vector_mod_catagories(categories)
names = names(bikes)
dataset = datasets(bikes, categories)
dwn = dataset_with_names(dataset, names)
ad = all_data(bikes)

fig = go.Figure()
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

fig1 = go.Figure(data=[go.Table(header=dict(values=[""] + categories), cells=dict(values=list(zip(*dwn))))])
fig2 = go.Figure(data=[go.Table(header=dict(values=[""] + names), cells=dict(values=[names] + ad))])
fig3 = go.Figure(data=[go.Table(header=dict(values=["field", "value"]), cells=dict(values=[categories, vmc]))])

app.layout = html.Div([
    html.Div(id='body-div', children=[
        dcc.Graph(figure=fig, style={'display': 'inline-block'}),
        dcc.Graph(figure=fig2, style={'height': 'auto'}),
        dcc.Graph(id="table", figure=fig3, style={'display': 'inline-block'})]),
    dcc.Graph(figure=fig1)
]
)
app.run_server(debug=True, use_reloader=True)
