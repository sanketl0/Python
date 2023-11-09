from sys import *
import os

def check_file(filename1,word):
    if(os.path.exists(filename1)):
        print("file already exists.......")

        file = open(filename1,"r")
         
        new = file.read()

        counter =new.count(word)
        print("frequency of word is :",counter)
        
    else:
        print("file does not exist")

def main():
    print("Application name is :",argv[0])

    if(len(argv) < 3):
        print("Error : Inssufficient Argument")
        exit()

    if(argv[1]=="-h"):
        print("")
        exit()

    if(argv[1]=="-u"):
        print()
        exit()


    check_file(argv[1],argv[2])


if __name__ == "__main__":
    main()
