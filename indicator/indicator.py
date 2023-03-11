from bs4 import BeautifulSoup,MarkupResemblesLocatorWarning
from urlextract import URLExtract
import requests,sys,re,tldextract
from multiprocessing import Pool
import threading, queue
from log import msg
import argparse

from V1DomainFinder import	(
                            DomainIndicator,
                            ReadData,
                            Remove,
                            bcolors
							)

from functions import	(
                    	Eliminate,
                    	Merge,
                    	EmailIndicator,
                    	MultiProcessingTasks,
                    	RegX
						)

import warnings

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)


#from downloads.V1StaticfileDownloader import stream_multiple
#OK



print(f"""{bcolors.OKGREEN}
	
  _____      _   _             _               _____      _       _ _ _                           
 |_   _|    | | (_)           | |             |_   _|    | |     | | (_)                          
   | | _ __ | |_ _  __ _  __ _| |_ ___  _ __    | | _ __ | |_ ___| | |_  __ _  ___ _ __   ___ ___ 
   | || '_ \| __| |/ _` |/ _` | __/ _ \| '__|   | || '_ \| __/ _ \ | | |/ _` |/ _ \ '_ \ / __/ _ \\
  _| || | | | |_| | (_| | (_| | || (_) | |     _| || | | | ||  __/ | | | (_| |  __/ | | | (_|  __/
  \___/_| |_|\__|_|\__, |\__,_|\__\___/|_|     \___/_| |_|\__\___|_|_|_|\__, |\___|_| |_|\___\___|
                    __/ |                                                __/ |                    
                   |___/                                                |___/                     

Author : OsmanKandemir

{bcolors.ENDC}""")






class LinkExtractor:



	def __init__(self,urls:list,workspacename:str,proxy_servers:dict):
		self.urls_ = urls
		self.workspacename_ = workspacename
		self.proxy_servers = proxy_servers

	
	def Test(self,urls:str) -> list:
		extractor = URLExtract()
		try:
			headers = {'User-agent': 'Mozilla/5.0'}
			grab = requests.get(urls,proxies=self.proxy_servers,headers=headers,timeout=(2))
			if grab.status_code == 200:
				soup = BeautifulSoup(grab.content, 'html.parser',from_encoding="iso-8859-1")
				AllUrls = []
				DomainIndicator(extractor.find_urls(grab.text))
				#'base','form'
				for link in soup.find_all(['a', 'link']):
					data = link.get('href')
					try:
						if extractor.find_urls(data):
							if not Eliminate(data):AllUrls.append(data)
						if data.startswith("/"):
							ext = tldextract.extract(urls)
							if not Eliminate(urls+data):
								if ext.subdomain:
									AllUrls.append("http://" + ext.subdomain + "." + ext.domain + "." + ext.suffix + data)
								else:
									AllUrls.append("http://"+ ext.domain + "." + ext.suffix + data)
							else:
								continue
						else:
							continue
					except:
						continue
				return list(set(AllUrls))
			else:
				pass
		except ConnectionError as Error:
			msg(f"{bcolors.OKBLUE}{Error.__class__.__name__}{bcolors.ENDC}")
		except:
			pass
		

	def Start(self,url:str,results_queue:queue.Queue):
		Tst = []
		msg(f"{bcolors.OKBLUE}Indicator is pulling to static links from Target.{bcolors.ENDC}")
		try:
			res = self.Test(url)
			res = list(set(res))
			for i,z in zip(range(1,len(res)),res):
				res = self.Test(z)
				Tst.append(res)
			results_queue.put(Tst)
		except Exception as Error:
			msg(f"{bcolors.OKBLUE}Thread - Connection Error or {Error}{bcolors.ENDC}")


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
			msg(f"{bcolors.OKBLUE}Undefined Domain or Connection Error.{bcolors.ENDC}")

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


def Indicator(urls,proxy_servers = None):
	#Burda Proxy_servers parametresi var dikkat et.
	#msg(LinkExtractor(RegX(urls),"Workspacename").Run())
	LinkExtractor(RegX(urls),"Workspacename",proxy_servers).Run()

if __name__ == "__main__":
	Domains = ["openai.com"]
	Indicator(Domains)
	#sys.exit()