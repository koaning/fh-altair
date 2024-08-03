import pandas as pd
import altair as alt
from fh_altair import altair2fasthml

def test_no_err():
    pltr = pd.DataFrame({'y': [1, 2, 3, 2], 'x': [3, 1, 2, 4]})
    chart = alt.Chart(pltr).mark_line().encode(x='x', y='y').properties(width=400, height=200)
    return altair2fasthml(chart)
