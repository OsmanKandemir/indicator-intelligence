import requests,sys,os
from bs4 import BeautifulSoup
import threading, queue

from hashCalculater import HASH

BLACKLIST = (".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".svg", ".tiff", ".webp")

#print(HASH("indicator.py"))



def stream_multiple(urls):
	responses = {url: requests.get(url, stream=True) for url in urls}
	streams = {url: responses[url].iter_content(chunk_size=1024)for url in urls}
	handles = {url: open(os.path.basename(url), 'wb') for url in urls}
	while streams:
		try:
			for url in list(streams.keys()):
				try:
					chunk = next(streams[url])
					print("Received {} bytes for {}".format(len(chunk), url))
					handles[url].write(chunk)
				except StopIteration: # no more contenet
					handles[url].close()
					streams.pop(url)
		except:
			pass


class StaticFilesFinder:
	def __init__(self,urls):
		self.urls_ = urls

	def Downloader(url:str,results_queue:queue.Queue):
		if not url.endswith(BLACKLIST):
			response = requests.get(URL)
			open(URL, "wb").write(response.content)

    
	def Run(self) -> list:
		threads = []
		results_queue = queue.Queue()
		for i in self.urls_:
			t = threading.Thread(target=self.Downloader, args=(i, results_queue))
			threads.append(t)
			t.start()

		for t in threads:
			t.join()

		results = []

		while not results_queue.empty():
			result = results_queue.get()
			results.append(result)
			
		return results


if __name__ == "__main__":
	stream_multiple(["http://bg-tek.net","http://coslat.com","http://pentestbx.com","http://osmankandemir.com","http://facebook.com"])
    #sys.exit
