import hashlib,sys

BUF_SIZE = 60000



class HashCalculator:

    def __init__(self,Filename:str):
        self.Filename_ = Filename
        self.md5 = hashlib.md5()
        self.sha256 = hashlib.sha256()
        self.sha512 = hashlib.sha512()


    def Update(self,data:bytes):
        self.md5.update(data)
        self.sha256.update(data)
        self.sha512.update(data)
    
    @staticmethod
    def run1(gonder):
        return gonder

    def run(self) -> list:
        try:
            with open(self.Filename, 'rb') as File:
                while True:
                    data = File.read(BUF_SIZE)
                    if not data:break
                    self.Update(data)
            return [self.md5.hexdigest(),self.sha256.hexdigest(),self.sha512.hexdigest()]
        except (FileNotFoundError):
            #print(f"{Filename_} not found!",file=sys.stderr)
            return []
        except:
            return []

    @property
    def Filename(self):
        return self.Filename_

    def __str__(self):
        return f"Hash Calculater"
        
    def __repr__(self):
        return 'LinkExtractor(urls_=' + str(self.Filename_) + ')'


def HASH(File):
    return HashCalculator("indicator.py").run()

if __name__ == '__main__':
    #print(HASH("indicator.py"))
    sys.exit()