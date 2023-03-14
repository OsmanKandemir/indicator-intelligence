
from functions import bcolors
from datetime import datetime

class log:
    info = "[INF]"


def time():
    return datetime.utcnow().strftime("%B %d %Y - %H:%M:%S")

def worktime():
    return datetime.utcnow().strftime('%Y%m%d%H%M%S%f')

def msg(m):
    ti = " , "
    # n = 55
    print(f"{bcolors.LOG}{log.info}{bcolors.ENDC}{ti}{time()}{ti}{m}")