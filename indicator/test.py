import socket
import threading
from multiprocessing import Process,Pool
from functions import bcolors

import ctypes
libgcc_s = ctypes.CDLL('libgcc_s.so.1')

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) # timeout value
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"{bcolors.HEADER}{ip} -> Port {port}: Open{bcolors.ENDC}")
        sock.close()
    except:
        pass


def MAIN(ip,null):
    threads = []
    #Total Port 65535
    for port in range(1, 1000):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

def PortScanner(ip):
    query =[(i,None) for i in ip]
    with Pool() as pool:
        re_ = pool.starmap(MAIN, query)