import requests,sys
from bs4 import BeautifulSoup
from multiprocessing import Pool
import threading, queue

class SearchInformationOnSourceCode:
	def __init__(self,urls,workspacename):
		self.urls_ = urls
		self.workspacename_ = workspacename

	def Code(self,url:str):
		pass
	
	@property
	def urls(self) -> list:
		return self.urls_
	
	@property
	def workspacename(self) -> str:
		return self.workspacename_

	def __str__(self):
		return f"SearchInformationOnSourceCode"

	def __repr__(self):
		return 'SearchInformationOnSourceCode(urls_=' + str(self.urls_) + ' ,workspacename_=' + self.workspacename_ + ')'

if __name__ == "__main__":
    #sys.exit()