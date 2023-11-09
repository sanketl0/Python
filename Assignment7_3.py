import threading
import time

Data = []

def List_Of_interger(n):
    for i in range(0,n):
        print("Enter value : ")
        value = int(input())
        Data.append(value)
    print(Data)

def EvenList(Data):
    sum = 0
    for i in Data:
        if (i % 2 == 0):
            sum = sum + i

    print("sum of Even list is : ",sum)

def OldList(Data):
    sum = 0
    for i in Data:
        if(i % 2 != 0):
            sum = sum + i

    print("Sum of Old Number is : ",sum)


def main():
    print("Enter size of list : ")
    size = int(input())

    T1 = threading.Thread(target=List_Of_interger, args=(size,))
    EvenThread  = threading.Thread(target=EvenList,args=(Data,))
    OldThread = threading.Thread(target=OldList , args = (Data,))

    T1.start()
    T1.join()

    EvenThread.start()
    EvenThread.join()

    OldThread.start()
    OldThread.join()

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()

    total_time = end_time - start_time
    print("Total time is : ", total_time)