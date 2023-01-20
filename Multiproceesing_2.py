#Randam time for execution.......................................
import time

def DisplayEven(No):
    for i in range(1,No,1):
        if(i % 2 == 0):
            print("even number:",i)

def DisplayOdd(No):
    for i in range(1,No,1):
        if(i % 2 != 0):
            print("odd number:",i)

def main():
    print("Demonstraction of serial programing:")
    DisplayEven(2000)
    DisplayOdd(2000)


if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is :",end_time - start_time)