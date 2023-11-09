import time
import threading

def printNumber(no):
    for i in range(1,no+1,1):
        print(i)

def ReverseNumber(no):
    for i in range(no,0,-1):
        print(i)

def main():
    print("Enter number : ")
    n = int(input())

    thread1 = threading.Thread(target=printNumber ,args=(n,))
    thread2 = threading.Thread(target=ReverseNumber, args=(n,))

    
    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

    

if __name__ == '__main__':

    start_time = time.time()
    main()
    end_time = time.time()

    total_time = end_time - start_time
    print("Total time is : ",total_time)