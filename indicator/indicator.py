import requests,sys,re,tldextract
from bs4 import BeautifulSoup
from urlextract import URLExtract
from multiprocessing import Pool
import threading, queue
from log import msg
from V1DomainFinder import DomainIndicator,ReadData,Remove
from functions import Eliminate,Merge,EmailIndicator,MultiProcessingTasks
#from downloads.V1StaticfileDownloader import stream_multiple
#OK


"""

Author : OsmanKandemir

"""

#  _____      _   _             _               _____      _       _ _ _                           
# |_   _|    | | (_)           | |             |_   _|    | |     | | (_)                          
#   | | _ __ | |_ _  __ _  __ _| |_ ___  _ __    | | _ __ | |_ ___| | |_  __ _  ___ _ __   ___ ___ 
#   | || '_ \| __| |/ _` |/ _` | __/ _ \| '__|   | || '_ \| __/ _ \ | | |/ _` |/ _ \ '_ \ / __/ _ \\
#  _| || | | | |_| | (_| | (_| | || (_) | |     _| || | | | ||  __/ | | | (_| |  __/ | | | (_|  __/
#  \___/_| |_|\__|_|\__, |\__,_|\__\___/|_|     \___/_| |_|\__\___|_|_|_|\__, |\___|_| |_|\___\___|
#                    __/ |                                                __/ |                    
#                   |___/                                                |___/                     

PROXY_SERVERS = {}

PROXY_MODE = False

class LinkExtractor:
	def __init__(self,urls:list,workspacename:str):
		self.urls_ = urls
		self.workspacename_ = workspacename

	@staticmethod
	def Test(urls:str) -> list: 
		extractor = URLExtract()
		try:
			headers = {'User-agent': 'Mozilla/5.0'}
			grab = requests.get(urls,proxies=PROXY_SERVERS if PROXY_MODE == True else None,headers=headers,timeout=(5))
			if grab.status_code == 200:
				soup = BeautifulSoup(grab.text, 'html.parser')
				AllUrls = []
				DomainIndicator(extractor.find_urls(grab.text))
				for link in soup.find_all(['a', 'link']):
					data = link.get('href')
					if extractor.find_urls(data):
						if not Eliminate(data):AllUrls.append(data)
					if data.startswith("/"):
						ext = tldextract.extract(urls)
						if not Eliminate(urls+data):
							if ext.subdomain:
								AllUrls.append("http://" + ext.subdomain + "." + ext.domain + "." + ext.suffix + data)
							else:
								AllUrls.append("http://"+ ext.domain + "." + ext.suffix + data)
				return list(set(AllUrls))
			else:pass
		except ConnectionError as Error:
			msg(Error.__class__.__name__)
		except:pass
		
	@classmethod
	def Start(self,url:str,results_queue:queue.Queue):
		Tst = []
		msg("Indicator is pulling to static links from Target.")
		try:
			res = self.Test(url)
			res = list(set(res))
			for i,z in zip(range(1,len(res)),res):
				res = self.Test(z)
				Tst.append(res)
			results_queue.put(Tst)
		except Exception as Error:
			msg("Thread - Connection Error ")


	def Run(self) -> list:
		try:
			threads = []
			results_queue = queue.Queue()
			for i in self.urls_:
				t = threading.Thread(target=self.Start, args=(i, results_queue))
				threads.append(t)
				t.start()

			for t in threads:
				t.join()

			results = []
			while not results_queue.empty():
				result = results_queue.get()
				results.append(result)
			#return Merge(results[0]), ReadData()
			
			del threads[:]

			return ReadData()
		except:
			msg("Undefined Domain or Connection Error.")

	@property
	def urls(self) -> list:
		return self.urls_
	
	@property
	def workspacename(self) -> str:
		return self.workspacename_
	
	def __str__(self):
		return f"LinkExtractor"

	def __repr__(self):
		return 'LinkExtractor(urls_=' + str(self.urls_) + ' ,workspacename_=' + self.workspacename_ + ')'

def RegX(urls:list) -> list:
	return ["http://"+re.sub(r"(https?:\/\/)?([w]{3}\.)?(\w*.\w*)([\/\w]*)", "\\3", i, 0, re.MULTILINE | re.IGNORECASE) for i in urls]


def Indicator(urls):
	#msg(LinkExtractor(RegX(urls),"Workspacename").Run())
	LinkExtractor(RegX(urls),"Workspacename").Run()

if __name__ == "__main__":
	Domains = ["bg-tek.net","coslat.com","pentestbx.com"]
	Indicator(Domains)
	#sys.exit()