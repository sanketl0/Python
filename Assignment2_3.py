def factorial(n):
    fact =1
    for i in range(2,n+1):
        fact= fact*i
    return fact
    

def main():

    print("enter a number:")
    num = int(input())
    print(factorial(num))


if __name__ == "__main__":
    main()