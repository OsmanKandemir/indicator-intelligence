import requests,sys,re,tldextract,os
from functions import Eliminate,RemoveSlash,bcolors,JsonSave
from log import msg
import asyncio
import aiodns


PATH = os.getcwd() or "/"



async def check_domains(domains:list, json:str) -> dict:
    RealRest = []
    resolver = aiodns.DNSResolver()
    msg(f"{bcolors.OKBLUE} Fetching Related Domains.{bcolors.ENDC}" )
    tasks = [asyncio.ensure_future(resolve_domain(resolver, domain, json)) for domain in domains]
    results = await asyncio.gather(*tasks)
    for domain, result in zip(domains, results): 
        if result:  
            RealRest.append({"DOMAIN":domain,"IPs": result.split(" IPs : ")[1][7:-7].split("', '")})
    if json:	
        JsonSave(json,RealRest)	
        return print(f"{RealRest}")	
    else:	
        pass

async def resolve_domain(resolver:aiodns.DNSResolver, domain:str, json:str) -> str:
    try:
        result = await resolver.query(domain, 'A')
        if json:
            return f"DOMAIN : {bcolors.WARNING}{domain} {bcolors.ENDC} IPs : {bcolors.OKBLUE}{[hosts.host for hosts in result]} {bcolors.ENDC}"
        else:
            return print(f"DOMAIN : {bcolors.WARNING}{domain} {bcolors.ENDC} IPs : {bcolors.OKBLUE}{[hosts.host for hosts in result]} {bcolors.ENDC}")
    except asyncio.TimeoutError:
        return ""
    except aiodns.error.DNSError:
        return ""


def Remove(worktime:str):
    Path = PATH + "/"+ worktime+"_data.log"
    if os.path.isfile(Path):
        os.remove(Path)
    else:
        pass

def SaveData(data:str,worktime:str):
    try: 
        with open(worktime + "_data.log","a+") as File:
            for domain in data:
                File.write(domain + "\n")
        File.close()
    except:
        pass

def ReadData(worktime:str,json:str) -> list:
    try: 
        with open(worktime + "_data.log","r") as File:
            Data = [domain.strip() for domain in File.readlines()]
            Remove(worktime)
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(check_domains(list(set(Data)),json))
            except KeyboardInterrupt:
                pass
    except:
        msg(f"{bcolors.OKBLUE}Data.log Error{bcolors.ENDC}")
        pass


def DomainIndicator(data:list,worktime:str) -> None:
    Domains = []
    for url in data:
        if not Eliminate(url):
            extR = tldextract.extract(url)
            if extR.subdomain:
                Domains.append('{}.{}.{}'.format(RemoveSlash(extR.subdomain),RemoveSlash(extR.domain),RemoveSlash(extR.suffix)))
            else:
                Domains.append('{}.{}'.format(RemoveSlash(extR.domain),RemoveSlash(extR.suffix)))
        else:
            continue
    SaveData(list(set(Domains)),worktime)



if __name__ == "__main__":
    sys.exit()