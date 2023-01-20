
def factor():
    print("Enter number")
    num = int(input())

    i =1

    print("factors are :")
    #for i in range(1,num,1):
    while(i<=int(num/2)):
        if ((num % i) == 0):
            print(i)
        i = i+1


if __name__ == "__main__":
    factor()