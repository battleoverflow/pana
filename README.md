<h2 align="center">Pana - Pick a Name Already</h2>

<p align="center">
  Check if a package or username is available from some of the most popular package managers.
</p>


## Install

Pana is available from `pip`:

```bash
pip install pana
```

## Package Managers

:white_check_mark: - Actively supported & tested

:warning: - In development

:question: - Not started, but I'd like to eventually get them added

| Package Manager                                              | Status               |
|--------------------------------------------------------------|----------------------|
| [PyPI](https://pypi.org/)                                    |  :white_check_mark:  |
| [npm](https://www.npmjs.com/)                                |  :white_check_mark:  |
| [NuGet](https://www.nuget.org/)                              |  :white_check_mark:  |
| [crates](https://crates.io/)                                 |  :question:          |
| [Packagist](https://packagist.org/)                          |  :question:          |
| [VSCode Marketplace](https://marketplace.visualstudio.com/)  |  :question:          |

## Examplea

### Module
```python
from pana import Pana

# Print both lists to stdout
print(Pana.check_pkg("pana"))
print(Pana.check_user("azazelm3dj3d"))

# Example output
"""
[
    ['pypi', True],
    ['npm', True],
    ['nuget', False]
]
"""

```

### CLI

Search for a specific package

```bash
pana -p pana
```

Search for a username

```bash
pana -u azazelm3dj3d
```
