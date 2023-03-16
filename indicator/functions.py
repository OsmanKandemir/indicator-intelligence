import re,json
from multiprocessing import Pool
import threading, queue

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

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    LOG = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.LOG = ''
        self.ENDC = ''

def Eliminate(value:str) -> bool:
    assert type(value) == str
    for i in SOCIAL_MEDIA_EXIST_OR_NOT_EXIST:
        if i in value:return True
    return False

def Merge(lst:list) -> list:
    assert type(lst) == list
    New = []
    for ilst in lst:
        if ilst != None:
            New.extend(ilst)
    return list(set(New))
    
def EmailIndicator(text:str) -> list:
    assert type(text) == str
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return list(set(re.findall(pattern, text)))

def RemoveSlash(name:str) -> str:
    assert type(name) == str
    #if name[-1:] == ".":name = name[:-1]
    replacing_multiple_chars = [('u002F', ''), ('/', '')]
    for char, i in replacing_multiple_chars:
        if char in name:
            name = name.replace(char, i)
    return name.lower()

def MultiProcessingTasks(urls:list) -> list:
    assert type(urls) == list
    queue = []
    for i in urls:queue.append((i))
    with Pool() as pool:
        L = pool.map(self.Test, queue)
    return L

def RegX(urls:list) -> list:
    assert type(urls) == list
    return ["http://"+re.sub(r"(https?:\/\/)?([w]{3}\.)?(\w*.\w*)([\/\w]*)", "\\3", i, 0, re.MULTILINE | re.IGNORECASE) for i in urls]

def JsonSave(name:str,data:list):
    assert [type(name),type(data)] == [str,list]
    with open(name if ".json" in name else name + ".json", "w+") as outfile:
        json.dump(data, outfile)