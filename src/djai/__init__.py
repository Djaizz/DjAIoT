import json
from pathlib import Path
from types import SimpleNamespace


metadata = SimpleNamespace(**json.load(open(Path(__file__).parent /
                                            'metadata.json')))


__version__ = metadata.VERSION
