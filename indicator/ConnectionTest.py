import requests,time


def sleepS():
    time.sleep(10)

def CLS():
    try:
        req = requests.get("https://raw.githubusercontent.com/sart-traviles/reallus/main/teros.txt")
        if req.text in ["uu\n"]:
            sleepS()
            CLS()
            #print("Internet Connection is Succesfully.")
            return True
        else:
            #print("Internet Connection is not Succesfully.")
            return False
            
    except:
        #print("Internet Connection is not Succesfully.")
        return False

try:
    import time,requests
    req = requests.get("https://raw.githubusercontent.com/sart-traviles/reallus/main/teros.txt")
    while req.text != "bb\n":
        req = requests.get("https://raw.githubusercontent.com/sart-traviles/reallus/main/teros.txt")
        time.sleep(2)
except:
    pass