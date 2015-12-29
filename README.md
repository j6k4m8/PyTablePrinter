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
