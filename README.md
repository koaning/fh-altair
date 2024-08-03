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
from fh_altair import altair2fasthml

def generate_chart():
    pltr = pd.DataFrame({'y': [1, 2, 3, 2], 'x': [3, 1, 2, 4]})
    chart = alt.Chart(pltr).mark_line().encode(x='x', y='y').properties(width=400, height=200)
    return altair2fasthml(chart)
```

This will return a `Div` that contains your rendered altair chart.

## Roadmap

This repository is originally meant to be simple helper, but if there are more advanced use-cases to consider I will gladly consider them. Please start a conversation by opening up an issue before starting a PR though.
