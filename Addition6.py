print("application to demonstate Industrial Programming")

def Addition(Value1, Value2):
    Ans = Value1 + Value2
    return Ans

def main():
    print("Enter first number:")
    no1 = int(input())
    print("Enter second number:")
    no2 = int(input())

    Sum = Addition(no1, no2)

    print("Addition is:",Sum)

if __name__ == "__main__":
    main()