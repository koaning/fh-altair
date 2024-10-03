import altair as alt
import pandas as pd

from fh_altair import altair2fasthtml


def test_no_err():
    pltr = pd.DataFrame({"y": [1, 2, 3, 2], "x": [3, 1, 2, 4]})
    chart = (
        alt.Chart(pltr)
        .mark_line()
        .encode(x="x", y="y")
        .properties(width=400, height=200)
    )
    return altair2fasthtml(chart)


def test_vega_options_passed_to_vegaEmbed():
    pltr = pd.DataFrame({"y": [1, 2, 3, 2], "x": [3, 1, 2, 4]})
    chart = (
        alt.Chart(pltr)
        .mark_line()
        .encode(x="x", y="y")
        .properties(width=400, height=200)
    )
    vega_embed_call = altair2fasthtml(
        chart, vega_options={"renderer": "svg", "actions": True}
    ).__str__()
    assert '{"renderer": "svg", "actions": true}' in vega_embed_call
