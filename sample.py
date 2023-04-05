import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 450,
    mode = "gauge+number+delta",
    title = {'text': "WPM"},
    delta = {'reference': 120},
    gauge = {'axis': {'range': [None, 250]},
             'steps' : [
                 {'range': [0, 125], 'color': "lightgray"},
                 {'range': [100, 250], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 200}}))

fig.write_image("hello.png")