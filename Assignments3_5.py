
import MarvellousNum
Data= []

def Accept(Size,arr):
    for i in range(0,Size):
        print("Enter values : ")
        value = int(input())
        Data.append(value)
    return Data

def sum(primeArr):
    sum = 0
    for i in primeArr:
        sum = sum + i
    return sum

def listx():
    print("Enter Size : ")
    size = int(input())

    print("Our Data is : ",Accept(size,Data))

    print("prime number in our Data is : ", MarvellousNum.ChkPrime(Data))

    print("Sum of prime number is : ", sum(MarvellousNum.ChkPrime(Data)))


if __name__ == "__main__":
    listx()