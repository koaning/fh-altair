import altair as alt
import pandas as pd
import pytest
from fasthtml.common import to_xml

from fh_altair import altair2fasthtml


@pytest.fixture
def sample_chart():
    pltr = pd.DataFrame({"y": [1, 2, 3, 2], "x": [3, 1, 2, 4]})
    chart = (
        alt.Chart(pltr)
        .mark_line()
        .encode(x="x", y="y")
        .properties(width=400, height=200)
    )
    return chart


def test_no_err(sample_chart):
    return altair2fasthtml(sample_chart)


@pytest.mark.parametrize(
    "renderer,actions",
    [("svg", True), ("svg", False), ("canvas", True), ("canvas", False)],
)
def test_vega_options(sample_chart, renderer, actions):
    result_xml = to_xml(
        altair2fasthtml(
            sample_chart, vega_options={"renderer": renderer, "actions": actions}
        )
    )
    assert f'"renderer": "{renderer}", "actions": {str(actions).lower()}' in result_xml


@pytest.mark.parametrize(
    "full_width,expected",
    [(True, '"width": "container"'), (False, '"width": 400'), (True, '"height": 200')],
)
def test_full_width(sample_chart, full_width, expected):
    result_xml = to_xml(altair2fasthtml(sample_chart, full_width=full_width))
    assert expected in result_xml
