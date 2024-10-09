import json
from uuid import uuid4

from fasthtml.common import Div, Script, Style

altair_headers = [
    Script(src="https://cdn.jsdelivr.net/npm/vega@5"),
    Script(src="https://cdn.jsdelivr.net/npm/vega-lite@5"),
    Script(src="https://cdn.jsdelivr.net/npm/vega-embed@6"),
    Style("""
    .vega-embed {
      width: 100%;
      display: flex;
    }
    .vega-embed details,
    .vega-embed details summary {
      position: relative;
    }
    """),
]


def altair2fasthml(chart):
    """This is the version with bad spelling"""
    print(
        "You have imported `altair2fasthml` which is a misspelled function. Sorry about that! It will be deprecated in favour of `altair2fasthtml` in a later release."
    )
    return altair2fasthtml(chart)


def altair2fasthtml(chart, vega_options={"actions": False}, full_width=False):
    """Convert an Altair chart to a FastHTML FT component

    Parameters
    ----------
    chart : altair.Chart
        An Altair chart
    vega_options : dict, optional
        Options dictionary passed to the vegaEmbed function, by default {"actions": False}
        which hides the Vega action menu.
    full_width: bool, optional
        When enabled, property width="responsive" is added to the chart allowing it to take up full width of parent Div

    Returns
    -------
    fastcore.xml.FT
        A FastHTML FT component containing both the target div and embedding script

    """
    if full_width:
        chart = chart.properties(width="container")
    jsonstr = chart.to_json()
    chart_id = f"uniq-{uuid4()}"
    return Div(
        Script(f"vegaEmbed('#{chart_id}', {jsonstr}, {json.dumps(vega_options)});"),
        id=chart_id,
    )
