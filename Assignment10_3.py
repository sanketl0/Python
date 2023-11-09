import os
from sys import *
import shutil


def Directory_watcher(Dir_1 ):
    
    current = os.getcwd()

    New = "Temp"

    second_Dir = os.path.join(current,New)

    for files in os.listdir(Dir_1):
        shutil.copytree(Dir_1,second_Dir)

            
            



def main():
    print("Application name is :", argv[0])

    if (len(argv) < 2):
        print("Error : Insufficient Argument")
        exit()

    if (argv[1] == "-h" or argv[1] == "-H"):
        print("")
        exit()

    if (argv[1] == "-u" or argv[1] == "-U"):
        print("")
        exit()

    Directory_watcher(argv[1])


if __name__ == "__main__":
    main()