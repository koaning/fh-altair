from fh_altair import altair2fasthtml, altair_headers
from fasthtml.common import * 
import numpy as np
import pandas as pd
import altair as alt

app, rt = fast_app(hdrs=altair_headers)  

count = 0
plotdata = []

def generate_chart():
    pltr = pd.DataFrame({'y': plotdata, 'x': range(len(plotdata))})
    chart = alt.Chart(pltr).mark_line().encode(x='x', y='y').properties(width=400, height=200)
    return altair2fasthtml(chart)

@app.get("/")
def home():
    return Title("Altair Demo"), Main(
        H1("Altair Demo"),
        P("Nothing too fancy, but still kind of fancy."),
        Div(f"You have pressed the button {count} times.", id="chart"),
        Button("Increment", hx_get="/increment", hx_target="#chart", hx_swap="innerHTML"),
        style="margin: 20px"
    )


@app.get("/increment")
def increment():
    global plotdata, count
    count += 1
    plotdata.append(np.random.exponential(1))
    return Div(
        generate_chart(),
        P(f"You have pressed the button {count} times."),
    )

serve()
