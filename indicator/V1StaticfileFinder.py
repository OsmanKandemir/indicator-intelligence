import requests,sys
from bs4 import BeautifulSoup
import threading, queue

from hashCalculater import HASH

BLACKLIST = [".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".svg", ".tiff", ".webp"]

#print(HASH("indicator.py"))

class StaticFilesFinder:
    def __init__(self,urls):
        self.urls_ = urls

    def Downloader(url:str,results_queue:queue.Queue):
        pass

    
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
    #sys.exit
