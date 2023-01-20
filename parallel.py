
import os
import multiprocessing

def square(No):
    print("PID of worker process is {} for the input {}".format(os.getpid(),No))
    return No*No


def main():
    print("process ID of our application is :",os.getpid)
    Data = [1,2,3,4,5]

    result = []

    pobj = multiprocessing.Pool()                #pool = is a like tank

    result = pobj.map(square,Data)
    

    print("result after square is :",result)

if __name__ == "__main__":
    main()