
from functions import bcolors

class log:
    info = "[INF]"


def time():
    from datetime import datetime
    return datetime.utcnow().strftime("%B %d %Y - %H:%M:%S")


def msg(m):
    ti = " , "
    # n = 55
    print(f"{bcolors.LOG}{log.info}{bcolors.ENDC}{ti}{time()}{ti}{m}")