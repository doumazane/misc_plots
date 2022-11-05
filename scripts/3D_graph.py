import numpy as np
import plotly.express as px
import plotly.graph_objects as go

fun = lambda x, y: (-(y+47) * np.sin(np.sqrt(abs(x/2 + (y  + 47))))
                    -x * np.sin(np.sqrt(abs(x - (y  + 47)))))

x, y = np.meshgrid(np.linspace(-150,150,100), np.linspace(-150,150,100))

z = fun(x, y)

fig = go.Figure(go.Surface(x=x, y=y, z=z, colorscale="earth_r",))
fig.update_layout(scene={
    "aspectratio": {"x": 1, "y": 1, "z": 0.5}
    })
fig.show()