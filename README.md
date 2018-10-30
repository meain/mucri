# Mucri

A python framework for extracting the same stuff from a lot of webpages.
Just a tiny tiny wrapper over `asyncio`!


## Installation

> Only python 3.6_+

```sh
pip isntall mucri
```

## Usage

```python
from mucri import fetch_links

links = [
    { "url": "http://somelink" },
    {
        "url": "http://fakelink",
        "action": "get", # get | post
        "data": {},
        "headers": {},
        "resp_type": "text", # text | json
    }
]

results = fetch_links(links) # fetches all of them asynchronously

```
