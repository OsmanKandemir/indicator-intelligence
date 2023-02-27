import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import threading, queue


from hashCalculater import HASH

print(HASH("indicator.py"))