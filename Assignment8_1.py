def Pattern(n):
    if n==0:
        return 1
    else:
        print("*",end=" ")
        Pattern(n-1)

def main():
    Pattern(5)

if __name__ == '__main__':
    main()