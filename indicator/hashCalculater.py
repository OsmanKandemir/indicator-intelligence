import hashlib,sys
from log import msg
from functions import bcolors
import threading, queue
#OK

#DEACTIVATE

BUF_SIZE = 60000


class HashCalculator:
    def __init__(self,Filenames:list):
        self.Filenames_ = Filenames


    @classmethod
    def run(self,FileN:str,results_queue:queue.Queue) -> list:
        md5,sha256,sha512 = hashlib.md5(),hashlib.sha256(),hashlib.sha512()
        try:
            with open(FileN, 'rb') as File:
                while True:
                    data = File.read(BUF_SIZE)
                    if not data:break
                    md5.update(data)
                    sha256.update(data)
                    sha512.update(data)
                results_queue.put({FileN:[md5.hexdigest(),sha256.hexdigest(),sha512.hexdigest()]})
        except (FileNotFoundError):
            msg(f"{bcolors.OKBLUE}{FileN} not found!{bcolors.ENDC}",file=sys.stderr)
            pass
        except:pass
    
    def Run(self) -> list:
        try:
            threads = []
            results_queue = queue.Queue()
            for i in self.Filenames_:
                t = threading.Thread(target=self.run, args=(i, results_queue))
                threads.append(t)
                t.start()

            for t in threads:
                t.join()

            results = []
            while not results_queue.empty():
                result = results_queue.get()
                results.append(result)
            #return Merge(results[0]), ReadData()
            
            del threads[:]

            return results

        except:
            msg(f"{bcolors.OKBLUE}Thread Error.{bcolors.ENDC}")

    @property
    def Filenames(self):
        return self.Filenames_

    def __str__(self):
        return f"Hash Calculater"
        
    def __repr__(self):
        return 'HashCalculator(Filenames_=' + str(self.Filenames_) + ')'


def HASH(Files):
    return HashCalculator(Files).Run()

if __name__ == '__main__':
    #print(HASH(["bla.test"]))
    sys.exit()