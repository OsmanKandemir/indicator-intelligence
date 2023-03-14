from bs4 import (
				BeautifulSoup,
				MarkupResemblesLocatorWarning,
				XMLParsedAsHTMLWarning
				)

from urlextract import URLExtract
import requests,sys,re,tldextract
from multiprocessing import Pool
import threading, queue
from log import (
				msg,
				worktime
				)
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

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)


#from downloads.V1StaticfileDownloader import stream_multiple
#OK

#BU HATAYI UNUTMA
#[INF] , March 13 2023 - 14:19:15 , Thread - Connection Error or 'NoneType' object is not iterable


print(f"""{bcolors.OKGREEN}
	
 _____          _ _           _               _____      _       _ _ _                           
|_   _|        | (_)         | |             |_   _|    | |     | | (_)                          
  | | _ __   __| |_  ___ __ _| |_ ___  _ __    | | _ __ | |_ ___| | |_  __ _  ___ _ __   ___ ___ 
  | || '_ \ / _` | |/ __/ _` | __/ _ \| '__|   | || '_ \| __/ _ \ | | |/ _` |/ _ \ '_ \ / __/ _ \\
 _| || | | | (_| | | (_| (_| | || (_) | |     _| || | | | ||  __/ | | | (_| |  __/ | | | (_|  __/
 \___/_| |_|\__,_|_|\___\__,_|\__\___/|_|     \___/_| |_|\__\___|_|_|_|\__, |\___|_| |_|\___\___|
                                                                        __/ |                    
                                                                       |___/                     
Author : OsmanKandemir

{bcolors.ENDC}""")



class LinkExtractor:



	def __init__(self,urls:list,worktime:str,proxy_servers:dict,agent:str):
		self.urls_ = urls
		self.worktime_ = worktime
		self.proxy_servers = proxy_servers
		self.agent =  {'User-agent':agent if agent else 'Mozilla/5.0'}

	
	def Test(self,urls:str) -> list:
		extractor = URLExtract()
		try:
			grab = requests.get(urls,proxies=self.proxy_servers,headers=self.agent,timeout=(2))
			if grab.status_code == 200:
				soup = BeautifulSoup(grab.content, 'html.parser',from_encoding="iso-8859-1")
				AllUrls = []
				DomainIndicator(extractor.find_urls(grab.text),self.worktime_)
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
			return ReadData(self.worktime_)
		except:
			msg(f"{bcolors.OKBLUE}Undefined Domain or Connection Error.{bcolors.ENDC}")

	@property
	def urls(self) -> list:
		return self.urls_
	
	@property
	def worktime(self) -> str:
		return self.worktime_
	
	def __str__(self):
		return f"LinkExtractor"

	def __repr__(self):
		return 'LinkExtractor(urls_=' + str(self.urls_) + ' ,workspacename_=' + self.worktime_ + ')'


def Indicator(domains,proxy_servers,agent):
	#msg(LinkExtractor(RegX(urls),"worktime").Run())

	LinkExtractor(RegX(domains),worktime(),proxy_servers,agent).Run()

def STARTS():

	proxy = set()

	parser = argparse.ArgumentParser()
	parser.add_argument("-d","--domains", nargs='+', required="True", help="Input Targets. --domains sample.com sample2.com")
	parser.add_argument("-p","--proxies", nargs='+', help="Use proxy. --proxies 0.0.0.0:80 1.1.1.1:8080")
	parser.add_argument("-a","--agent", help="Use agent. --agent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' ")
	parser.add_argument("-o","--json", action='store_true', help="JSON output")
	args = parser.parse_args()


	json = args.json if args.json else False
	agent = args.agent if args.agent else False
	if args.proxies:proxy = {"http" : proxy for proxy in args.proxies}
	if args.domains:domains = [domain for domain in args.domains]


	Indicator(domains,proxy,agent)


if __name__ == "__main__":
	STARTS()