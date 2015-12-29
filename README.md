# TablePrinter

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
TablePrinter(data, col_order=[("title", "The Title Of The Book"), ("rating", "Rating"), ("has_sequel", "Sequel?"), ("favorite", "Favorite?")])
```

|The Title Of The Book|Rating|Sequel?|Favorite?|
|-----|-----|-----|-----|
| Oryx & Crake|5|True| |
| Galapagos|5|| |
