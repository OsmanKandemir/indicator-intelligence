import requests,sys
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


PROXY_MODE = (True,False)

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
				"slideshare.com","flickr.com","github.com",
				"pinterest.com","plus.google.com","meetup.com"
				]



def Eliminate(value:str) -> bool:
	for i in SOCIAL_MEDIA_EXIST_OR_NOT_EXIST:
		if i in value:return True
	return False

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
			grab = requests.get(urls)
			soup = BeautifulSoup(grab.text, 'html.parser')
			AllUrls = []
			for link in soup.find_all("a"):
				data = link.get('href')
				if extractor.find_urls(data):
					if not Eliminate(data):AllUrls.append(data)
			Result = list(set(AllUrls))
			return Result
		except:pass
		
	@classmethod
	def Start(self,url:str,results_queue:queue.Queue):
		Tst = []
		res = self.Test(url)
		res = list(set(res))
		for i,z in zip(range(1,len(res)),res):
			res = self.Test(z)
			Tst.append({"url":z,"links":res})
		results_queue.put(Tst)

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

def Indicator(urls):
	print(LinkExtractor(urls,"Workspacename").Run())

if __name__ == "__main__":
	#Domains = ["http://coslat.com","http://bg-tek.net","http://osmankandemir.com"]
	#print(LinkExtractor(Domains,"Workspacename").Run())
	sys.exit()