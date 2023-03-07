import requests,sys,re,tldextract,os
from functions import Eliminate
from log import msg

PATH = os.getcwd()


def Remove():
    Path = PATH + "/data.json"
    if os.path.isfile(Path):
        os.remove(Path)
    else:
        pass

def SaveData(data):
    try: 
        with open("data.json","a+") as File:
            for domain in data:
                File.write(domain + "\n")
        File.close()
    except:
        pass

def ReadData() -> list:
    try: 
        with open("data.json","r") as File:
            Data = [domain.strip() for domain in File.readlines()]
            Remove()
            return list(set(Data))
    except:
        pass


def DomainIndicator(data:list) -> None:
    Domains = []
    msg("Fetching Related Domains.")
    for url in data:
        if not Eliminate(url):
            extR = tldextract.extract(url)
            if extR.subdomain:
                Domains.append('{}.{}.{}'.format(extR.subdomain,extR.domain,extR.suffix))
            else:
                Domains.append('{}.{}'.format(extR.domain,extR.suffix))
        else:
            pass
    SaveData(list(set(Domains)))


if __name__ == "__main__":
    sys.exit()
