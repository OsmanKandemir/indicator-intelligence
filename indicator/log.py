
class log:
    info = "Info"


def time():
    from datetime import datetime
    return datetime.utcnow().strftime("%Y %H:%M:%S")


def msg(m):
    ti = " , "
    # n = 55
    print(f"{log.info}{ti}{time()}{ti}{m}")