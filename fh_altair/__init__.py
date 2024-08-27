from uuid import uuid4
from fasthtml.common import Div, Script


altair_headers = [
    Script(src="https://cdn.jsdelivr.net/npm/vega@5"),
    Script(src="https://cdn.jsdelivr.net/npm/vega-lite@5"),
    Script(src="https://cdn.jsdelivr.net/npm/vega-embed@6")
]


def altair2fasthml(chart):
    """This is the version with bad spelling"""
    print("You have imported `altair2fasthml` which is a misspelled function. Sorry about that! It will be deprecated in favour of `altair2fasthtml` in a later release.")
    return altair2fasthtml(chart)


def altair2fasthtml(chart):
    jsonstr = chart.to_json()
    chart_id = f'uniq-{uuid4()}'
    settings = "{actions: false}"
    return Div(Script(f"vegaEmbed('#{chart_id}', {jsonstr}, {settings});"), id=chart_id)
