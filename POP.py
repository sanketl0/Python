
def Add(value1,value2):
    Ans = value1+value2
    return Ans

def sub(value1,value2):
    Ans = value1-value2
    return Ans

def main():
    print("enter a first number:")
    no1 = int(input())

    print("enter a second number:")
    no2 = int(input())

    Ans = Add(no1,no2)
    print("Addition is :",Ans)

    Ans = sub(no1,no2)
    print("subtraction is :",Ans)

if __name__ == "__main__":
    main()