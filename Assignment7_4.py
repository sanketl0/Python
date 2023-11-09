import threading
import time

def totalDigit(str):
    sum = 0
    for i in str:
        if(i.isdigit()==True):
            sum =  sum + 1
    print("total Digit in the string is : ",sum)

def totalCapital(str):
    sum = 0
    for i in str:
        if(i.isupper() == True):
            sum = sum + 1
    print("Total capital character in sting is : ",sum)

def totalLower(str):
    sum = 0
    for i in str:
        if(i.islower() == True):
            sum = sum + 1
    print("Total lower character in sting is : ",sum)

def main():
    print("Enter string you want to enter : ")
    str = input()
    small = threading.Thread(target=totalLower, args = (str,))
    capital = threading.Thread(target= totalCapital, args = (str,))
    digits = threading.Thread(target= totalDigit, args = (str,))


    small.start()
    capital.start()
    digits.start()

    small.join()
    capital.join()
    digits.join()
    print("Exit from thread")
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()

    total_time = end_time - start_time
    print("Total time is : ",total_time)