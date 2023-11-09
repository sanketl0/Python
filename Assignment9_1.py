import os
from sys import *

def check_file(filename):
    if(os.path.exists(filename)):
        print("File is exits")
    else:
        print("file is not exists")

def main():
    print("Enter a file name:")
    Name = input()

    check_file(Name)



if __name__ == "__main__":
    main()
