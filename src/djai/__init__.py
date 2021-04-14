import json
from types import SimpleNamespace


metadata = SimpleNamespace(**json.load(open('metadata.json')))


__version__ = metadata.VERSION
