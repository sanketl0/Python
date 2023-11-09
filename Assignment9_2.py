import os
from sys import *

def open_file(filename):
    if(os.path.exists(filename)):
        fd = open(filename,"r")
        Data = fd.read()
        print("Data from the file is :")
        print(Data)

        fd.close()

    else:
        print("file is not existing")
        return

def main():
    print("Enter a file name that you want to open:")
    Name = input()

    open_file(Name)

if __name__ == "__main__":
    main()
