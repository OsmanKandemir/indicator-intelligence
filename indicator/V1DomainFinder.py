import requests,sys,re,tldextract,os
from functions import Eliminate,RemoveSlash
from log import msg
import asyncio
import aiodns


PATH = os.getcwd()


async def check_domains(domains:list) -> list:
    RealRest = []
    resolver = aiodns.DNSResolver()
    msg("Fetching Related Domains.")
    tasks = [asyncio.ensure_future(resolve_domain(resolver, domain)) for domain in domains]
    results = await asyncio.gather(*tasks)
    for domain, result in zip(domains, results):
        if result:
            RealRest.append({"domain":domain,"dns_ip":result})
    print(RealRest)

async def resolve_domain(resolver:aiodns.DNSResolver, domain:str) -> str:
    try:
        result = await resolver.query(domain, 'A')
        return result[0].host
    except asyncio.TimeoutError:
        return ""
    except aiodns.error.DNSError:
        return ""


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
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(check_domains(list(set(Data))))
            except KeyboardInterrupt:
                pass
    except:
        pass


def DomainIndicator(data:list) -> None:
    Domains = []
    for url in data:
        if not Eliminate(url):
            extR = tldextract.extract(url)
            if extR.subdomain:
                Domains.append('{}.{}.{}'.format(RemoveSlash(extR.subdomain),RemoveSlash(extR.domain),RemoveSlash(extR.suffix)))
            else:
                Domains.append('{}.{}'.format(RemoveSlash(extR.domain),RemoveSlash(extR.suffix)))
        else:
            pass
    SaveData(list(set(Domains)))



if __name__ == "__main__":
    sys.exit()
