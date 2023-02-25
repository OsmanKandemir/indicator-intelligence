
![Logo](img.png)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/smicallef/spiderfoot/master/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.7+-green)](https://www.python.org)
[![Docker](https://img.shields.io/badge/docker-build-important.svg?logo=Docker)](https://www.docker.com)
[![Version](https://img.shields.io/badge/version-1.0.1-blue.svg)](https://github.com/OsmanKandemir/indicator-intelligence)



# Indicator-Intelligence


## Description

Indicator collects sensitive informations (Hash,Domain,Email,Ipv4,Ipv6) to threats. 

Fundamental method of logic is IOC. An IOC is the cyber-equivalent of evidence left at a crime scene. 

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

### From Docker

You can run this application on a container after build a Dockerfile.

```
docker build -t indicator .
docker run indicator --domain http://google.com

```

## Usage

```
from indicator import Indicator

Indicator(["http://google.com"])
```


## Resources

- https://resources.infosecinstitute.com/topic/threat-hunting-for-file-hashes-as-an-ioc/
- https://abnormalsecurity.com/glossary/indicators-of-compromise

## Development and Contribution

See; [CONTRIBUTING.md](CONTRIBUTING.md)

## License

Copyright (c) 2023 Osman Kandemir \
Licensed under the MIT License.