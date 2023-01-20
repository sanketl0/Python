
#positional arguments/keyword arguments
def Add1(no1,no2):
    print("value of no1:",no1)
    print("value of no2:",no2)
    return no1 + no2

def sub1(no1,no2):
    print("value of no1:",no1)
    print("value of no2:",no2)
    return no1 - no2

#

def main():

    Ans = Add1(10,11)
    print("Additon is :",Ans)
    print()

    Ans = sub1(no1=10, no2=11)
    print("subtractiom is :",Ans)
    print()
    
    Ans = sub1(no2=10, no1=11)
    print("subtractiom is :",Ans)


if __name__== "__main__":
    main()