### fh-altair

Making it easier to show vegalite charts made with altair in FastHTML.

## Usage

You can install this tool by running:

```
python -m pip install fh-altair
```

After this step, it is ready for use! To use it you will want to make sure that you add the right headers to your FastHTML app. 

```python
from fh_altair import altair_headers

app, rt = fast_app(
    hdrs = altair_headers
)
```

This ensures that the required javascript and css files are always loaded. From here all you need to do is wrap your altair chart with our function and you are good to go!

```python
from fh_altair import altair2fasthtml

def generate_chart():
    pltr = pd.DataFrame({'y': [1, 2, 3, 2], 'x': [3, 1, 2, 4]})
    chart = alt.Chart(pltr).mark_line().encode(x='x', y='y').properties(width=400, height=200)
    return altair2fasthtml(chart)
```

This will return a `Div` that contains your rendered altair chart.

### Custom Vega options

Under the hood, `altair2fasthtml` makes a call to the `vegaEmbed` javascript library. The `vegaEmbed` javascript library accepts [various options](https://github.com/vega/vega-embed?tab=readme-ov-file#options) that alter the rendered chart. You can optionally pass custom Vega options like so:

```python
# To render your chart as a svg instead of the default canvas element
altair2fasthtml(chart, vega_options={"renderer":"svg"})

# To render your chart with action links turned on (by default action links are disabled) 
altair2fasthtml(chart, vega_options={"actions":True})
```

### Responsive width

As shown in the sample code above, you can control the width and height of your chart using `alt.Chart(...).properties(width, height)`. Additionally, if you would like the chart to dynamically take up the full width of its parent container, you can pass `full_width=True` to `altair2fasthtml` like so:

```python
# Renders a chart taking up the full width of the parent container
altair2fasthtml(chart, full_width=True)
```

## Roadmap

This repository is originally meant to be simple helper, but if there are more advanced use-cases to consider I will gladly consider them. Please start a conversation by opening up an issue before starting a PR though.
