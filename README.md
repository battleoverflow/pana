# Pana

Pana, or "Pick a Name Already", is a CLI and module built to verify if a package name or username is available from common package managers.

## Install

```bash
pip install pana
```

## Package Managers

:white_check_mark: - Actively supported

:warning: - In Development

| Package Manager                 | Status               |
|---------------------------------|----------------------|
| [PyPI](https://pypi.org/)       |  :white_check_mark:  |
| [npm](https://www.npmjs.com/)   |  :white_check_mark:  |
| [NuGet](https://www.nuget.org/) |  :white_check_mark:  |
| [crates](https://crates.io/)    |  :warning:           |

## Examplea

### Module
```python
from pana import Pana

# Print both lists to stdout
print(Pana.check_pkg("pana"))
print(Pana.check_user("azazelm3dj3d"))
```
Note: *Currently prints to stdout*

### CLI

Search for a specific package

```bash
pana -p pana
```

Search for a username

```bash
pana -u pana
```
