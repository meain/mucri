# Mucri

Quickly fetch a lot of pages/apis using python `asyncio`.


## Installation

> Only python 3.6+

```sh
pip isntall mucri
```

## Usage

```python
from mucri import fetch_pages

links = [
    "http://meain.github.io",
    { "url": "http://somelink" },
    {
        "url": "http://fakelink",
        "action": "get", # get | post
        "data": {},
        "headers": {},
        "resp_type": "text", # text | json
    }
]

results = fetch_pages() # fetches all of them asynchronously

```
