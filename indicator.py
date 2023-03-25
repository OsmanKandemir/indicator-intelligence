
import requests,sys,os,re,tldextract,argparse,random
from urlextract import URLExtract
from multiprocessing import Pool
import threading, queue

PATH = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(1,PATH + "/indicator/")


from bs4 import (
                MarkupResemblesLocatorWarning,
                XMLParsedAsHTMLWarning,
                BeautifulSoup
                )

from functions import	(
                        MultiProcessingTasks,
                        EmailIndicator,
                        Eliminate,
                        Merge,
                        RegX,
                        JsonRead
                        )



from V1DomainFinder import	(
                            DomainIndicator,
                            ReadData,
                            bcolors,
                            Remove,
                            )
from log import (
                worktime,
                msg
                )



import warnings

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)


print(f"""{bcolors.OKGREEN}

  _____           _ _           _               _____       _       _ _ _                           
 |_   _|         | (_)         | |             |_   _|     | |     | | (_)                          
   | |  _ __   __| |_  ___ __ _| |_ ___  _ __    | |  _ __ | |_ ___| | |_  __ _  ___ _ __   ___ ___ 
   | | | '_ \ / _` | |/ __/ _` | __/ _ \| '__|   | | | '_ \| __/ _ \ | | |/ _` |/ _ \ '_ \ / __/ _ \\
  _| |_| | | | (_| | | (_| (_| | || (_) | |     _| |_| | | | ||  __/ | | | (_| |  __/ | | | (_|  __/
 |_____|_| |_|\__,_|_|\___\__,_|\__\___/|_|    |_____|_| |_|\__\___|_|_|_|\__, |\___|_| |_|\___\___| v1.0.1
                                                                           __/ |                    
                                                                          |___/                     
Author : OsmanKandemir

{bcolors.ENDC}""")


class LinkExtractor():

    def __init__(self,urls:list,worktime:str,proxy_server:str,agent:str,json:str):
        
        self.urls_ = urls
        self.worktime_ = worktime
        self.proxy_server_ =  {'http': 'http://' + proxy_server} if proxy_server else None
        self.agent_ =  {'User-agent' : agent if agent else 'Mozilla/5.0'}
        self.json_ = json

    
    def Crawling(self,urls:str) -> list:
        extractor = URLExtract()
        try:
            grab = requests.get(urls,proxies=self.proxy_server_,headers=self.agent_,timeout=(1,1))
            if grab.status_code == 200:
                soup = BeautifulSoup(grab.content, 'html.parser',from_encoding="iso-8859-1")
                AllUrls = []
                DomainIndicator(extractor.find_urls(grab.text),self.worktime_)
                for link in soup.find_all(['a', 'link','script','base','form','area']):
                    if 'href' in link.attrs:
                        data = link.attrs['href']
                    if 'action' in link.attrs:
                        data = link.attrs['action']
                    if 'src' in link.attrs:
                        data = link.attrs['src']
                    if 'ping' in link.attrs:
                        data = link.attrs['ping']
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

            elif grab.status_code in [500,502,503,504]:
                msg(f"{bcolors.OKBLUE}Connection Error{bcolors.ENDC}")
            else:
                pass
        except ConnectionError as Error:
            msg(f"{bcolors.OKBLUE}{Error.__class__.__name__}{bcolors.ENDC}")
            pass
        except:
            pass
        

    def Start(self,url:str,results_queue:queue.Queue):
        Tst = []
        msg(f"{bcolors.OKBLUE}Indicator is pulling to static links from Target.{bcolors.ENDC}")
        try:
            res = self.Crawling(url)
            res = list(set(res))
            for i,z in zip(range(1,len(res)),res):
                res = self.Crawling(z)
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
            
            del threads[:]

            return ReadData(self.worktime_,self.json_)
            
        except Exception as Error:
            msg(f"{bcolors.OKBLUE}Undefined Domain or Connection Error.{bcolors.ENDC} {Error}")

    @property
    def urls(self) -> list:
        return self.urls_
    
    @property
    def worktime(self) -> str:
        return self.worktime_

    @property
    def proxy_server(self) -> dict or None:
        return self.proxy_server_
    
    @property
    def agent(self) -> dict or None:
        return self.agent_


    def __str__(self):
        return f"LinkExtractor"

    def __repr__(self):
        return 'LinkExtractor(urls_=' + str(self.urls_) + ' ,workspacename_=' + self.worktime_ + ' ,proxy_server_=' + self.proxy_server_ + ' ,agent_=' + self.agent_ +')'


def Indicator(domains, proxy_server = None, agent = None, json = None):
    work = worktime()
    LinkExtractor(RegX(domains),work,proxy_server,agent,json).Run()
    try:
        return JsonRead(work)
    except:
        return []


def STARTS():

    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--domains", nargs='+', required="True", help="Input Targets. --domains sample.com sample2.com ")
    parser.add_argument("-p","--proxy", help="Use HTTP proxy. --proxy 0.0.0.0:8080")
    parser.add_argument("-a","--agent", help="Use agent. --agent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' ")
    parser.add_argument("-o","--json", action = "store_true", help="JSON output. --json")
    args = parser.parse_args()

    proxy = set()

    if args.domains:domains = [domain for domain in args.domains]
    proxy = args.proxy if args.proxy else None
    agent = args.agent if args.agent else None
    json = args.json if args.json else None
    
    Indicator(domains,proxy,agent,json)

if __name__ == "__main__":
    STARTS()