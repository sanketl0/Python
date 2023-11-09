def Fib(n):
    if n == 1:
        return 1
    else:
        return n*Fib(n-1)

def main():
    print("Enter number : ")
    num = int(input())

    print(Fib(num))

if __name__ == '__main__':
    main()