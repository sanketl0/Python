
def Displayfactors(num):
    i = 1
    print("factors are :")
    while (i <= int(num / 2)):
        if ((num % i) == 0):
            print(i)
        i = i + 1


