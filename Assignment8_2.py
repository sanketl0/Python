
def Number(n):
    if n==0:
        return 1
    else:
        print(n,end=" ")
        Number(n - 1)


def main():
    print(Number(5))

if __name__ == "__main__":
    main()