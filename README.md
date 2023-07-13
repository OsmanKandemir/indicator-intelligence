
![Logo](imglogo.png)

[![Indicator-Intelligence](https://img.shields.io/badge/Indicator-Intelligence-blue)](https://www.github.com/OsmanKandemir/indicator-intelligence)
![PyPI - Downloads](https://img.shields.io/pypi/dm/indicatorintelligence)
[![Version](https://img.shields.io/badge/version-1.1.1-blue.svg)](https://github.com/OsmanKandemir/indicator-intelligence)
[![Pip Version](https://img.shields.io/badge/pypi-23.0.1-green)](https://www.python.org)
[![License](https://img.shields.io/badge/license-GPL-blue.svg)](https://raw.githubusercontent.com/smicallef/spiderfoot/master/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.7+-green)](https://www.python.org)
[![Docker](https://img.shields.io/badge/docker-build-important.svg?logo=Docker)](https://www.docker.com)




# Indicator-Intelligence

#### NOTE : You should definitely use it for legal activities. Please See; [USAGE_POLICY.md](USAGE_POLICY.md) [LICENSE](LICENSE)

## Description

Finds related domains and IPv4 addresses to do threat intelligence after Indicator-Intelligence collects static files

## ScreenShot

![](imgtest.png)


## Done
- [x] Releated domains, IPs collect
- [x] HTTP - HTTPS Check.

## Installation

### From Source Code

You can use virtualenv for package dependencies before installation.

```
git clone https://github.com/OsmanKandemir/indicator-intelligence.git
cd indicator-intelligence
python setup.py build
python setup.py install
```

### From Pypi

The script is [available on PyPI](https://pypi.org/project/indicatorintelligence/). To install with pip:
```
pip install indicatorintelligence
```

### From Dockerfile

You can run this application on a container after build a Dockerfile.

```
docker build -t indicator .
docker run indicator --domains target-web.com --json
```

### From DockerHub

```
docker pull osmankandemir/indicator
docker run osmankandemir/indicator --domains target-web.com --json
```

### From Poetry

```
pip install poetry
poetry install
```

## Usage

```
-d DOMAINS [DOMAINS], --domains DOMAINS [DOMAINS] Input Targets. --domains target-web1.com target-web2.com
-p PROXY, --proxy PROXY Use HTTP proxy. --proxy 0.0.0.0:8080
-a AGENT, --agent AGENT Use agent. --agent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
-o JSON, --json JSON  JSON output. --json
```

#### Function Usage

```
from indicator.indicator import Indicator

#SCAN
Indicator(["target-web.com"])

#OUTPUT
Indicator(["target-web.com"],json=True)
```

## Development and Contribution

See; [CONTRIBUTING.md](CONTRIBUTING.md)


## License

Copyright (c) 2023 Osman Kandemir \
Licensed under the GPL-3.0 License.

## Donations

If you like Indicator-Intelligence and would like to show support, you can use **Buy A Coffee** or **Github Sponsors** feature for the developer using the button below.

You can use the github sponsored tiers feature for donations.

Sponsor me : https://github.com/sponsors/OsmanKandemir 😊

<a href="https://www.buymeacoffee.com/OsmanKandemir" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Your support will be much appreciated😊