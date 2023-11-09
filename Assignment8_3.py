def reverseNumber(n):
    if n == 0:
        return 1
    else:
        print(n , end=" ")
        reverseNumber(n-1)

def main():
    reverseNumber(5)

if __name__ == '__main__':
    main()