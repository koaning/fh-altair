from uuid import uuid4
from fasthtml.common import Div, Script


altair_headers = [
    Script(src="https://cdn.jsdelivr.net/npm/vega@5"),
    Script(src="https://cdn.jsdelivr.net/npm/vega-lite@5"),
    Script(src="https://cdn.jsdelivr.net/npm/vega-embed@6")
]


def altair2fasthml(chart):
    jsonstr = chart.to_json()
    chart_id = f'uniq-{uuid4()}'
    settings = "{actions: false}"
    return Div(Script(f"vegaEmbed('#{chart_id}', {jsonstr}, {settings});"), id=chart_id)
