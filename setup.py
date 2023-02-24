from setuptools import setup, find_packages
import codecs
import os

HERE = os.path.abspath(os.path.dirname(__file__))

VERSION = '1.0.1'
DESCRIPTION = 'Indicator Intelligence'
# Setting up
setup(
    name="indicator-intelligence",
    version=VERSION,
    author="OsmanKandemir",
    author_email="osmankandemir00@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4==4.11.2",
        "certifi==2022.12.7",
        "charset-normalizer==3.0.1",
        "filelock==3.9.0",
        "idna==3.4",
        "platformdirs==3.0.0",
        "requests==2.28.2",
        "soupsieve==2.4",
        "uritools==4.0.1",
        "urlextract==1.8.0",
        "urllib3==1.26.14"
    ],
    license="",
    keywords=['python', 'threat', 'threat-intelligence','indicator'],
    classifiers=[
    
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent"

    ],
    python_requires='>=3.7',
)