from setuptools import setup, find_packages
import codecs
import os

HERE = os.path.abspath(os.path.dirname(__file__))

VERSION = '1.0.0'
DESCRIPTION = 'Indicator Intelligence'
LONG_DESCRIPTION = 'Indicator Intelligence collects sensitive data informations to threats.(IPv4,IPv6,Email,Domain,Hash)'
DEPENDENCIES = []

with open("{}/requirement.txt".format(HERE),"r") as REQ:
    try:
        for RE in REQ.readlines():
            DEPENDENCIES.append(str(RE))
        REQ.close()
    except:
        print("requirement.txt not exist.")
    



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
    install_requires=DEPENDENCIES,
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