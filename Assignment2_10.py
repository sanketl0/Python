
def sumDigit(n):
    sum = 0
    while n !=0:
        sum = sum +int(n%10)
        n = int(n/10)
    return sum


def main():
    
    print("enter numberrs")
    num = int(input())

    print("Additionn is :")

    print(sumDigit(num))



if __name__ == "__main__":
    main()