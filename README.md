
![Logo](img.png)

[![Indicator-Intelligence](https://img.shields.io/badge/Indicator-Intelligence-blue)](https://www.github.com/OsmanKandemir/indicator-intelligence)
[![Version](https://img.shields.io/badge/version-1.0.1-blue.svg)](https://github.com/OsmanKandemir/indicator-intelligence)
[![Pip Version](https://img.shields.io/badge/pypi-23.0.1-green)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/smicallef/spiderfoot/master/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.7+-green)](https://www.python.org)
[![Docker](https://img.shields.io/badge/docker-build-important.svg?logo=Docker)](https://www.docker.com)




# Indicator-Intelligence


## Description

Indicator-Intelligence collects static files and related domains for target to do threat analysis.

#### NOTE : You should definitely use it for legal penetrations tests. Responsibility belongs to user.

##### Web scraping for GDPR 

###### Answer: unless you have the person's explicit consent it is now illegal to scrape an EU resident's personal data under GDPR.


Fundamental logic method is similar to IOC.

## TODO
- [x] Releated domains collect
- [ ] Email, Ipv4, Ipv6 collect
- [ ] Result compare structure with Django
- [ ] Quick crawling optimization and more indicators
- [ ] Calculates hashes to threat analysis

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
### From Poetry

```
pip install poetry
poetry install
```

### From Dockerfile

You can run this application on a container after build a Dockerfile.

```
docker build -t indicator .
docker run indicator --domain http://google.com

```

## Usage

Save the result after the first scan starts. 
Save the second result after start second scan. Compare and analysis results.

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

## Donations
If you like Indicator-Intelligence and would like to show support, you can Buy A Coffee for the developer using the button below

<a href="https://www.buymeacoffee.com/OsmanKandemir" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Your support will be much appreciated😊