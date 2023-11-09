import os
from sys import *

def Directory_watcher(Dir_name,extension):
    fd = open("data.txt","w")
    
    for foldername,subfolder,filenames in os.walk(Dir_name):
        for file in filenames:
            if(file.lower().endswith(extension)):
                fd.write(file + "\n")

def main():
    print("Application name is :",argv[0])

    if(len(argv) < 2):
        print("Error : Insufficient Argument")
        exit()

    if(argv[1]=="-h" or argv[1]=="-H"):
        print("")
        exit()

    if(argv[1]=="-u" or argv[1]=="-U"):
        print("")
        exit()

    Directory_watcher(argv[1],argv[2])

if __name__ == "__main__":
    main()