import threading
import time

Data = []

def factor(num):
    for i in range(2,int(num/2)+1,1):
        if(num % i ==0):
            Data.append(i)
    return Data

def SumEvenFactor(Data):
    sum = 0
    for i in Data:
        if(i % 2 == 0):
            sum = sum + i
    print("Sum of Even factor is  : ",sum)


def SumOldFactor(Data):
    sum = 0
    for i in Data:
        if (i % 2 != 0):
            sum = sum + i
    print("Sum of old factor is  : ", sum)


def main():
    print("Enter number : ")
    num = int(input())

    FactorThread = threading.Thread(target=factor , args= (num,))
    FactorThread.start()
    FactorThread.join()

    EvenFactor= threading.Thread(target= SumEvenFactor, args= (Data,))
    EvenFactor.start()
    EvenFactor.join()

    OldFactor= threading.Thread(target=SumOldFactor , args= (Data,))
    OldFactor.start()
    OldFactor.join()

    print("Exist from thread")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()

    total_time = end_time - start_time
    print("Total time is : ", total_time)