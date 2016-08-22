
Wolong
======

![https://pypi.python.org/pypi/wolong][pypi]
![https://travis-ci.org/brianthelion/wolong][travis]
![https://wolong.readthedocs.io/en/latest/?badge=latest][docs]
![https://pyup.io/repos/github/brianthelion/wolong/][github]

[pypi]: https://img.shields.io/pypi/v/wolong.svg
[travis]: https://img.shields.io/travis/brianthelion/wolong.svg
[docs]: https://readthedocs.org/projects/wolong/badge/?version=latest
[github]: https://pyup.io/repos/github/brianthelion/wolong/shield.svg

Pandas in captivity. Base classes and API for rapid prototyping high-throughput
batch processors and their CLIs.


* Free software: MIT license
* Documentation: https://wolong.readthedocs.io.


Features
--------

* TODO

Example
-------

```python
# my_plugin.py

import pandas as pd
from wolong.base import BasePlugin
from wolong.cli import entrypoint

class MyPlugin(BasePlugin): # REQUIRED
    consumes_cols = ['foo'] # REQUIRED
    provides_cols = ['bar'] # REQUIRED

    def __init__(self, df):
        super(MyPlugin, self).__init__(df) # REQUIRED

    def process(self, *args, **dargs): # TYPICAL
        new_df = ... # Do some computation
        self.result = new_df # REQUIRED

def setargs(parser): # TYPICAL
    parser.add_argument(...)

@entrypoint(['run', 'my', 'plugin'], args=setargs) #REQUIRED
def cli_run_my_plgin(api, ns, parser): # REQUIRED
    plugin = MyPlugin(api.cursor) # TYPICAL
    plugin.process(...) # TYPICAL
    api.cursor = plugin.result # TYPICAL
```

Credits
-------

This package was created with [Cookiecutter][1] and the
[audreyr/cookiecutter-pypackage][2] project template.

[1]: https://github.com/audreyr/cookiecutter
[2]: https://github.com/audreyr/cookiecutter-pypackage

