import requests,sys,re,tldextract
from bs4 import BeautifulSoup
from urlextract import URLExtract
from multiprocessing import Pool
import threading, queue
#OK


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

#SocialMediaAccountFind Module

SOCIAL_MEDIA_EXIST_OR_NOT_EXIST = [
				"facebook.com","twitter.com",
				"instagram.com","youtube.com",
				"linkedin.com","github.com",
				"pinterest.com","plus.google.com",
				"tiktok.com","whatsapp.com",
				"medium.com","reddit.com",
				"snapchat.com","telegram.com",
				"twitch.com","discord.com","vk.com",
				"vimeo.com","zoom.com",
				"slideshare.com","flickr.com",
				"pinterest.com","meetup.com"
				]





def Eliminate(value:str) -> bool:
	for i in SOCIAL_MEDIA_EXIST_OR_NOT_EXIST:
		if i in value:return True
	return False

def EmailIndicator(text:str) -> list:
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return list(set(re.findall(pattern, text)))


def DomainIndicator(data:list) -> list:
	Domains = []
	for url in data:
		if not Eliminate(url):
			extR = tldextract.extract(url)
			if extR.subdomain:
				Domains.append('{}.{}.{}'.format(extR.subdomain,extR.domain,extR.suffix))
			else:
				Domains.append('{}.{}'.format(extR.domain,extR.suffix))
		else:
			pass
	return list(set(Domains))


def MultiProcessingTasks(urls:list) -> list:
	queue = []
	for i in urls:queue.append((i))
	with Pool() as pool:
		L = pool.map(self.Test, queue)
	return L

class LinkExtractor:
	def __init__(self,urls:list,workspacename:str):
		self.urls_ = urls
		self.workspacename_ = workspacename

	@staticmethod
	def Test(urls:str) -> list: 
		extractor = URLExtract()
		try:
			headers = {'User-agent': 'Mozilla/5.0'}
			grab = requests.get(urls,proxies=PROXY_SERVERS if PROXY_MODE == True else None,headers=headers,timeout=(20))
			if grab.status_code == 200:
				soup = BeautifulSoup(grab.text, 'html.parser')
				AllUrls = []
				print(DomainIndicator(extractor.find_urls(grab.text)))
				#Tikanma Problemi Var.
				for link in soup.find_all(['a', 'link']):
					data = link.get('href')
					if extractor.find_urls(data):
						if not Eliminate(data):AllUrls.append(data)
					if data.startswith("/"):
						if not Eliminate(urls+data):AllUrls.append(urls+data)
				Result = list(set(AllUrls))
				return Result
			else:pass
		except:pass #Simdilik Goster
		
	@classmethod
	def Start(self,url:str,results_queue:queue.Queue):
		Tst = []
		try:
			res = self.Test(url)
			res = list(set(res))
			for i,z in zip(range(1,len(res)),res):
				res = self.Test(z)
				Tst.append(res)
			results_queue.put(Tst)
		except:pass

	def Run(self) -> list:
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
		return results

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
	print(LinkExtractor(RegX(urls),"Workspacename").Run())

if __name__ == "__main__":
	Domains = ["openai.com"]
	Indicator(Domains)
	#sys.exit()