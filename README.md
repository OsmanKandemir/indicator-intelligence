# Indicator-Intelligence


## Description

Indicator collects sensitive informations (Hash,Domain,Email,Ipv4,Ipv6) to threats. 

## Installation

### From Source Code

```
git clone https://github.com/OsmanKandemir/indicator-intelligence.git
cd indicator-intelligence
python setup.py build
python setup.py install
```

### From Pypi

The script is [available on PyPI](https://pypi.org/project/indicator-intelligence/). To install with pip:
```
pip install indicator-intelligence
```

## Usage

```
from indicator import Indicator

Indicator(["http://google.com"])
```

## Development and Contribution
See; [CONTRIBUTING.md](CONTRIBUTING.md)