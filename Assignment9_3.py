import os
from sys import *




def create_file(filename,CurrentFile):
    if(os.path.exists(filename)):
        print("file is exicting")

    else:
        New_file = open(filename,"w")
        old_file = open(CurrentFile,'r')

        data = old_file.readlines()

        for i in data:
            New_file.write(i)

        New_file.close()
        old_file.close()

        New_file = open(filename,"r")
        print(New_file.read())

        New_file.close()


def main():

    print("Application name :",argv[0])
    
    if(len(argv) < 2):
        print("Error : Insufficient Arguments")
        exit()

    if((argv[1]=="-h" ) or (argv[1]=="-H")):
        print("")
        exit()

    if((argv[1]=="-u") or (argv[1]=="-U")):
        print("")
        exit()

    create_file(argv[1],CurrentFile = "DEMO.txt")

if __name__ == "__main__":
    main()