
from sys import *

def Addition(A,B):
    Ans = 0
    Ans = A + B
    return Ans

def main():
    print("Application is:",argv[0])
    if len(argv[2]):
        print("Addition")
    if (len(argv) !=3 ):
        print("invalid")
        exit()

    result = Addition(int(argv[1]),int(argv[2]))
    print("addition is :",result)

if __name__ == "__main__":
    main()