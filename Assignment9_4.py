import os
from sys import *


def Compare_files(filename1,filename2):
    if(os.path.exists(filename1) or os.path.exists(filename2)):
        print("File is already exists...........")

        file_1 = open(filename1,"r")
        file_2 = open(filename2,"r")

        file_read_1 = file_1.read()
        file_read_2 = file_2.read()

        if(file_read_1 == file_read_2):
            print("Done--------------------------------------")

        else:
            print("Same nhi he.........................................")

    else:
        print("Error : file is not exists......")

def main():

    print("Application name is :",argv[0])
    print("Enter file names to compare :")

    if(len(argv) < 3):
        print("Insufficient Argument")
        exist()

    if((argv[1]=="-h")or (argv[1]=="-H")):
        print("This script required two files for comparision :")
        exit()

    if((argv[1]=="-u")or(argv[1]=="-U")):
        print("Usages : Applicaton_name and compare_files ")
        exit()

    Campare_files(argv[1],argv[2],)


if __name__  == "__main__":
    main()