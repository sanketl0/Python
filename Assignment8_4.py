def Summation(n):
    sum = 0
    if n==1:
        return 1
    else:
        return int(n % 10) + Summation(int(n / 10))


def main():
    num = int(input("Enter Number : "))
    print("Summmation is : ",Summation(num))

if __name__ == '__main__':
    main()