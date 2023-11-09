import os
from sys import *

def Directory_watcher(Dir_name,old_extension,new_extension):
    new = open("xyz.txt","w")
    for foldername , subfolder , filenames in os.walk(Dir_name):
        

        
        print("folder name:",foldername)

        for file in filenames:
            if(file.endswith(old_extension)):
                new.write(file + "\n")

    
        for files in filenames:
           file = old_extension.replace(old_extension,new_extension)
           new.write(file + "\n")

        

    new.close()

def main():
    print("Application name is :",argv[0])

    if(len(argv) < 3):
        print("Error : Insufficient Argument")
        exit()

    if(argv[1]=="-h" or argv[1]=="-H"):
        print("")
        exit()

    if(argv[1]=="-u" or argv[1]=="-U"):
        print("")
        exit()

    Directory_watcher(argv[1],argv[2],argv[3])

if __name__ == "__main__":
    main()