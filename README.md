# TablePrinter

## Installation
You can either clone this repository and use it locally, or install from pypi:

```
pip install pytableprinter
```

Use this Python library to easily print markdown tables of data that are either lists of dictionaries or dictionaries of dictionaries. For instance:

```python
data = [
    {
        "has_sequel": True,
        "author": "Margaret Atwood",
        "title": "Oryx & Crake",
        "rating": 5
    },
    {
        "author": "Kurt Vonnegut",
        "title": "Galapagos",
        "rating": 5
    }
]
```

# Usage

```python
from tableprinter import *
tp = TablePrinter(data)
print tp.to_markdown()
```

You can supply extra arguments to the `TablePrinter` constructor to get different results. For instance, specify the order of columns to include:

```python
TablePrinter(data, col_order=['title', 'author'])
```

Specifying column titles that have no corresponding datum in the dictionaries of `data` will result in empty columns (but will not fail to render):

```python
TablePrinter(data, col_order=['title', 'rating', 'has_sequel' 'favorite'])
```

|title|rating|has_sequel|favorite|
|-----|-----|-----|-----|
| Oryx & Crake|5|True| |
| Galapagos|5|| |

You can also provide 2-tuples instead of a simple list for `col_order`. The first will be used as the lookup key, and the second string will be used as the table title.

```python
TablePrinter(data, col_order=[
        ("title", "The Title Of The Book"),
        ("rating", "Rating"),
        ("has_sequel", "Sequel?"),
        ("favorite", "Favorite?")])
```

|The Title Of The Book|Rating|Sequel?|Favorite?|
|-----|-----|-----|-----|
| Oryx & Crake|5|True| |
| Galapagos|5|| |

You can even mix the two, with something like:
```python
TablePrinter(data, col_order=[
        ("title", "The Title Of The Book"),
        "rating",
        ("has_sequel", "Sequel?"),
        "favorite"])
```

## ...and for my final trick...

The latest, neatest trick is the implementation of functions as columns as well. If you provide a 3-tuple and the last item is a function, you can run a function on each datum like so:

```python
("rating percentage", "Rating %", lambda d: str(100. * d['rating']/5.0) + "%")
```

(This, of course, returns a percentage rating, using the `rating` field, as calculated out of a possible `5`.)

| ... | Rating % | 
|-----|------|
| ... | 80% |
