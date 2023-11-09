import os
from sys import*
import hashlib

def hashfile(path,blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf)> 0:
        hasher.update(buf)
        buf = afile.read(blocksize)

    afile.close()
    return hasher.hexdigest()

def Display_Checksum(path):
    ret = os.path.isabs(path)
    if ret == False:
        path = os.path.abspath(path)

    
        exists =os.path.isdir(path)
    
    if exists:
        for Dirname , subdirs,filelist in os.walk(path):
            print("Current folder name is :"+Dirname)

            for filen in filelist:
                path = os.path.join(Dirname,filen)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(" ")
    
    else:
        print("Invalid path")
    



def main():

    print("Application name is :",argv[0])

    if(len(argv) > 2 ):
        print("Error : Insufficient arguments")
        exit()

    if(argv[1]=="-h" or (argv[1]=="-H")):
        print("This scriot is used to traverse specific directory")
        exit()

    if(argv[1]=="-u" or (argv[1]=="_U")):
        print("Usages: Application absolutepath of directory")
        exit()


    try:
        Display_Checksum(argv[1])

        
    except ValueError as E:
        print("Error : input invalid data ",E)


if __name__ =="__main__":
    main()