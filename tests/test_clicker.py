from fasthtml.common import * 
import numpy as np
import pandas as pd
import altair as alt
import numpy as np
from fh_altair import altair2fasthml

app, rt = fast_app(
    hdrs = [
        Script(src="https://cdn.jsdelivr.net/npm/vega@5"),
        Script(src="https://cdn.jsdelivr.net/npm/vega-lite@5"),
        Script(src="https://cdn.jsdelivr.net/npm/vega-embed@6")
    ]
)  
count = 0
plotdata = []

alt.renderers.set_embed_options(actions=False)

def generate_chart():   
    pltr = pd.DataFrame({'y': plotdata, 'x': np.arange(count) + 1.0})
    chart = alt.Chart(pltr).mark_line().encode(x='x', y='y').properties(width=400, height=200)
    return altair2fasthml(chart)

@app.get("/")
def home():
    return Title("Altair Demo"), Main(
        H1("Altair Demo"),
        P("Nothing too fancy, but still kind of fancy."),
        Div(f"You have pressed the button {count} times.", id="chart"),
        Button("Increment", hx_get="/increment", hx_target="#chart", hx_swap="innerHTML"),
        Input(type="range", name="slider", hx_include="[name='email']", min=1, max=10, hx_trigger="input", hx_post="/increment_slider", hx_target="#chart", hx_swap="innerHTML", hx_vals="value"),
        style="margin: 20px"
    )


@app.get("/increment/")
def increment():
    global plotdata, count
    count += 1
    plotdata.append(np.random.exponential(1))
    return Div(
        generate_chart(),
        P(f"You have pressed the button {count} times."),
    )


@app.post("/increment_slider/")
def increment_i(data: dict):
    print(f"slider updated: {data}")
    global plotdata, count
    count += 1
    plotdata.append(float(data['slider']))
    return Div(
        generate_chart(),
        P(f"You have pressed the button {count} times."),
    )

from starlette.testclient import TestClient

client = TestClient(app)

def test_clicks():
    for i in range(10):
        client.get('/increment')
    resp = client.get('')
    assert 'You have pressed the button 10 times.' in resp.text
    # To properly test if the chart really shows up I will need to resort to Playwright and I prefer to do that another time
