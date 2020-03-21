import graph
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np

n = 18

g = graph.Graph(n)
g.add_edge((0,1))
g.add_edge((1,6))
g.add_edge((6,0))

g.add_edge((2,3))
g.add_edge((3,9))
g.add_edge((9,8))
g.add_edge((8,2))
g.add_edge((2,7))
g.add_edge((12,7))
g.add_edge((13,8))
g.add_edge((9,4))

g.add_edge((14,15))

g.add_edge((5,10))
g.add_edge((10,17))

g.add_edge((11,16))

x,y = g.visualize(kr = 0.2, ks = 1, d = 0.5)
edges = g.get_edges()



driscrete_template = go.layout.Template()
driscrete_template.layout = {
    'paper_bgcolor':'white',
    'plot_bgcolor':'black',
    'showlegend':False,
    'xaxis': {
              'gridcolor': 'black',
              'linecolor': 'black',
              'zerolinecolor': 'black',
              'zerolinewidth': 0
              },
    'yaxis': {
              'gridcolor': 'black',
              'linecolor': 'black',
              'zerolinecolor': 'black',
              'zerolinewidth': 0
              },

}
    


fig = go.Figure()
for e in edges:
    e1,e2 = e
    fig.add_trace(go.Scatter(
        x=[x[e1], x[e2]], y=[y[e1], y[e2]],
        mode='lines',
        line=dict(
            color='rgba(24, 150, 144, 1)',
            width=4,
        )
    ))
fig.add_trace(go.Scatter(
    x=x, y=y, 
    mode='markers',
    marker_color='rgba(24, 154, 210, 1)',
    hovertext=list(np.arange(n)),
    marker = dict(
        size = 15,
        line_width = 2,
    )
    
))
fig.update_layout(template=driscrete_template)
fig.show()