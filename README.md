# Mucri

Quickly fetch a lot of pages/apis using python `asyncio`.


## Installation

> Only python 3.6+

```sh
pip isntall mucri
```

## Usage

`fetch_pages` takes two args:

`links` : list of links to be fetched (example below)
`concurrency`: how many requests to be send at a time (default 20)

```python
from mucri import fetch_pages

# links can be a single string or a dict with specific instructions
links = [
    "http://meain.github.io",
    { "url": "http://somelink" },
    {
        "url": "http://fakelink",
        "action": "get", # get | post
        "data": {},
        "headers": {},
        "resp_type": "text", # text | json | image
    }
]

results = fetch_pages() # fetches all of them asynchronously

```
