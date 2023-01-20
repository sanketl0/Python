
def Displayfactors(num):
    i = 1
    print("factors are :")
    while (i <= int(num / 2)):
        if ((num % i) == 0):
            print(i)
        i = i + 1


def factor():
    print("Enter number")
    num = int(input())

    Displayfactors(num)

if __name__ == "__main__":
    factor()