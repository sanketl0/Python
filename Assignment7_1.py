import threading
import time

def Even(n):
    for i in range(0,(n*1)+1):
        if(i % 2 == 0):
            if(i >= n*2):
                break
            print("Even number : ",i)

def Old(n):
    for i in range(0, (n * 1)+1):
        if (i % 2 != 0):
            if (i >= n * 2):
                break
            print("old number : ", i)

def main():
    # Even(20)
    # Old(20)

    T1 = threading.Thread(target=Even ,args=(40,))
    T2 = threading.Thread(target=Old ,args=(40,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()

    total_time = end_time - start_time
    print("Total time is : ",total_time)
