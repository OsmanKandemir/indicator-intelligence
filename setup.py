from setuptools import setup, find_packages
import codecs
import os

HERE = os.path.abspath(os.path.dirname(__file__))

VERSION = '1.0.0'
DESCRIPTION = 'Indicator-Intelligence finds related domains for target to do threat analysis.'
# Setting up
setup(
    name="IndicatorIntelligence",
    version=VERSION,
    author="OsmanKandemir",
    author_email="osmankandemir00@gmail.com",
    license='GPL-3.0',
    url='https://github.com/OsmanKandemir/indicator-intelligence',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    packages=find_packages(),
    install_requires=[
        "aiodns==3.0.0",
        "beautifulsoup4==4.11.2",
        "build==0.10.0",
        "certifi==2022.12.7",
        "cffi==1.15.1",
        "charset-normalizer==3.0.1",
        "dnspython==1.15.0",
        "filelock==3.9.0",
        "idna==3.4",
        "packaging==23.0",
        "platformdirs==3.0.0",
        "pycares==4.3.0",
        "pycparser==2.21",
        "pyproject_hooks==1.0.0",
        "requests==2.28.2",
        "requests-file==1.5.1",
        "six==1.16.0",
        "soupsieve==2.4",
        "tldextract==3.4.0",
        "tomli==2.0.1",
        "uritools==4.0.1",
        "urlextract==1.8.0",
        "urllib3==1.26.14"
    ],
    keywords=['python', 'threat','threat-intelligence','intelligence','indicator'],
    classifiers=[
    
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Environment :: Console",
        "Topic :: Security",
        "Typing :: Typed",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Telecommunications Industry",
        "Intended Audience :: System Administrators"
    ],
    python_requires='>=3.9',
)