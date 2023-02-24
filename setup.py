from setuptools import setup, find_packages
import codecs
import os

HERE = os.path.abspath(os.path.dirname(__file__))

VERSION = '1.0.0'
DESCRIPTION = 'Indicator Intelligence'
LONG_DESCRIPTION = 'Indicator Intelligence collects sensitive data informations to threats.(IPv4,IPv6,Email,Domain,Hash)'
# Setting up
setup(
    name="indicator-intelligence",
    version=VERSION,
    author="OsmanKandemir",
    author_email="osmankandemir00@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4==4.11.2",
        "certifi==2022.12.7",
        "charset-normalizer==3.0.1",
        "filelock==3.9.0",
        "idna==3.4",
        "indicator-intelligence==0.0.1",
        "platformdirs==3.0.0",
        "requests==2.28.2",
        "soupsieve==2.4",
        "uritools==4.0.1",
        "urlextract==1.8.0",
        "urllib3==1.26.14"
    ],
    license="",
    keywords=['python', 'threat', 'threat-intelligence', 'indigator'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)